import unittest

from reporting import SARIF_SCHEMA, build_sarif


class SarifReportingTests(unittest.TestCase):
    def test_safe_results_are_omitted(self):
        sarif = build_sarif(
            {
                "url": "https://example.com",
                "verdict": "SAFE",
                "probability": 0.1,
                "features": {},
            }
        )

        self.assertEqual(sarif["$schema"], SARIF_SCHEMA)
        self.assertEqual(sarif["version"], "2.1.0")
        self.assertEqual(sarif["runs"][0]["results"], [])

    def test_phishing_result_is_an_error_with_explainable_properties(self):
        result = {
            "url": "http://paypa1-secure-login.xyz/verify",
            "verdict": "PHISHING",
            "probability": 0.98,
            "features": {"suspicious_tld": 1},
        }

        sarif_result = build_sarif(result)["runs"][0]["results"][0]

        self.assertEqual(sarif_result["ruleId"], "PHISHGUARD_PHISHING")
        self.assertEqual(sarif_result["level"], "error")
        self.assertEqual(sarif_result["properties"]["probability"], 0.98)
        self.assertEqual(
            sarif_result["properties"]["features"],
            {"suspicious_tld": 1},
        )
        self.assertEqual(
            sarif_result["locations"][0]["logicalLocations"][0]["kind"],
            "url",
        )

    def test_fingerprints_are_deterministic(self):
        result = {
            "subject": "Urgent account warning",
            "verdict": "SUSPICIOUS",
            "probability": 0.65,
            "features": {"urgency_word_count": 1},
        }

        first = build_sarif(result)["runs"][0]["results"][0]
        second = build_sarif(result)["runs"][0]["results"][0]

        self.assertEqual(first["level"], "warning")
        self.assertEqual(first["partialFingerprints"], second["partialFingerprints"])
        self.assertEqual(
            first["locations"][0]["logicalLocations"][0]["kind"],
            "email",
        )


if __name__ == "__main__":
    unittest.main()

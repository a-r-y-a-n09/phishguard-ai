# PhishGuard AI Roadmap

The roadmap is maintained by
[Omobolaji Adeyan](https://github.com/omobolajiadeyan). Implementation work is
tracked in GitHub issues so contributors can discuss and claim scoped tasks.

## Current Priorities

| Priority | Work | Status |
| --- | --- | --- |
| Portability | [Plain ASCII output mode](https://github.com/omobolajiadeyan/phishguard-ai/issues/1) | Good first issue |
| Detection | [IDN and punycode signals](https://github.com/omobolajiadeyan/phishguard-ai/issues/2) | Help wanted |
| Quality | [Labeled calibration benchmark](https://github.com/omobolajiadeyan/phishguard-ai/issues/3) | Help wanted |

## Next

- Email-header analysis for SPF, DKIM, and DMARC indicators
- URL redirect-chain and hostname-normalization analysis
- SARIF export for code-scanning and security pipelines
- A documented Python API in addition to the command-line interface
- Reproducible evaluation against public-safe labeled datasets

## Later

- Optional trained model support while preserving the explainable heuristic mode
- REST API wrapper for SOC integrations
- Browser integration after the detection benchmark is mature

Roadmap items are not promises or deadlines. Priorities may change when
testing, security review, or contributor feedback reveals a better direction.

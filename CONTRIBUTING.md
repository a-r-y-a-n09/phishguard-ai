# Contributing to PhishGuard AI

Thank you for helping improve PhishGuard. Contributions should make detection
more accurate, explainable, portable, or easier to verify.

## Development Setup

PhishGuard uses only the Python standard library.

```bash
git clone https://github.com/omobolajiadeyan/phishguard-ai.git
cd phishguard-ai
python -m unittest discover -s tests -v
```

Python 3.10 or newer is supported.

## Good Contributions

- Add labeled legitimate and phishing samples with a source and rationale.
- Reduce false positives without weakening existing malicious test cases.
- Add explainable URL or email features with focused unit tests.
- Improve cross-platform CLI behavior.
- Improve documentation when it is tied to verified behavior.

Do not include live credentials, private email, personal data, or active
phishing payloads. Use reserved domains and clearly synthetic samples in tests.

## Pull Requests

1. Open or reference an issue describing the behavior.
2. Comment on the issue and wait for a maintainer to confirm the approach
   before starting substantial work. This avoids duplicate pull requests.
3. Keep the change focused. Draft pull requests are welcome for early feedback.
4. Add tests that fail before the change and pass afterward.
5. Run `python -m unittest discover -s tests -v`.
6. Explain any scoring or threshold change with before-and-after examples.

An issue normally has one active implementation. You can still contribute by
reviewing an open pull request, reproducing the behavior, suggesting test
cases, or choosing another unclaimed issue.

Detection changes should include both positive and negative samples. A model
change that catches more phishing but labels common legitimate sites as
malicious is a regression.

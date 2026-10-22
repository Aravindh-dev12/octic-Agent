# Octic AI Agent Security Policy

Octic AI Agent takes security reports seriously. Please report suspected vulnerabilities responsibly and avoid publishing exploit details before maintainers have had a chance to assess the issue.

## Reporting a vulnerability

Use GitHub's private security advisory flow for this repository:

https://github.com/Aravindh-dev12/octic-Agent/security/advisories/new

Please include:
- The affected component and version or commit.
- A concise impact summary.
- Reproduction steps and relevant configuration.
- Any suggested mitigation, if known.

Do not include live API keys, passwords, personal data, or other secrets in a report. If private advisories are unavailable, contact the repository maintainer through GitHub before sharing technical details publicly.

## Scope

Reports are most useful when they involve a practical security impact in supported configurations, including:
- Authentication, authorization, and session handling.
- Secret handling and unsafe defaults.
- Agent tool execution, sandbox boundaries, or unintended code execution.
- API, web, MCP, and webhook integrations.
- Injection, unsafe deserialization, or server-side request forgery.
- Vulnerabilities in dependencies as used by Octic AI Agent.

For a third-party dependency issue, identify the exact dependency and version so the report can be triaged accurately.

## Out of scope

- Findings that require an already-compromised operator account or machine.
- Theoretical issues without a practical impact in a supported configuration.
- Vulnerabilities in unsupported or obsolete versions with no realistic upgrade path.
- Reports that disclose secrets or exploit details publicly before coordinated disclosure.

## Response process

Maintainers will review the report, attempt to reproduce the issue, determine severity and affected versions, and coordinate an appropriate fix or mitigation. Please allow reasonable time for triage and remediation before public disclosure.

## Public issues

Do not use public issues for unpatched vulnerabilities or sensitive exploit details. Use the private reporting flow above.

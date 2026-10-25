# Homemade Detection Rules

## Author note

This directory contains detection rules created from hands-on investigation in
the SOC homelab. It is the main working area for developing and testing new
detections from observed attacker or malware behavior.

The current rules originated from the BlueHammer POC investigation. The POC was
run in the isolated homelab, the resulting endpoint activity was investigated,
and the observed logs were used to create detection logic.

This collection is still in progress. More rules will be added as additional
investigations are completed.

## Current rules

Each rule has two representations:

1. A Sigma rule for portable detection logic.
2. A Splunk SPL version for direct use as a saved search or alert.

| Detection | Sigma | Splunk | Severity |
|---|---|---|---|
| EICAR in a user staging directory | [Sigma](sigma/win_defender_eicar_user_staging_directory.yml) | [Splunk](splunk/win_defender_eicar_user_staging_directory.txt) | Low |
| Suspicious Defender artifact creation | [Sigma](sigma/file_event_win_suspicious_defender_artifact_creation.yml) | [Splunk](splunk/file_event_win_suspicious_defender_artifact_creation.txt) | High |

The Splunk versions are prepared for validation as saved searches or alerts.
Before deployment, test them against the expected event source and confirm
false-positive behavior in the lab.

## Detection development process

```text
BlueHammer POC activity
        |
        v
Collect and investigate endpoint logs
        |
        v
Identify behavior and useful fields
        |
        v
Create Sigma detection logic
        |
        v
Convert and validate Splunk SPL
        |
        v
Save as alert and configure actions
        |
        v
Deploy and continue tuning
```

For each future rule, document:

- Investigation or POC source
- Data source and required sourcetype
- Important fields and event IDs
- Detection logic
- False positives
- Severity and MITRE mapping
- Sigma rule
- Splunk conversion
- Validation results
- Alert and deployment status

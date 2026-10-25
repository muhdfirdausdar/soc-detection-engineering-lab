# Splunk to n8n Alert Integration

## Data flow

```text
Splunk alert action
  |
HTTP POST webhook
  |
n8n Webhook -> Edit Fields -> Jira Create Issue
```

The workflow shown in [n8n-workflow.md](../n8n-workflow.md) receives a Splunk
alert, prepares the issue fields, and sends the result to Jira Cloud.

## Webhook endpoint

The n8n workflow receives Splunk alert data through this webhook endpoint:

```text
http://10.20.30.10:5678/webhook/splunk-alert
```

Use the **Test URL** while the Webhook node is listening for a test event. Use
the **Production URL** when the workflow is active.

## Test payload

```json
{
  "result": {
    "alertId": "12345",
    "alertTitle": "Unrecognized Device Logon",
    "severity": "medium",
    "user": "sample-user",
    "agentName": "WIN-SRV01",
    "src_ip": "10.10.10.20"
  }
}
```

The expressions shown in the workflow screenshots expect the alert values at
`$json.body.result.*`. If testing with a direct JSON body instead, use paths
such as `$json.body.alertTitle` or update the test payload to match the
Splunk-shaped structure.

## Send a test alert

In n8n, open the Webhook node and select **Listen for test event**. Then run
[test-splunk-webhook.ps1](../test-splunk-webhook.ps1) from PowerShell using the
test URL:

```powershell
.\test-splunk-webhook.ps1
```

The event descriptions in [descriptions](../descriptions/) provide the field
layout for Windows and Microsoft 365 alert details.

Configure the Splunk alert action to send an HTTP POST request containing the
alert JSON to the n8n webhook URL. The Splunk example in
`splunk-n8n-integration-webhook-alert.png` shows this action configured for the
`User Account Created or Enabled` alert.

## Validation

1. Confirm the Webhook node receives the POST request.
2. Confirm Edit Fields produces `summary`, `priority`, and `description`.
3. Confirm the Jira node creates one issue in the selected project.
4. Search Splunk for the originating alert and compare it with the Jira issue.

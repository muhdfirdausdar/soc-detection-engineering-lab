$body = @{
    result = @{
        alertId = "12345"
        alertTitle = "Unrecognized Device Logon"
        severity = "medium"
        user = "sample-user"
        agentName = "WIN-SRV01"
        src_ip = "10.10.10.20"
    }
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://10.20.30.10:5678/webhook-test/splunk-alert" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

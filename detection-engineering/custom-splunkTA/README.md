# Custom Splunk TAs

This directory contains custom Splunk add-ons created for the SOC homelab.
Each TA packages configuration, knowledge objects, lookups, and documentation
for one technical purpose.

## Standard TA structure

```text
custom-splunkTA/
├── README.md
├── TA-fortigate-ocsf/
│   ├── README.md
│   ├── default/
│   ├── local/
│   └── metadata/
└── SOC_Detections/
    ├── default/
    ├── local/
    ├── lookups/
    └── metadata/
```

A Splunk app or TA can contain additional directories such as `lookups/`,
`bin/`, `static/`, and `appserver/` when the app needs them.

## Configuration directories

### `default/`

Contains the app's baseline configuration. It is useful for distributable
configuration and documents the default behavior of the app.

Do not edit files inside an installed app's `default/` directory. Put local
changes in `local/` so upgrades and app updates do not overwrite them.

### `local/`

Contains configuration that overrides or extends the values in `default/`.
This is where lab-specific and deployment-specific settings belong.

Examples:

```text
local/props.conf
local/transforms.conf
local/macros.conf
local/indexes.conf
local/savedsearches.conf
```

Splunk applies configuration using file precedence. Local configuration takes
precedence over default configuration.

### `metadata/`

Contains `.meta` files that control Splunk knowledge-object visibility and
sharing. Metadata is not the same as Windows filesystem permissions.

For example:

```text
metadata/local.meta
```

```ini
[props]
export = system
```

The `export` setting controls where the knowledge object is available:

| Value | Scope |
|---|---|
| `app` | Available only inside the current app |
| `system` | Exported globally and available across apps |

Use `export = system` when a `props.conf` rule must apply to events searched
from other apps, such as the FortiGate normalization TA. Use `export = app`
when the configuration should remain limited to the app.

The `metadata/` setting controls Splunk knowledge-object scope; it does not
change the operating system's read/write permissions on the files. The Splunk
service account still needs filesystem access to the installed app directory.

## Installing a TA

Copy the complete TA directory into the Splunk Enterprise apps directory:

```text
<SPLUNK_HOME>\etc\apps\TA-name
```

Example:

```text
D:\Program Files\Splunk\etc\apps\TA-fortigate-ocsf
```

Keep the app directory name stable because it is used by Splunk to identify the
app and its configuration.

After copying or changing a TA, restart Splunk:

```bat
cd /d "D:\Program Files\Splunk\bin"
splunk.exe restart
```

## Verify that Splunk loaded the TA

Check that the app is installed:

```bat
cd /d "D:\Program Files\Splunk\bin"
splunk.exe list app
```

Inspect the effective configuration and its source files:

```bat
splunk.exe btool props list fortigate --debug
```

The `--debug` output helps confirm whether Splunk loaded the expected file from
the TA's `local/` directory.

For search-time field extraction, run a representative search and confirm the
expected fields are present:

```spl
index=firewall sourcetype=fortigate
| head 1
| table _raw device.uid src_endpoint.ip dst_endpoint.ip
```

## Deployment checklist

1. Confirm the TA directory contains the expected files.
2. Copy the complete directory into `$SPLUNK_HOME/etc/apps/`.
3. Confirm ownership and filesystem access for the Splunk service account.
4. Restart Splunk after configuration changes.
5. Use `btool` to inspect the effective configuration.
6. Run a representative search.
7. Confirm knowledge-object scope matches the intended app or global use.
8. Document the TA purpose and dependencies in its own README.

See [TA-fortigate-ocsf](TA-fortigate-ocsf/README.md) for the first custom TA.

See [SOC_Detections](SOC_Detections/README.md) for the detection collection app.

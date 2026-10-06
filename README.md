# Jamf Pro + Intune Migration Playbook

A practical, client-facing playbook for planning a **macOS MDM migration from Microsoft Intune to Jamf Pro** while designing the **Jamf Pro + Microsoft Intune device-compliance integration**. It connects ABM assignment, Jamf Computer PreStage Enrollment, user/device registration, policy translation, phased cutover, validation, and rollback.

This is a portfolio reference project, not a tenant-specific migration package. All sample assets, serials, groups, IDs, dates, and outcomes are synthetic. There are no credentials, tokens, certificates, tenant identifiers, or customer data. Included tooling reconciles sanitized CSV exports locally; it makes no API calls and changes no device or tenant state.

## The key distinction

“Move from Intune to Jamf” can mean two different things:

1. **Change the MDM authority:** move macOS configuration, app deployment, inventory, and lifecycle management from Intune to Jamf Pro. ABM assignment and the enrollment path must be planned; changing a console assignment does not convert an already-enrolled device in place.
2. **Keep Jamf Pro as MDM and integrate compliance with Intune/Entra:** Jamf remains responsible for Mac management, while Jamf device-compliance data is made available to Microsoft access/compliance workflows. This is not dual MDM enrollment.

This repo documents both tracks, including the separate transition from Jamf's legacy macOS Conditional Access integration to the current Device Compliance integration. Always confirm the supported method, prerequisites, licensing, and timing against current vendor documentation before a live change.

## What this demonstrates

- Migration discovery and readiness gates for a mixed Apple fleet.
- A control-by-control mapping from Intune to Jamf with explicit disposition and validation evidence.
- ABM and Jamf Computer PreStage enrollment planning for organization-owned Macs.
- Pilot, wave rollout, user communications, cutover, exception handling, and rollback.
- Clear policy ownership between Jamf Pro, Intune, and Microsoft Entra ID.
- Safe, local, read-only reconciliation of synthetic Intune and Jamf inventory exports.
- Current Jamf/Intune compliance integration considerations and legacy integration caveats.

## Repository map

| Topic | Guide |
|---|---|
| Architecture and terminology | [Integration architecture](docs/integration-architecture.md) |
| Intune MDM to Jamf Pro MDM transition | [Migration workflow](docs/intune-to-jamf-migration.md) |
| ABM, ADE, and PreStage readiness | [Enrollment and PreStage](docs/abm-ade-prestage-readiness.md) |
| Policy and workload translation | [Control mapping](docs/control-mapping.md) |
| Jamf + Intune compliance integration | [Device compliance integration](docs/device-compliance-integration.md) |
| Cutover and recovery | [Cutover and rollback](docs/cutover-and-rollback.md) |
| Script permissions and data handling | [Safety and limitations](docs/safety-and-limitations.md) |
| Synthetic wave worksheet | [Templates](templates/) |

## Quick start: compare sanitized exports

The example script compares the serials in two CSV exports. It reports whether a synthetic device appears in each source and flags duplicate or unmatched serials. It does not query either product, decide compliance, or modify records.

```sh
python3 examples/scripts/reconcile-inventory.py \
  --intune examples/intune-export/intune-devices.csv \
  --jamf examples/jamf-export/jamf-computers.csv \
  --output ./reconciliation.json
```

Use only approved, sanitized exports. Output is created at the explicit path and existing files are not overwritten. See [Safety and limitations](docs/safety-and-limitations.md) before using real exports.

## Practical boundary

There is no universal one-click or guaranteed in-place Intune-to-Jamf migration. Enrollment method, ABM ownership, supervision, current MDM restrictions, user data, FileVault escrow, bootstrap/account state, app delivery, security controls, and access policies all affect the sequence. The runbooks deliberately require a device-level pilot and explicit approval before destructive actions such as erase/re-enrollment.

## License

MIT. See [LICENSE](LICENSE).

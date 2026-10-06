# Safety, prerequisites, and limitations

## Included tool

`examples/scripts/reconcile-inventory.py` is local-only and read-only. It reads two CSV exports, compares serial numbers, identifies duplicate/missing entries, and writes JSON to an explicitly named new output file. The report includes serials for unmatched/duplicate records so an operator can reconcile them. It does not connect to Apple, Jamf Pro, Intune, or Entra ID; make API calls; change management state; or infer compliance.

Only the synthetic sample CSVs are safe to publish. Real exports and reports can contain serial numbers, device names, usernames, or other personal/asset data. Do not commit real exports or generated reports. Follow organizational approval, minimization, retention, and access-control requirements.

## Requirements and permissions

- Python 3.9+ for local CSV reconciliation; no third-party modules.
- No management API credentials or elevated local permissions for the sample script.
- Console work described in the runbooks requires authorized Jamf, ABM, Intune, and Entra roles, based on current vendor requirements. Use least privilege and a test scope.
- The connector may request Microsoft permissions and admin consent. Review current documentation and consent scope before configuration.

## Limits

Migration behavior depends on Apple enrollment type, ABM assignment, macOS version, Jamf Pro/Intune releases, identity policy, and organizational data-protection controls. The examples do not determine whether a given device can transition in place or needs to be erased/re-enrolled. They do not validate connector health or policy enforcement. Treat unknown data as unknown and have platform administrators validate each change in a lab and pilot.

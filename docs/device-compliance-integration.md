# Jamf Pro and Intune device-compliance integration

This guide is about compliance reporting for Macs managed by Jamf Pro. It does **not** describe enrolling the same Mac into two MDM authorities and does not replace the [MDM authority migration workflow](intune-to-jamf-migration.md).

## Current design direction

Jamf Pro evaluates its selected compliance criteria and reports device compliance into Microsoft Entra through the supported Jamf/Microsoft integration. Microsoft Intune participates as the compliance partner and Entra Conditional Access remains the access decision point. Follow the current Jamf Cloud Connector and Microsoft integration documentation for your product versions and tenant.

Jamf's macOS Conditional Access integration is deprecated; the repository treats the Device Compliance integration as the current target. Do not start a new design from old Conditional Access integration instructions.

## Design and validation checklist

1. Verify Jamf Pro and Microsoft tenant versions, licensing, cloud/service prerequisites, admin roles, connector support, and network paths from current vendor docs.
2. Define Jamf **Applicable** and **Compliance** device groups. The applicable population should represent devices expected to register; the compliance group should encode the actual approved requirements.
3. Decide on inventory freshness, FileVault evidence, minimum OS, required apps, remediation windows, and exception handling.
4. Configure the supported connector in a pilot tenant/scope. Review every requested Microsoft permission and use authorized administrators.
5. Register a test Mac/user. Validate Company Portal or the documented registration flow, Jamf inventory, partner connector health, Intune compliance evaluation, Entra device state, and Conditional Access behavior.
6. Test a compliant and intentionally noncompliant scenario with approved test devices. Confirm transitions, latency, recovery, user messaging, and sign-in logs.
7. Expand scope only after the full path is observable and supportable.

## Legacy Conditional Access transition

Organizations already using Jamf's older macOS Conditional Access integration must follow Jamf's migration procedure to Device Compliance. Jamf documentation describes a Microsoft Intune grace period after legacy integration is disabled and advises enabling Device Compliance promptly; the time window and sequence are vendor-version-sensitive. Follow current Jamf instructions and do not re-enable the retired path as an informal rollback. Establish a support-approved recovery plan before changing production integration.

## Common failure classes

- User/device registration is blocked by Conditional Access targeting the registration app.
- Duplicate device registrations or stale Entra/Intune objects confuse evaluation.
- Compliance policy targets the wrong identity/group scope.
- Jamf inventory is stale or the selected compliance group criteria don't match approved intent.
- Connector, Company Portal, SSO extension, licensing, or network prerequisites are incomplete.
- A legacy integration was disabled without coordinating the Device Compliance transition.

Troubleshoot by capturing sanitized timestamps, affected cohort, connector status, device registration state, policy assignment, and sign-in outcomes. Do not include tokens, secrets, recovery keys, or personal user identifiers in issue artifacts.

## Official references

- [Jamf: Device Compliance with Microsoft Entra and Jamf Pro](https://learn.jamf.com/r/en-US/technical-paper-microsoft-intune-current/Configuring_the_Microsoft_Intune_Integration)
- [Jamf: Requirements for Jamf Pro device compliance](https://learn.jamf.com/r/en-US/technical-paper-microsoft-intune-current/Device_Compliance_Requirements)
- [Jamf: Migrate from macOS Conditional Access to Device Compliance](https://learn.jamf.com/r/en-US/technical-paper-microsoft-intune-current/Migrating_from_macOS_Conditional_Access_to_macOS_Device_Compliance)
- [Microsoft: Integrate Jamf Pro with Intune to report compliance to Entra ID](https://learn.microsoft.com/en-us/intune/device-security/compliance/jamf-entra-id)
- [Microsoft: Troubleshoot Jamf Pro integration with Intune](https://learn.microsoft.com/en-us/troubleshoot/mem/intune/troubleshoot-jamf)

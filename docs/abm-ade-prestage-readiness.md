# ABM, ADE, and Jamf PreStage readiness

## What each part does

- **Apple Business Manager (ABM):** organization device records and assignment to an MDM service.
- **Automated Device Enrollment (ADE):** Apple's enrollment experience during supported initial setup/activation.
- **Jamf Computer PreStage Enrollment:** configures the ADE setup experience and associates eligible Macs with Jamf enrollment settings.
- **Configuration profiles and policies:** deliver settings and operational tasks after the device enrolls; they are not the PreStage itself.

An ABM assignment change affects the device the next time it goes through Setup Assistant; it does not replace a current MDM enrollment. Plan the current device state and the transition method rather than assuming assignment alone migrates it.

## Pre-migration gates

- [ ] Device is organization-owned and ABM record is verified against the asset system.
- [ ] Intended Jamf MDM server is configured and selected for the device.
- [ ] ADE token/integration health, expiry owner, and latest sync are recorded.
- [ ] Jamf Computer PreStage has a documented owner, settings review, assignment scope, and rollback/change record.
- [ ] Setup Assistant and authentication design is tested with synthetic/test identities.
- [ ] Account creation, bootstrap/local admin, FileVault escrow, and recovery approach are proven on a lab Mac.
- [ ] Required network services and URLs are reachable during Setup Assistant and post-enrollment.
- [ ] User notice, data backup, interruption window, and service desk path are published.
- [ ] Enrollment transition method is explicitly approved per cohort and macOS state.

## Synthetic PreStage worksheet

| Setting intent | Example | Validation evidence |
|---|---|---|
| PreStage | `MIGRATION-PILOT-MACOS-01` | Jamf scope and owner reviewed |
| ABM MDM server | `EXAMPLE-JAMF-PROD` | Matching asset records in ABM |
| Cohort | `Synthetic pilot wave A` | 5 test Macs, no production wildcard |
| Authentication | `Test identity required` | Successful Setup Assistant flow |
| Setup Assistant panes | `Only approved panes skipped` | User impact and privacy reviewed |
| Account handling | `Approved bootstrap workflow` | Local account and MDM-enabled behavior validated |
| Initial payload scope | `MIGRATION-PILOT smart group` | Profiles and apps apply as expected |
| Support/rollback owner | `Example Endpoint Ops` | Named, reachable during test window |

Values are fictional, not an importable Jamf configuration. Setting names and behavior can vary by Jamf Pro/macOS version.

## Official references

- [Jamf Pro: Computer PreStage Enrollment](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Configuring_a_Computer_PreStage_Enrollment)
- [Apple: Automated Device Enrollment](https://support.apple.com/guide/security/automated-device-enrollment-secc2cd563ef/web)
- [Apple: Device Enrollment and device management](https://support.apple.com/guide/deployment/device-enrollment-and-device-management-depd1c27dfe6/1/web)

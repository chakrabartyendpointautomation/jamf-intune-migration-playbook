# Intune-to-Jamf workload and control mapping

Use this as a mapping workshop template. Each row needs a source owner, target owner, implementation decision, test evidence, and exception owner. Product settings are not assumed to have one-to-one equivalents.

| Source area | Target decision | Questions / evidence |
|---|---|---|
| ABM assignment / ADE enrollment | Preserve or correct ABM assignment; Jamf PreStage | Is the device org-owned and eligible? What enrollment transition is approved? |
| Configuration profiles | Recreate supported payloads in Jamf or retire | Does the payload exist for target macOS? Could old/new profiles conflict? |
| macOS compliance policy | Define Jamf inventory criteria and compliance group | Which evidence is authoritative, fresh, and reported to Entra? |
| Applications | Rebuild distribution and update ownership in Jamf | License, package trust, architecture, deployment timing, update/rollback? |
| Scripts and remediation | Reimplement as reviewed Jamf policy or approved tool | Are scripts idempotent, scoped, logged, and safe to roll back? |
| FileVault | Reconfigure escrow and recovery handling in Jamf | Is recovery key escrow verified before source is retired? Keep keys out of reports. |
| Wi-Fi, VPN, certificates | Rebuild with certificate issuance/renewal dependencies | Will connectivity survive the management transition and token rotation? |
| SSO / Company Portal | Preserve identity registration and test user flows | Is registration needed for device-compliance reporting? What policies can block setup? |
| System extensions, PPPC/TCC, security | Stage and validate target payloads/approvals | Which apps require user prompts or OS-specific payloads? |
| Update policies | Assign clear update owner | Are deferrals, deadlines, and restart expectations compatible? |
| Groups and assignments | Rebuild Jamf smart/static groups and Entra scopes | Can stale or duplicate objects cause scope drift? |
| Conditional Access / compliance connector | Keep Entra access authority; configure supported Jamf device compliance flow | Is this the current Device Compliance integration, not legacy macOS Conditional Access? |

## Disposition labels

- `recreate`: implement in Jamf with reviewed target behavior.
- `replace`: use a different supported control to achieve the same objective.
- `retire`: no longer required; owner approves removal.
- `retain-integration`: remains in Microsoft for identity/compliance/access integration but does not make Intune the Mac MDM authority.
- `exception`: documented reason, owner, compensating control, expiry/review date.

## Mapping record fields

Use `templates/control-mapping.csv` as a starter. Record evidence and approval; never mark a control migrated solely because a profile or policy object was created in the target console.

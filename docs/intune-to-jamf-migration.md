# Intune MDM to Jamf Pro MDM migration

This runbook covers a change in macOS management authority. It is not a compliance-connector setup guide; see [Device Compliance Integration](device-compliance-integration.md) for that separate track.

## Migration principles

- Treat migration as a controlled service transition, not simply a product switch.
- Inventory first and group devices by ownership, enrollment method, user, OS, location, criticality, and ABM eligibility.
- Build and validate the Jamf target state before detaching source devices.
- Keep one clearly identified MDM authority per device during each migration wave.
- Do not assume ABM assignment changes take effect on currently enrolled devices; plan the required activation or approved enrollment transition.
- Never delete source records, release an ABM asset, remove a management profile, or erase a Mac as an exploratory troubleshooting step.

## Phase 0: agree scope and service ownership

1. Name the business owner, Jamf admin, Intune admin, identity/access owner, service desk lead, and change approver.
2. Define eligible device cohort, exclusion rules, migration window, support coverage, success measures, and maximum acceptable interruption.
3. Decide target management boundaries: Jamf owns Apple MDM; Entra owns identity/access; Intune may remain in the compliance integration path where configured.
4. Define user data backup, FileVault recovery, local admin/bootstrap, app licensing, and device return requirements.
5. Record risks, dependencies, change approvals, and rollback decision authority.

## Phase 1: discover and reconcile

Collect approved exports from Intune, Jamf (if already partially deployed), and ABM asset records. Use the local script with **sanitized** CSVs to reconcile stable serials. Record source and export timestamps. Resolve missing, duplicate, stale, or conflicting records before selecting a wave.

Minimum cohort fields: asset/serial, ownership, assigned user, current MDM authority, ABM assignment, enrollment type, OS/build, last check-in, FileVault status/key-escrow evidence, required apps, identity registration, criticality, support region, migration eligibility, and exception owner.

Never treat an absent field as compliant. Use `unknown` until evidence is confirmed.

## Phase 2: translate policies and service dependencies

For each source workload, choose one disposition: `recreate`, `replace`, `retire`, `retain-in-Intune-integration`, or `exception`. Map intent, not just settings; see [Control Mapping](control-mapping.md).

- Convert configuration profiles into supported Jamf-managed profile designs, checking payload support and macOS version behavior.
- Rebuild app assignments and update ownership; validate licenses, package signatures, deployment method, and user impact.
- Translate compliance controls into Jamf inventory criteria / smart groups and define how the supported Intune/Entra integration consumes them.
- Reconcile scripts/remediations with Jamf policy or another approved automation design; remove obsolete overlapping agents only with a tested plan.
- Map update enforcement, FileVault escrow, certificates, Wi-Fi/VPN, SSO, PPPC/TCC, kernel/system extensions, and local admin flows explicitly.

## Phase 3: prepare ABM and Jamf enrollment

1. Verify ABM records, owner, MDM server assignment, Jamf ADE integration/token state, and device eligibility.
2. Build a dedicated lab Computer PreStage Enrollment and validate authentication, account creation, Setup Assistant, management controls, and scope.
3. Confirm network access to Apple, Jamf, Microsoft identity/registration, and package sources during enrollment.
4. Decide whether each cohort uses ADE reactivation/re-enrollment or another supported enrollment method. Document the user and data impact for the exact Mac and macOS release.
5. Validate Jamf profile/app ordering, FileVault configuration and escrow, Self Service, inventory, and support channel on a spare test Mac.
6. Keep ABM assignments and production PreStage scopes restricted to approved devices.

See [ABM, ADE, and PreStage Readiness](abm-ade-prestage-readiness.md).

## Phase 4: pilot and migration wave

1. Select a small representative, recoverable cohort; exclude executive, regulated, or high-criticality devices until the workflow is proven unless explicitly approved.
2. Communicate action, timing, expected prompts, backup/recovery, work interruption, and support contact.
3. Capture pre-change inventory, access state, encryption/key escrow evidence, app list, and a timestamped change record.
4. Follow the approved source-MDM retirement and Jamf enrollment sequence for the cohort. Steps vary with existing enrollment method and ABM assignment; do not generalize an erase/un-enroll action across all devices.
5. Run the post-enrollment acceptance checklist and reconcile expected cohort against Jamf inventory.
6. Keep the wave open until all exceptions are owned and access, apps, security controls, and support are confirmed.

## Phase 5: scale and close

Promote through waves only after gate review. Compare migrated, pending, excluded, exception, and duplicate counts with the approved cohort. Retire old profiles, groups, packages, connectors, and licenses only after no in-scope device depends on them and records are retained according to policy.

Close with an operational owner, final reconciliation, known limitations, user feedback, exception expiry dates, and an approved change record.

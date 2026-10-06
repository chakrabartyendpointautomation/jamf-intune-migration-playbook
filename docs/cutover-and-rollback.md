# Cutover gates and rollback planning

## Go/no-go gate

Do not start a wave until each item has an owner and evidence:

- Source and target exports reconciled; duplicate/missing serials resolved or excluded.
- ABM assignment and Jamf PreStage scope correct for the approved wave.
- User communication, backup, recovery, and service desk coverage confirmed.
- Required profiles, apps, FileVault escrow, identity registration, and access flows passed pilot acceptance.
- Migration steps are documented for the actual enrollment method and device state.
- Rollback authority, decision deadline, and recovery actions approved.
- Compliance connector state and any legacy-integration transition are coordinated.

## Post-cutover acceptance per device

- Jamf Pro inventory identifies the expected synthetic/asset serial and enrollment method.
- The Mac is in the intended PreStage-derived scope and target smart groups.
- Required profiles are installed and report expected status.
- Required apps launch at approved versions and user access works.
- FileVault is enabled as intended and escrow is verified in Jamf Pro through approved access.
- Identity registration, compliance evaluation, and Conditional Access work for intended test scenarios.
- Intune's former MDM assignments no longer apply unexpectedly; records are retained or retired under policy.
- User confirms work access and support contact; exceptions are logged with owner and due date.

## Rollback design

Rollback is not automatically “reenroll in Intune.” Before each wave, decide whether the safe recovery is to pause the wave, correct Jamf policy, use a supported enrollment path back to source, restore a backup, or return the device for hands-on recovery. MDM ownership changes and ABM activation routing may constrain reversibility.

Define explicit triggers such as failed enrollment, unexpected data loss, FileVault/recovery failure, widespread app/access failure, incorrect security scope, or connector-wide compliance errors. Record who can pause further waves and who can authorize any erase, unenrollment, ABM reassignment, or user-data recovery action.

Never include FileVault recovery keys, credentials, or tokens in this record. Refer to approved secret/key systems only.

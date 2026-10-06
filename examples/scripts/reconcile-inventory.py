#!/usr/bin/env python3
"""Compare sanitized Intune and Jamf CSV exports by serial number, locally."""
import argparse
import csv
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def load_serials(path: Path) -> Counter:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "serial_number" not in reader.fieldnames:
            raise ValueError(f"{path}: required CSV column 'serial_number' is missing")
        values = []
        for row_number, row in enumerate(reader, start=2):
            serial = (row.get("serial_number") or "").strip().upper()
            if not serial:
                continue
            values.append(serial)
        return Counter(values)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intune", required=True, type=Path, help="Intune CSV export")
    parser.add_argument("--jamf", required=True, type=Path, help="Jamf CSV export")
    parser.add_argument("--output", required=True, type=Path, help="New JSON report path (will not overwrite)")
    args = parser.parse_args()

    if not args.intune.is_file() or not args.jamf.is_file():
        parser.error("both input paths must be existing files")
    if args.output.exists():
        parser.error(f"refusing to overwrite existing file: {args.output}")

    try:
        intune = load_serials(args.intune)
        jamf = load_serials(args.jamf)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    intune_ids, jamf_ids = set(intune), set(jamf)
    report = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "local_csv_reconciliation",
        "compliance": "unknown",
        "counts": {
            "intune_rows_with_serial": sum(intune.values()),
            "jamf_rows_with_serial": sum(jamf.values()),
            "in_both": len(intune_ids & jamf_ids),
            "intune_only": len(intune_ids - jamf_ids),
            "jamf_only": len(jamf_ids - intune_ids),
        },
        "duplicates": {
            "intune": sorted(serial for serial, count in intune.items() if count > 1),
            "jamf": sorted(serial for serial, count in jamf.items() if count > 1),
        },
        "unmatched_serials": {
            "intune_only": sorted(intune_ids - jamf_ids),
            "jamf_only": sorted(jamf_ids - intune_ids),
        },
        "limitations": [
            "Serial-number matching alone does not prove device ownership, enrollment health, or compliance.",
            "Validate duplicates, stale exports, reused records, and asset ownership with authorized systems.",
        ],
    }
    try:
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2)
            handle.write("\n")
        os.chmod(args.output, 0o600)
    except OSError as exc:
        print(f"Output error: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote local reconciliation report to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

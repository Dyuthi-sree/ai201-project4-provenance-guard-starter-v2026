"""
Persistent verified-human credentials.

This is a lightweight authorship attestation, not government identity
verification. A successful attestation earns a credential that appears on
future submissions from that creator_id.
"""

import json
from datetime import datetime, timezone

import config


CREDENTIAL_FILE = config.LOG_DIR / "verified_creators.json"
REQUIRED_ATTESTATION = "I confirm that I am the human author."


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read_credentials() -> dict:
    if not CREDENTIAL_FILE.exists():
        return {}

    try:
        data = json.loads(CREDENTIAL_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def verify_creator(creator_id: str, attestation: str) -> dict:
    """Award a persistent credential after the required attestation."""
    if not isinstance(creator_id, str) or not creator_id.strip():
        raise ValueError("A non-empty creator_id is required.")

    if attestation != REQUIRED_ATTESTATION:
        raise ValueError(
            f'Attestation must exactly match: "{REQUIRED_ATTESTATION}"'
        )

    creator_id = creator_id.strip()
    credentials = _read_credentials()

    credential = {
        "creator_id": creator_id,
        "credential": "verified-human",
        "verified_at": _now(),
        "verification_method": "authorship-attestation",
    }

    credentials[creator_id] = credential
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    CREDENTIAL_FILE.write_text(
        json.dumps(credentials, indent=2),
        encoding="utf-8",
    )

    return credential


def credential_for(creator_id: str) -> str | None:
    """Return a creator's credential, if one has been earned."""
    record = _read_credentials().get(creator_id)
    if not isinstance(record, dict):
        return None
    return record.get("credential")


if __name__ == "__main__":
    print(f'Required attestation: "{REQUIRED_ATTESTATION}"')
import json
from pathlib import Path


MANIFEST = Path(__file__).parent / "custom_components" / "casambi_bt" / "manifest.json"


def test_manifest_pins_the_timezone_safe_library_release() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert manifest["version"] == "1.9.0.dev14"
    assert manifest["requirements"] == [
        "casambi-bt-revamped@git+https://github.com/drschnalli/casambi-bt-revamped.git@v0.4.2.dev14"
    ]

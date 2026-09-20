# Casambi BT dev14 - stale ESPHome GATT cleanup

Versionen:
- casambi-bt-revamped: 0.4.2.dev14
- casambi-bt-hass: 1.9.0.dev14

Neu in dev14:
- Die Integration verwendet `casambi-bt-revamped@v0.4.2.dev14`.
- Der Bibliotheksstand räumt verwaiste ESPHome-GATT-Slots auch bei lokalem `is_connected=False` aktiv auf.
- Dadurch wird der beobachtete Zustand `not in allocated list []` beim nächsten Retry bereinigt.

---

# Casambi BT dev13 - dependency refresh and timezone-safe session expiry

Versionen:
- casambi-bt-revamped: 0.4.2.dev13
- casambi-bt-hass: 1.9.0.dev13

Neu in dev13:
- Die Integration verwendet den expliziten Tag `v0.4.2.dev13`.
- Dadurch verwirft Home Assistant eine eventuell noch gecachte alte CasambiBt-Installation und lädt den UTC-sicheren Bibliotheksstand neu.
- Die manifest-Version wurde gemeinsam mit der Dependency erhöht; ein direkter Commit-Pin wird nicht verwendet.

Verifiziert:
- Der Tag lässt sich mit pip als Wheel bauen.
- Der Zeitzonen-Regressionstest deckt naive, UTC-aware und offset-aware Ablaufzeiten ab.

---

# Casambi BT dev12 - expanded EVO pre-auth packet tolerance

Versionen:
- casambi-bt-revamped: 0.4.2.dev12
- casambi-bt-hass: 1.9.0.dev12

Neu in dev12:
- Unerwartete pre-auth Pakete vom Typ 0x04, 0x05 und 0x07 waehrend EVO-Key-Exchange werden nicht mehr sofort als fatal behandelt.
- Interner Retry fuer transiente EVO-Handshake-Fehler bleibt aktiv.

GitHub Releases:
- drschnalli/casambi-bt-revamped: Tag v0.4.2.dev12, Title casambi-bt-revamped 0.4.2.dev12
- drschnalli/casambi-bt-hass: Tag v1.9.0.dev12, Title casambi-bt-hass 1.9.0.dev12

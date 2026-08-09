# Casambi BT dev11 - internal EVO handshake retry + ignored stale packet fix

Versionen:
- casambi-bt-revamped: 0.4.2.dev11
- casambi-bt-hass: 1.9.0.dev11

Neu in dev11:
- Unerwartete pre-auth Pakete vom Typ 0x04 waehrend EVO-Key-Exchange werden nicht mehr sofort als fatal behandelt.
- Logmarker: [CASAMBI_HANDSHAKE_IGNORED_PACKET]
- Interner Retry fuer transiente EVO-Handshake-Fehler, bevor Home Assistant ConfigEntryNotReady anzeigen muss.
- Logmarker: [CASAMBI_KEY_EXCHANGE_RETRY]
- Timeout fuer Key-Exchange-Wartepunkte, damit ein ignoriertes Paket nie zu einem haengenden Setup fuehrt.

Environment-Variablen:
- CASAMBI_BT_HANDSHAKE_RETRY_ATTEMPTS=3
- CASAMBI_BT_HANDSHAKE_RETRY_DELAY_SECONDS=1.5
- CASAMBI_BT_KEY_EXCHANGE_NOTIFY_TIMEOUT_SECONDS=8.0

Bestehende Fixes bleiben enthalten:
- GATT/Auth-Read Retry
- GATT settle delay
- Reconnect/Cleanup Hardening
- Vollstaendiger timezone-aware datetime fix in _network.py
- casambi_bt.dump_diagnostics Service aus dev10

GitHub Releases:
- drschnalli/casambi-bt-revamped: Tag v0.4.2.dev11, Title casambi-bt-revamped 0.4.2.dev11
- drschnalli/casambi-bt-hass: Tag v1.9.0.dev11, Title casambi-bt-hass 1.9.0.dev11

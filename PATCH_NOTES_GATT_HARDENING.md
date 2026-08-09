# Casambi BT GATT/Reconnect Hardening Build

Versionen:
- casambi-bt-revamped: 0.4.2.dev7
- casambi-bt-hass: 1.9.0.dev7

Aenderungen:
1. Wartet nach erfolgreichem BLE-Connect kurz, bevor GATT/Protokoll geprueft wird. Default: 0.75 s.
2. Wiederholt den ersten EVO-Auth-Characteristic-Read, wenn Bleak die Characteristic kurzzeitig nicht findet. Default: 6 Versuche, 1 s Abstand.
3. Raeumt den BLE-Client nach jedem fehlgeschlagenen Handshake/Authentifizierungsversuch sauber auf, bevor HA erneut verbindet.
4. Manifest der HA-Integration wurde auf casambi-bt-revamped==0.4.2.dev7 und Version 1.9.0.dev7 gesetzt.

Optionale Environment-Variablen fuer Tests:
- CASAMBI_BT_GATT_SERVICE_SETTLE_SECONDS=0.75
- CASAMBI_BT_GATT_AUTH_READ_ATTEMPTS=6
- CASAMBI_BT_GATT_AUTH_READ_RETRY_SECONDS=1.0

Wichtig:
Wenn Home Assistant die Library per manifest.json aus PyPI installieren soll, muss casambi-bt-revamped 0.4.2.dev7 auch als Paket verfuegbar sein. Fuer lokale Tests kannst du die Library im HA-Container installieren oder die Version in manifest.json auf eine lokal verfuegbare/testweise installierte Version anpassen.

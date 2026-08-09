# Casambi BT GATT/Reconnect Hardening Build - GitHub Requirement Bundle

Versionen:
- casambi-bt-revamped: 0.4.2.dev7
- casambi-bt-hass: 1.9.0.dev7

Dieses Bundle ist die Variante mit bereits korrigiertem Home-Assistant-Manifest.

Wichtige Manifest-Aenderung:
- Die Home-Assistant-Integration installiert die Library direkt aus deinem GitHub-Repository:
  casambi-bt-revamped@git+https://github.com/drschnalli/casambi-bt-revamped.git@v0.4.2.dev7

Dafuer bitte im Repository drschnalli/casambi-bt-revamped einen GitHub-Release/Tag erstellen:
- Tag: v0.4.2.dev7
- Release title: casambi-bt-revamped 0.4.2.dev7

Und im Repository drschnalli/casambi-bt-hass:
- Tag: v1.9.0.dev7
- Release title: casambi-bt-hass 1.9.0.dev7

Aenderungen in der Library:
1. Wartet nach erfolgreichem BLE-Connect kurz, bevor GATT/Protokoll geprueft wird. Default: 0.75 s.
2. Wiederholt den ersten EVO-Auth-Characteristic-Read, wenn Bleak die Characteristic kurzzeitig nicht findet. Default: 6 Versuche, 1 s Abstand.
3. Raeumt den BLE-Client nach jedem fehlgeschlagenen Handshake/Authentifizierungsversuch sauber auf, bevor HA erneut verbindet.

Optionale Environment-Variablen fuer Tests:
- CASAMBI_BT_GATT_SERVICE_SETTLE_SECONDS=0.75
- CASAMBI_BT_GATT_AUTH_READ_ATTEMPTS=6
- CASAMBI_BT_GATT_AUTH_READ_RETRY_SECONDS=1.0

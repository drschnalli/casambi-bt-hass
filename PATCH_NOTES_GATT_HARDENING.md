# Casambi BT GATT/Reconnect Hardening + Session Timezone Fix

Versionen:
- casambi-bt-revamped: 0.4.2.dev8
- casambi-bt-hass: 1.9.0.dev8

Dieses Bundle behebt zusaetzlich den Fehler:
TypeError: can't compare offset-naive and offset-aware datetimes

Aenderungen:
1. GATT/Reconnect Hardening aus dev7 bleibt enthalten.
2. Session-Expiry-Vergleich in CasambiBt/_network.py ist jetzt robust fuer naive und timezone-aware UTC datetimes.
3. HA manifest installiert die Library direkt aus deinem GitHub-Repo:
   casambi-bt-revamped@git+https://github.com/drschnalli/casambi-bt-revamped.git@v0.4.2.dev8

GitHub Releases:
- drschnalli/casambi-bt-revamped: Tag v0.4.2.dev8, Title casambi-bt-revamped 0.4.2.dev8
- drschnalli/casambi-bt-hass: Tag v1.9.0.dev8, Title casambi-bt-hass 1.9.0.dev8

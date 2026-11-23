# Wekelijkse aflevering maken

1. Zoek in Gmail: `from:no-reply@somtoday.nl subject:Nieuwsupdate newer_than:8d`. Sla over als het weeknummer al in episodes.json staat.
2. Haal de mailtekst op en download alle PDF-bijlagen; extraheer tekst met `pdftotext -layout`.
3. Schrijf `scripts/<jaar>-wk<NN>.txt`: een Nederlandse luistertekst in dezelfde stijl als `scripts/2026-wk47.txt`:
   - Opening: "Lorentz Lyceum. Nieuwsupdate week ..., verstuurd op ...". Daarna overzicht van onderwerpen, genummerd.
   - Alles uit mail én bijlagen meenemen; tabellen omzetten naar zinnen; getallen, data en tijden voluit schrijven (drieëntwintig november, half twee); e-mailadressen als "info at lorentzlyceum punt n l".
   - Geen namen van leerlingen of leerlingnummers. Niets verzinnen. Tegenstrijdigheden tussen mail en bijlage benoemen.
   - Afsluiten met "Einde van de nieuwsupdate."
4. Voeg een entry toe aan episodes.json (id, title "Nieuwsupdate week NN-JJJJ", date = verzenddatum mail in ISO, summary één regel).
5. `./make_episode.sh <id>` en daarna commit + push naar main.

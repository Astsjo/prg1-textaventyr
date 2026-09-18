## (AI har använts till berättelsen enbart)

Spelaren vaknar upp i ett nedsläckt laboratorium på en rymdstation. Ett larm piper svagt och syrenivån sjunker. Målet är att ta sig till räddningskapseln, men vägen dit beror helt på spelarens val och om de lyckas hitta rätt utrustning.

Struktur & Valträd (Flödesschema)
För att uppgiften ska bli lätt att koda kan du följa den här strukturen i ditt program:

Start (Rum 1: Laboratoriet)
Spelaren ser två dörrar och en upplyst datorterminal.
Val 1A: Undersök datorterminalen → Spelaren hittar ett nyckelkort och går sedan vidare till korridoren.
Val 1B: Gå direkt till dörren mot korridoren → Spelaren har inget nyckelkort.

Mellanstadium (Rum 2: Korridoren)
Vägen blockeras av en trasig elkabel som gnistrar, och bredvid finns en ventilationstrumma.
Val 2A: Försök hoppa över elkabeln → GAME OVER (Spelaren får en stöt).
Val 2B: Kryp genom ventilationstrumman → Spelaren kommer vidare till slussrummet.

Finalen (Rum 3: Räddningskapseln)
Spelaren står framför den låsta räddningskapseln.
Kodkolla (If-sats baserad på tidigare val):
Om has_keycard == True: Kapseln låses upp, spelaren skjuts ut i rymden och överlever! (VINST)
Om has_keycard == False: Dörren är låst, syret tar slut. (GAME OVER)
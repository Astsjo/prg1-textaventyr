## [22/9-26] – ["Sammanfattning"]

**Vad gick fel:**
Jag har inte felsökt eller testat koden än eftersom jag fick tillåtelse att lämna in den ofärdig. Istället kan jag kanske se eller gissa några fel:

1. Möjligtvis med if-satserna

2. Kosmetisk problem

3. Syre-variabeln


**Varför:**
1. Om en användare inte använder den bokstav/ord som förväntas kommer inte if/elif att fungera.
2. Eftersom vi låter användaren välja namn kan de lämna det blankt, alltså " ", en siffra, eller massa bokstäver. Det kan se dåligt ut sedan.

3. Syret var planerat som det alternativa slutet: alltså att syret tar slut och spelaren inte överlever. Men eftersom äventyret inte är färdigt, och inte testat, så kan syret gå in i negativa tal samt kanske inte ens komma i närheten av noll.


**Hur jag löste det:**

1. En enkel lösning är att lägga till en sista "else" ifall inga av de tidigare if/elif fungerade vilket innebär att användaren inte valde något val. Else-satsen kan då säga typ "Var snäll och använd _" och en while-loop startar om den delen av koden så användaren kan göra sitt val igen. Om if/elif fungerar så stänger man av while-loopen. 

2. Man kan säkert göra en enkel if-sats som kollar om "namn == ' ':" och ber användaren att skriva ett namn och en while-loop börjar om den delen. Kan vara svårare med siffror (om man inte kan använda "type" i en if-sats eller kollar om namnet går att byta till int utan att krascha), och om användaren vill heta en massa bokstäver får de helt enkelt bara göra det.

3. Lösningen är igentligen bara att göra färdigt det. Bara att lägga till några "if oxygen >= 0:" här och där, eller efter den punkt man vet att syret kommer att kunna bli lågt. Eller att lägga till några mer "oxygen -= random.int(3, 6)" om inte syret tar slut snabbt nog (eller öka nummren den kan slumpa mellan).


**Vad jag skulle göra annorlunda:**
1. Om man skulle vara lite smart så lägger man in det direkt när man gör den delen så kommer det inte vara ett problem i första början. 

2. Tänka på alla användare och förhindra saker som gör så att spelet ser ut/arbetar annorlunda än förväntat.

3. Inte så mycket att säga om den här.


# *En del av den är kopierad från en tidigare del och ser rörig ut och är inte färdig alls. Tror det börjar vid ca rad 190*
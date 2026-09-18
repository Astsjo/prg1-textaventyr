import time
import random

cont = True
sov = False
oxygen = 100
latmask = True
standing_around = True
keycard_lvl1 = False
keycard_lvl2 = False
keycard_lvl3 = False

print(" ")
usr_name = input("Vad vill du heta: ")

while cont:
    print(" ")
    print(f"{usr_name} blinkar långsamt tillbaka till liv. Du hör någonting som piper, bara för att inse att det är syre-varningen.")
    print(f"Skäppet har {oxygen}% syre kvar.")

    while latmask == True:
        if sov == True:
            print(" ")
            print("Tiden passerar och du blinkar långsamt till liv igen.")
            depletion = random.int(3, 6)
            oxygen -= depletion
            print(f"Det finns nu {oxygen}% syre kvar.")
        print(" ")
        print(f"Vill {usr_name}: ")
        print("(1) Ställa dig upp?")
        print("(2) Ligga kvar en stund till?")
        choice1 = input("Val: ")
        print(" ")

        if choice1 == "2":
            print(f"{usr_name} stänger sina ögon igen...")
            sov = True
        elif choice1 == "1":
            print(f"{usr_name} ställer sig långsamt upp.")
            latmask = False
            sov = False

    while standing_around:
        print("Du står nu i det mörka rummet. Vill du kolla omkring?")
        choice2 = input("[Y/n] ")
        print(" ")
        if choice2.lower() == "n":
            print(f"{usr_name} bestämmer sig att bara stå där och inte kolla omkring.")
            depletion = random.int(3, 6)
            oxygen -= depletion
            print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
        elif choice2.lower != "n":
            standing_around = False
            print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
            print(f"{usr_name} kollar omkring. Du ser en metallisk dörr med någon sorts skannare till sidan om den. Du ser någonting blänka borta i hörnet.")
            depletion = random.int(3, 6)
            oxygen -= depletion
            while keycard_lvl1 == False:
                choice3 = input("Vill du gå och kolla vad föremålet är [Y/n] ")
                if choice3.lower() == "n":
                    print("Du går och kollar på dörren istället. Du försöker bryta upp den men det går inte.")
                    depletion = random.int(3, 6)
                    oxygen -= depletion
                    print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
                elif choice3 != "n":
                    print(f"{usr_name} går och kollar på vad det är som blänker. Det visar sig vara ett kort med siffran 1 på.")
                    keycard_lvl1 = True
                    if keycard_lvl1 == True:
                        print("Du går till dörren och testar ditt nya kort med skannaren du såg. Dörren gnisslar långsamt upp till en korridor.")
    depletion = random.int(3, 6)
    oxygen -= depletion
    print("Du kollar ut genom dörren in i korridoren.")
    choice4 = input("Den leder bara höger och vänster. Vill du gå [H]öger eller [V]änster: ")

    if (choice4.lower() == "h") or (choice4.lower() == "höger"):
        print("Du går till höger och fortätter tills du möter en dörr. Den ser exact ut som förra dörren, så du testar kortet men ingenting händer.")
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
keycard_captain = False
återvända_1 = True
återvända_2 = True
återvända_3 = True
återvända_4 = True
återvända_5 = True

print(" ")
usr_name = input("Vad vill du heta: ")

while cont:
    print(" ")
    print(f"{usr_name} blinkar långsamt tillbaka till liv. Du hör någonting som piper, bara för att inse att det är syre-varningen.")
    print(f"Skäppet har {oxygen}% syre kvar.")
    print(" ")

    while latmask == True:
        if sov == True:
            print(" ")
            print("Tiden passerar och du blinkar långsamt till liv igen.")
            depletion = random.int(3, 6)
            oxygen -= depletion
            print(" ")
            print(f"Det finns nu {oxygen}% syre kvar.")
            print(" ")
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
            print(" ")
            print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
            print(" ")
        elif choice2.lower != "n":
            standing_around = False
            depletion = random.int(3, 6)
            oxygen -= depletion
            print(" ")
            print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
            print(" ")
            print(f"{usr_name} kollar omkring. Du ser en metallisk dörr med någon sorts skannare till sidan om den. Du ser någonting blänka borta i hörnet.")
            while keycard_lvl1 == False:
                choice3 = input("Vill du gå och kolla vad föremålet är [Y/n] ")
                if choice3.lower() == "n":
                    print("Du går och kollar på dörren istället. Du försöker bryta upp den men det går inte.")
                    depletion = random.int(3, 6)
                    oxygen -= depletion
                    print(" ")
                    print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
                    print(" ")
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
        choice4_1 = input("Vill du testa igen [Y/n]: ")
        if choice4_1.lower() != "n":
            print(f"{usr_name} testar att försöka öppna den igen men ingenting händer.")
            depletion = random.int(3, 6)
            oxygen -= depletion
            print(" ")
            print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
            print(" ")
        else:
            print(f"{usr_name} ser ingenting annat och går tillbaka till där de kom från.")
            print(f"{usr_name} har redan testat att gå höger utan någon success, så det går åt vänster istället.")
    print(f"{usr_name} slutar när de möts av en vägg och en dörr till vänster.")
    depletion = random.int(3, 6)
    oxygen -= depletion
    print(" ")
    print(f"Tiden passerar. Det finns nu {oxygen}% syre kvar.")
    print(" ")

    choice4_2 = input("Vill du [K]olla omkring eller gå genom [D]örren: ")
    if (choice4_2.lower() == "k") or (choice4_2.lower() == "kolla"):
        print(f"{usr_name} kollar omkring i korridoren och ser något som blänker igen. De kollar närmare och hittar ett kort liknande objekt igen, den här gången med siffran 2 på och tar upp den.")
        keycard_lvl2 = True

        choice4_2_1 = input("Vill du gå genom [D]örren eller [Å]tervända: ")
        if (choice4_2_1.lower() == "d") or (choice4_2_1.lower() == "dörren"):
            print(f"{usr_name} vänder sig till vänster och försöker öppna dörren utan någon tur. Den metalliska dörren är lite öppen och elektricitet sprakar från den.")
            oxygen -= random.int(3, 6)
            print(" ")
            print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
            print(" ")
            choice4_2_1_1 = input("Vill du [F]örsöka igen eller [Å]tervända: ")
            if (choice4_2_1_1.lower() == "f") or (choice4_2_1_1.lower() == "försöka") or (choice4_2_1_1.lower() == "försöka igen"):
                if keycard_lvl2 == True:
                    print(f"{usr_name} försöker och tar i allt de har tills dörren till slut gnisslar upp. De kliver in och hittar på ett bord ett till kort med siffran 3 på.")
                    keycard_lvl3 = True
                    print(" ")
                    print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                    print(" ")
                else:
                    print(f"{usr_name} försöker och tar i allt de har tills dörren till slut gnisslar upp. De kliver in och hittar på ett kort med siffran 3 ovanpå ett bord.")
                    keycard_lvl3 = True
                    print(" ")
                    print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                    print(" ")
            elif (choice4_2_1_1.lower() == "å") or (choice4_2_1_1.lower() == "återvända"):
                print(f"{usr_name} stoppar ner kortet i fickan och går tillbaka till den andra dörren. De testar med det nya kortet och dörren glider upp.")
                print("Framför dem ser det ut som navigations (kaptens) rummet samt en dörr på vänster sida med en ruta på.")
                oxygen -= random.int(3, 6)
                print(" ")
                print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                print(" ")

                while återvända_5:
                    choice5 = input("Vill du gå till [D]örren, testa [K]ontrollpanelen eller [Å]tervända: ")
                    if (choice5.lower() == "k") or (choice5.lower() == "kontrollpanelen"):
                        print(f"{usr_name} går fram till kaptenens stol vid kontrollpanelen. De testar ett alternativ men inser snabbt att systemet är låst.")
                        print(f"{usr_name} testar kortet men den bara piper till och inget händer.")
                        oxygen -= random.int(3, 6)
                        print(" ")
                        print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                        print(" ")
                    elif (choice5.lower() == "d") or (choice5.lower() == "dörren"):
                        print(f"{usr_name} går fram till dörren och kikar in genom rutan. De ser ett kort utan nummer ligga där blänkandes.")
                        choice5_1 = input("Vill du testa [Ö]ppna dörren eller [Å]tervända: ")
                        if (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 == True)):
                            print(f"{usr_name} testar sitt kort och dörren glider upp. De kliver in och tar upp kortet de såg och återvände sedan tillbaka till navigationsrummet. {usr_name} går till kontrollpanelen och testar det nya korter de hittade och den piper till igen och låser upp. Massa varningar syns, som den låga syrenivån. {usr_name} hittar snabbt knappen för att återställa systemet för syret och ett pys kunde höras från ventilationen.")
                            print(f"Äntligen var {usr_name} säker igen.")
                            print(" ")
                            print("Du klarade av äventyret!")
                        elif (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 != True)):
                            print(f"{usr_name} testar sitt kort men ingenting händer. De återvänder till mitten av rummet.")

        elif (choice4_2_1.lower() == "å") or (choice4_2_1.lower() == "återvända"):
            print(f"{usr_name} stoppar ner kortet i fickan och går tillbaka till den andra dörren. De testar med det nya kortet och dörren glider upp.")
            print("Framför dem ser det ut som navigations (kaptens) rummet samt en dörr på vänster sida med en ruta på.")
            oxygen -= random.int(3, 6)
            print(" ")
            print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
            print(" ")

            choice5 = input("Vill du gå till [D]örren eller testa [K]ontrollpanelen: ")
            if (choice5.lower() == "k") or (choice5.lower() == "kontrollpanelen"):
                print(f"{usr_name} går fram till kaptenens stol vid kontrollpanelen. De testar ett alternativ men inser snabbt att systemet är låst.")
                print(f"{usr_name} testar kortet men den bara piper till och inget händer.")
                oxygen -= random.int(3, 6)
                print(" ")
                print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                print(" ")
            elif (choice5.lower() == "d") or (choice5.lower() == "dörren"):
                print(f"{usr_name} går fram till dörren och kikar in genom rutan. De ser ett kort utan nummer ligga där blänkandes.")
                choice5_1 = input("Vill du testa [Ö]ppna dörren eller [Å]tervända: ")
                if (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 == True)):
                    print(f"{usr_name} testar sitt kort och dörren glider upp. De kliver in och tar upp kortet de såg och återvände sedan tillbaka till navigationsrummet. {usr_name} går till kontrollpanelen och testar det nya korter de hittade och den piper till igen och låser upp. Massa varningar syns, som den låga syrenivån. {usr_name} hittar snabbt knappen för att återställa systemet för syret och ett pys kunde höras från ventilationen.")
                    print(f"Äntligen var {usr_name} säker igen.")
                    print(" ")
                    print("Du klarade av äventyret!")

    elif (choice4_2_1.lower() == "d") or (choice4_2_1.lower() == "dörren"):
        print(f"{usr_name} vänder sig till vänster och försöker öppna dörren utan någon tur. Den metalliska dörren är lite öppen och elektricitet sprakar från den.")
        oxygen -= random.int(3, 6)
        print(" ")
        print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
        print(" ")
        choice4_2_1_1 = input("Vill du [F]örsöka igen eller [Å]tervända: ")
        if (choice4_2_1_1.lower() == "f") or (choice4_2_1_1.lower() == "försöka") or (choice4_2_1_1.lower() == "försöka igen"):
            if keycard_lvl2 == True:
                print(f"{usr_name} försöker och tar i allt de har tills dörren till slut gnisslar upp. De kliver in och hittar på ett bord ett till kort med siffran 3 på.")
                keycard_lvl3 = True
                print(" ")
                print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                print(" ")
            else:
                print(f"{usr_name} försöker och tar i allt de har tills dörren till slut gnisslar upp. De kliver in och hittar på ett kort med siffran 3 ovanpå ett bord.")
                keycard_lvl3 = True
                print(" ")
                print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                print(" ")
                print(f"{usr_name} stoppar ner kortet i fickan och går tillbaka till korridoren.")

            while återvända_5:
                choice5 = input("Vill du gå till [D]örren, testa [K]ontrollpanelen eller [Å]tervända: ")
                if (choice5.lower() == "k") or (choice5.lower() == "kontrollpanelen"):
                    print(f"{usr_name} går fram till kaptenens stol vid kontrollpanelen. De testar ett alternativ men inser snabbt att systemet är låst.")
                    print(f"{usr_name} testar kortet men den bara piper till och inget händer.")
                    oxygen -= random.int(3, 6)
                    print(" ")
                    print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
                    print(" ")
                elif (choice5.lower() == "d") or (choice5.lower() == "dörren"):
                    print(f"{usr_name} går fram till dörren och kikar in genom rutan. De ser ett kort utan nummer ligga där blänkandes.")
                    choice5_1 = input("Vill du testa [Ö]ppna dörren eller [Å]tervända: ")
                    if (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 == True)):
                        print(f"{usr_name} testar sitt kort och dörren glider upp. De kliver in och tar upp kortet de såg och återvände sedan tillbaka till navigationsrummet. {usr_name} går till kontrollpanelen och testar det nya korter de hittade och den piper till igen och låser upp. Massa varningar syns, som den låga syrenivån. {usr_name} hittar snabbt knappen för att återställa systemet för syret och ett pys kunde höras från ventilationen.")
                        print(f"Äntligen var {usr_name} säker igen.")
                        print(" ")
                        print("Du klarade av äventyret!")
                    elif (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 != True)):
                        print(f"{usr_name} testar sitt kort men ingenting händer. De återvänder till mitten av rummet.")

    elif (choice4_2_1.lower() == "å") or (choice4_2_1.lower() == "återvända"):
        print(f"{usr_name} stoppar ner kortet i fickan och går tillbaka till den andra dörren. De testar med det nya kortet och dörren glider upp.")
        print("Framför dem ser det ut som navigations (kaptens) rummet samt en dörr på vänster sida med en ruta på.")
        oxygen -= random.int(3, 6)
        print(" ")
        print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
        print(" ")

        choice5 = input("Vill du gå till [D]örren eller testa [K]ontrollpanelen: ")
        if (choice5.lower() == "k") or (choice5.lower() == "kontrollpanelen"):
            print(f"{usr_name} går fram till kaptenens stol vid kontrollpanelen. De testar ett alternativ men inser snabbt att systemet är låst.")
            print(f"{usr_name} testar kortet men den bara piper till och inget händer.")
            oxygen -= random.int(3, 6)
            print(" ")
            print(f"Tiden går. Det finns nu {oxygen}% syre kvar.")
            print(" ")
        elif (choice5.lower() == "d") or (choice5.lower() == "dörren"):
            print(f"{usr_name} går fram till dörren och kikar in genom rutan. De ser ett kort utan nummer ligga där blänkandes.")
            choice5_1 = input("Vill du testa [Ö]ppna dörren eller [Å]tervända: ")
            if (((choice5_1.lower() == "ö") or (choice5_1.lower() == "öppna")) and (keycard_lvl3 == True)):
                print(f"{usr_name} testar sitt kort och dörren glider upp. De kliver in och tar upp kortet de såg och återvände sedan tillbaka till navigationsrummet. {usr_name} går till kontrollpanelen och testar det nya korter de hittade och den piper till igen och låser upp. Massa varningar syns, som den låga syrenivån. {usr_name} hittar snabbt knappen för att återställa systemet för syret och ett pys kunde höras från ventilationen.")
                print(f"Äntligen var {usr_name} säker igen.")
                print(" ")
                print("Du klarade av äventyret!")
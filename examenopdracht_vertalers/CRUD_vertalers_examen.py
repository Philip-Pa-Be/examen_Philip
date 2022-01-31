import sys
import gegevens
vert_Limb = gegevens.vertalers_limburg
vert_Antw = gegevens.vertalers_Antwerpen


def check_password():
    wachtwoord_encr = "Udymts"
    aantal_mislukte_pogingen = 0
    while aantal_mislukte_pogingen < 3:
        te_controleren_wachtwoord = input("Typ aub het wachtwoord in. Let op, dit is hoofdlettergevoelig!: ")
        ontvangen_wachtwoord_encrypt = encrypt(te_controleren_wachtwoord)
        print(ontvangen_wachtwoord_encrypt)
        if wachtwoord_encr == ontvangen_wachtwoord_encrypt:
            return True
        else:
            aantal_mislukte_pogingen += 1
            if aantal_mislukte_pogingen == 3:
                return False
            print("Wachtwoord is niet correct, probeer het opnieuw!: ")
            continue


def encrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + 5 - 65) % 26 + 65)
        else:
            result += chr((ord(char) + 5 - 97) % 26 + 97)
    return result


def display_menu():
    title = "Uitzendkantoor voor vertalers en tolken".upper()
    print(title)
    print(len(title) * "=", sep="|", end="\n\n")
    print("1     => Limburg")
    print("2     => Antwerpen")
    print("3     => bekijk de samengestelde lijst van beide provincies")
    print("4     => voeg vertaler toe")


def display_commands():
    print("1      => toon alle vertalers in de gekozen provincie")


def toon_alle_vertalers(lijst):
    for item in lijst:
        for k, v in item.items():
            if not type(v) == list:
               print(k, ":", v, end=" ")
        print("\n---------------------------------")
        for x in item["talen"]:
            print(x)
        print()


def toon_beschikbare_vertalers(lijst):
    for item in lijst:
        if item["beschikbaar"] == "ja":
            for k, v in item.items():
                if not type(v) == list:
                    print(k, ":", v, end=" ")
            print("\n---------------------------------")
            for x in item["talen"]:
                    print(x)


def toon_beschikbare_vertalers_gekozen_taal(lijst):
    benodigde_taal = input("Voor welke taal heb je iemand nodig?: ")
    benodigde_taal = benodigde_taal.title()
    for item in lijst:
        if benodigde_taal in item["talen"] and item["beschikbaar"] == "ja":
            for k, v in item.items():
                if not type(v) == list:
                    print(k, ":", v, end=" ")
            print("\n---------------------------------")
            print(item["naam"] + " is beschikbaar en beheerst het " + benodigde_taal)


def voeg_vertaler_toe(lijst, geselecteerde_lijst):
    volledige_naam = input("Typ de volledige naam van de vertaler die je wil toevoegen: ")
    moedertaal = input("Welk is de moedertaal van deze vertaler?: ")
    moedertaal = moedertaal.title()
    if geselecteerde_lijst == "1":
        provincie = "Limburg"
    elif geselecteerde_lijst == "2":
        provincie = "Antwerpen"
    dict_record = {"naam": volledige_naam,
                   "provincie": provincie,
                   "moedertaal": moedertaal,
                   "talen": [],
                   "beschikbaar": ""}
    res_controle_wachtwoord = check_password()
    if res_controle_wachtwoord is True:
        lijst.append(dict_record)
        print(lijst)


def verwijder_vertaler(lijst):
    te_verwijderen = input("Welke vertaler wil je verwijderen?: ")
    te_verwijderen = te_verwijderen.title()
    res_controle_wachtwoord = check_password()
    if res_controle_wachtwoord is True:
        for item in lijst:
            if item["naam"] == te_verwijderen:
                verwijderd = lijst.pop(lijst.index(item))
                print(f"{verwijderd} werd uit de lijst verwijderd!")


def voeg_taal_toe_aan_vertaler(lijst):
    naam = input("Voor welke vertaler wil je een taal toevoegen?: ")
    while True:
        taal = input("Welke taal wil je voor deze persoon toevoegen?: ")
        taal = taal.title()
        if not taal.isalpha():
            print("De taal mag alleen uit letters bestaan. Opnieruw!!!")
            print()
            continue
        else:
            for item in lijst:
                if item["naam"] == naam:
                    item["talen"].append(taal)
                    print(taal + " werd toegevoegd aan de lijst voor " + naam + "!!!")
        break


def reserveer_vertaler(lijst):
    naam = input("Welke vertaler wil je reserveren?: ")
    naam = naam.title()
    for item in lijst:
        if item["naam"] == naam and item["beschikbaar"] == "nee":
            item["beschikbaar"] = "nee"
            print("Je hebt " + naam + " gereserveerd!!!")


def toon_lijst_moedertaal(lijst):
    moedertaal = input("Typ de moedertaal waarop je wil selecteren: ")
    moedertaal = moedertaal.title()
    moedertaalsprekers = []
    for item in lijst:
        if item["moedertaal"] == moedertaal:
            moedertaalsprekers.append(item["naam"])
    moedertaalsprekers.sort()
    print(moedertaalsprekers)


def main():
    res_controle_wachtwoord = check_password()
    if res_controle_wachtwoord is True:
        display_menu()
        while True:
            geselecteerde_lijst = input("Selecteer een lijst door het bijhorende cijfer in te typen: ")
            if geselecteerde_lijst == "1":
                lijst = vert_Limb
                print()
                break
            elif geselecteerde_lijst == "2":
                lijst = vert_Antw
                print()
                break
            elif geselecteerde_lijst == "3":
                pass  # straks nog te definiëren functie aanroepen!!!
            else:
                print("Foutieve invoer, probeer het opnieuw!\n")
        display_commands()
        while True:
            commando = input("Selecteer een commando door het bijhorende cijfer in te typen. Typ \"stop\" om de applicatie te verlaten: ")
            commando = commando.upper()
            if commando == "1":
                toon_alle_vertalers(lijst)
            if commando == "2":
                toon_beschikbare_vertalers(lijst)
            if commando == "3":
                toon_beschikbare_vertalers_gekozen_taal(lijst)
            if commando == "4":
                voeg_vertaler_toe(lijst, geselecteerde_lijst)
            if commando == "5":
                verwijder_vertaler(lijst)
            if commando == "6":
                voeg_taal_toe_aan_vertaler(lijst)
            if commando == "7":
                reserveer_vertaler(lijst)
            if commando == "8":
                toon_lijst_moedertaal(lijst)
            if commando == "STOP":
                continue
                break
        ("Bedankt en tot ziens!!!")

    elif res_controle_wachtwoord is False:
        sys.exit("Je hebt drie keer een fout wachtwoord ingevoerd. De applicatie werd beëindigd!")


if __name__ == "__main__":
    main()

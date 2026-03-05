TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = {
    "bob": "123",
    "ann": "pass123", 
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení
username = input("username: ")
password = input("password: ")

if username not in user or user[username] != password:
    print("unregistered user, terminating the program..")  # Ukončení programu
else:  # Výstup přihlášení
    print(f"""{'-' * 42}
Welcome to the app, {username}
We have {len(TEXTS)} texts to be analyzed.
{'-' * 42}""")
    
    # Vstup: výběr textu
    choice_text = input("Enter a number between 1 and " + 
                        str(len(TEXTS)) + " to select: ")
    
    valid_number = False
    for char in choice_text:
        if not (char.isdigit()):
            print("Letter entered!")  # Zadáno písmeno
            valid_number = False
            break
        else:
            valid_number = True
    else:
        choice = int(choice_text)  # Převod na číslo
        if choice < 1 or choice > len(TEXTS):
            print("Invalid text number!")  # Zadáno číslo mimo rozsah
        else:
            valid_number = True

    if valid_number:
        if 1 <= choice <= len(TEXTS):  # Kontrola rozsahu
            text = TEXTS[choice - 1]
            words = text.split()  # Rozdělení na slova podle mezer

            number_words = len(words)  # Celkový počet slov
            title_words = 0
            uppercase_words = 0  # Slova velkými písmeny
            lower_words = 0
            numbers = []  # Seznam číselných řetězců

            for word in words:  # Průchod všech slov
                if len(word) > 0 and word[0].isupper():
                    # Je první písmeno velké?
                    title_words += 1  # Přičtení k velkým
                if word.isupper():
                    uppercase_words += 1
                if word.islower():
                    lower_words += 1
                if word.isdigit():
                    numbers.append(word)  # Přidání čísla do seznamu
            
            total = 0  # Součet čísel
            for num in numbers:
                total = total + int(num)  # Převod na int a sečtení
            
            # Délka slova
            lengths = {}  # Slovník {délka: počet}
            for word in words:
                clean_word = word  # Kopie slova
                for punctuation in ".,;:?!-(){}\"'":  # Průchod interpunkce
                    clean_word = clean_word.replace(punctuation, "")
                
                length_clean_word = len(clean_word)  # Délka očištěného slova
                if length_clean_word in lengths:  # Pokud délka existuje
                    lengths[length_clean_word] = lengths[length_clean_word] + 1
                    # Přičtení 1 k existující délce
                else:
                    lengths[length_clean_word] = 1  # Nová délka; začíná na 1

               
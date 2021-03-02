s = " 0123.5floz and lol"
chars = set('0123456789g')
letter_g = 'g'
letter_kg = 'kg'
letter_oz = 'oz'
letter_l = 'l'
letter_cl = 'cl'
letter_floz = 'floz'
letter_x = 'x'
letter_komma = ','
letter_punkt = '.'
letter_ml = 'ml'

if letter_kg in s.lower():
    if letter_x in s.lower():
        print("Error: contains(x)")
    elif letter_komma in s.lower():
        print('Error: contains(,)')
    elif letter_punkt in s.lower():
        splitt = (s.lower().split('g', 1)[0])
        splitter_low = splitt.lower()
        kg_int = splitter_low.replace('k', '')
        oP = kg_int.replace('.', '')
        final = int(oP) * 1000
        print(final)
    else:
        splitt = (s.lower().split('g', 1)[0])
        splitter_low = splitt.lower()
        kg_int = splitter_low.replace('k', '')
        final = int(kg_int) * 1000
        print(final)

elif letter_g in s.lower() and letter_kg not in s.lower():
    if letter_x in s.lower():
        print("Error: contains(x)")
    elif letter_komma in s.lower():
        print('Error: contains(,)')
    elif letter_punkt in s.lower():
        splitt = (s.lower().split('g', 1)[0])
        oR = float(splitt) * 1
        final = int(round(oR))
        print(final)
    else:
        splitt = (s.lower().split('g', 1)[0])
        print(splitt)

elif letter_oz in s.lower() and letter_floz not in s.lower():
    if letter_x in s.lower():
        print("Error: contains(x)")
    elif letter_komma in s.lower():
        print('Error: contains(,)')
    elif letter_punkt in s.lower():
        splitt = s.lower().split('o', 1)[0]
        oR = float(splitt) * 28.35
        final = int(round(oR))
        print(final)
    else:
        splitt = s.lower().split('z', 1)[0]
        oO = splitt.lower().replace('o', '')
        oR = int(oO) * 28.35
        final = int(round(oR))
        print(final)

elif letter_floz in s.lower():
    if letter_x in s.lower():
            print("Error: contains(x)")
    else:
        splitt = s.lower().split('f', 1)[0]
        if letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
            oR = float(splitt) * 29.6
            final = int(round(oR))
            print("Final Fl Oz: " + str(final))
        elif letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            oR = float(replace_komma) * 29.6
            final = int(round(oR))
            print("Final Fl Oz: " + str(final))
        else:
            oR = float(splitt) * 29.6
            final = int(round(oR))
            print("Final Fl Oz: " + str(final))


elif letter_cl in s.lower():
    if letter_x in s.lower():
        print("Error: contains(x)")
    else:
        splitt = s.lower().split('l', 1)[0]
        if letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
            remove = splitt.replace('c', '')
            oR = float(remove) * 10
            final = int(round(oR))
            print(final)
        elif letter_komma in splitt.lower():
            remove = splitt.replace('c', '')
            replace_komma = remove.lower().replace(',', '.')
            oR = float(replace_komma) * 10
            final = int(round(oR))
            print(final)
        else:
            oR = float(splitt) * 10
            final = int(round(oR))
            print(final)

elif letter_ml in s.lower():
    splitt = s.lower().split('l', 1)[0]
    if letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
        remove = splitt.replace('m', '')
        oR = float(remove) * 1
        final = int(round(oR))
        print(final)
    elif letter_komma in splitt.lower():
        remove = splitt.replace('m', '')
        replace_komma = remove.lower().replace(',', '.')
        oR = float(replace_komma) * 1
        final = int(round(oR))
        print(final)
    else:
        oR = float(splitt) * 1
        final = int(round(oR))
        print(final)


else:
    if letter_l in s.lower() and letter_ml not in s.lower() and letter_floz not in s.lower():
        if letter_x in s.lower():
            print("Error: contains(x)")
        else:
            splitt = s.lower().split('l', 1)[0]
            if letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
                oR = float(splitt) * 1000
                final = int(round(oR))
                print(final)
            elif letter_komma in splitt.lower():
                replace_komma = splitt.lower().replace(',', '.')
                oR = float(replace_komma) * 1000
                final = int(round(oR))
                print(final)
            else:
                oR = float(splitt) * 1000
                final = int(round(oR))
                print(final)


# print(1.5 * 1000)


""" if any((c in chars) for c in s):
    if any((c in letter_g) for c in s): 
        1 + 1
    else:
        print(s) """

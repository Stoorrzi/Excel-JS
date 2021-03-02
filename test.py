s = " 12 x 0123.5645464 g and lol"
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
    splitt = (s.lower().split('g', 1)[0])
    if letter_x in splitt.lower():
        if letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            vorx = float(replace_komma.split('x', 1)[0])
            nachx = float(replace_komma.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 1))
            print(final)
        else:
            vorx = float(splitt.split('x', 1)[0])
            nachx = float(splitt.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 1))
            print(final) 
    elif letter_komma in splitt.lower():
        replace_komma = float(splitt.lower().replace(',', '.'))
        print(replace_komma)
        rF = float(round(replace_komma))
        final = int(rF)
        print("Final g: " + str(final))
    elif letter_punkt in splitt.lower():
        oR = float(splitt) * 1
        final = int(round(oR))
        print(final)
    else:
        print(splitt)

elif letter_oz in s.lower() and letter_floz not in s.lower():
    splitt = s.lower().split('o', 1)[0]
    if letter_x in splitt.lower():
        if letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            vorx = float(replace_komma.split('x', 1)[0])
            nachx = float(replace_komma.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 28.6))
            print(final)
        else:
            vorx = float(splitt.split('x', 1)[0])
            nachx = float(splitt.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 28.6))
            print(final)    
    elif letter_komma in s.lower():
        replace_komma = splitt.lower().replace(',', '.')
        oR = float(replace_komma) * 28.6
        final = int(round(oR))
        print("Final Oz: " + str(final))
    elif letter_punkt in s.lower():
        oR = float(splitt) * 28.6
        final = int(round(oR))
        print(final)
    else:
        oR = int(splitt) * 28.6
        final = int(round(oR))
        print(final)





elif letter_floz in s.lower():
    splitt = s.lower().split('f', 1)[0]
    if letter_x in splitt.lower():
        if letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            vorx = float(replace_komma.split('x', 1)[0])
            nachx = float(replace_komma.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 29.6))
            print(final)
        else:
            vorx = float(splitt.split('x', 1)[0])
            nachx = float(splitt.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 29.6))
            print(final)
    elif letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
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
    splitt = s.lower().split('c', 1)[0]
    if letter_x in splitt.lower():
        if letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            vorx = float(replace_komma.split('x', 1)[0])
            nachx = float(replace_komma.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 10))
            print(final)
        else:
            vorx = float(splitt.split('x', 1)[0])
            nachx = float(splitt.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 10))
            print(final)
    elif letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
        oR = float(splitt) * 10
        final = int(round(oR))
        print(final)
    elif letter_komma in splitt.lower():
        replace_komma = splitt.lower().replace(',', '.')
        oR = float(replace_komma) * 10
        final = int(round(oR))
        print(final)
    else:
        oR = float(splitt) * 10
        final = int(round(oR))
        print(final)





elif letter_ml in s.lower():
    splitt = s.lower().split('m', 1)[0]
    if letter_x in splitt.lower():
        if letter_komma in splitt.lower():
            replace_komma = splitt.lower().replace(',', '.')
            vorx = float(replace_komma.split('x', 1)[0])
            nachx = float(replace_komma.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 1))
            print(final)
        else:
            vorx = float(splitt.split('x', 1)[0])
            nachx = float(splitt.split('x', 1)[1])
            final_liter = int(vorx * nachx)
            final = int(round(final_liter * 1))
            print(final)
    elif letter_punkt in splitt.lower() and letter_komma not in splitt.lower():
        oR = float(splitt) * 1
        final = int(round(oR))
        print(final)
    elif letter_komma in splitt.lower():
        replace_komma = splitt.lower().replace(',', '.')
        oR = float(replace_komma) * 1
        final = int(round(oR))
        print(final)
    else:
        oR = float(splitt) * 1
        final = int(round(oR))
        print(final)





else:
    if letter_l in s.lower() and letter_ml not in s.lower() and letter_floz not in s.lower():
        splitt = s.lower().split('l', 1)[0]
        if letter_x in s.lower():
            if letter_komma in splitt.lower():
                replace_komma = splitt.lower().replace(',', '.')
                vorx = float(replace_komma.split('x', 1)[0])
                nachx = float(replace_komma.split('x', 1)[1])
                final_liter = int(vorx * nachx)
                final = int(round(final_liter * 1000))
                print(final)
            else:
                vorx = float(splitt.split('x', 1)[0])
                nachx = float(splitt.split('x', 1)[1])
                final_liter = int(vorx * nachx)
                final = int(round(final_liter * 1000))
                print(final)
        else:
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

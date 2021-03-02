strg = '12 x 13'

vor12 = strg.split('x', 1)[0]
nach12 = strg.split('x', 1)[1]

print(int(vor12))
print(int(nach12))

final = int(vor12) * int(nach12)
print(final)
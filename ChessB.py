s = "_abcdefgh"
coord_1 = input()
coord_2 = input()
letter_1 = coord_1[0]
letter_2 = coord_2[0]
column1 = s.find(letter_1)
column2 = s.find(letter_2)
row1 = int(coord_1[1])
row2 = int(coord_1[2])
if (row1 + column1) % 2 == (row2 + column2) % 2:
    print("YES")
else:
    print("NO")

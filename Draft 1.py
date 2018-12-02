def beer_song():
    x = 99
    while x >= 0:
        if x > 2:
            print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
            x -= 1
            print("Take one down, pass it around, " + str(x) + " bottles of beer on the wall.\n")
        elif x == 2:
            print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
            x -= 1
            print("Take one down, pass it around, " + str(x) + " bottle of beer on the wall.\n")
        elif x == 1:
            print(str(x) + " bottle of beer on the wall, " + str(x) + " bottle of beer.")
            x -= 1
            print("Take one down, pass it around. No more bottles of beer on the wall,\n")
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            x += 99
            print("Go to the store and buy some more, " + str(x) + " bottles of beer on the wall.")
            break

print(beer_song())

print("The story begins")
print("----------------")
option_1 = input("(a)in your hometown\n(b)in a far off place\n(a/b):\n")
if option_1 == "a":
    option_1a = input("(a)natural disaster\n(b)a party invite from a distant relative\n(a/b):\n")
    if option_1a == "a":
        option_1aa = input("(a)tries to save himself\n(b)tries to save ther people\n(a/b):\n")
        if option_1aa == "a":
            print("Successfully escapes\n-------------------\nescaped ending")
            input()
        if option_1aa == "b":
            option_1aab = input("(a)saves a group of prople\n(b)saves an abandoned child\n(a/b):\n")
            if option_1aab == "b":
                print("Adopts the child and lives as a father\n -------------------------------------- \nfather ending")
                input()
            if option_1aab == "a":
                print("saves the group\n---------------\nsaviour ending")
                input()
    if option_1a == "b":
        option_1ab = input("(a)dosen't attend the party\n(b)attends the party\n(a/b):\n")
        if option_1ab == "a":
            print("Nothing happens\n---------------\nboring ending")
            input()
        if option_1ab == "b":
            option_1abb = input("(a)gets kidnapped\n(b)has a nice party\n(a/b):\n")
            if option_1abb == "a":
                print("pays a ransom and is let free\n-----------------------------\nransom ending")
                input()
            if option_1abb == "b":
                print("has a nice party\n----------------\nparty ending")
                input()
if option_1 == "b":
    option_1b = input("(a)got bored of life\n(b)got kidnapped by pirates\n(a/b):\n")
    if option_1b == "a":
        option_1ba = input("(a)becomes a skydiver\n(b)becomes a bodybuilder\n(c)kills a random person\n(a/b):\n")
        if option_1ba == "a":
            print("gets married and dies becasue of a skydiving accident\n---------------------------------------------------\nskydiving ending")
            input()
        if option_1ba == "b":
            print("becomes a bodybuilder and a surfer\ngets a lot of money\nspends his life in luxury")
        if option_1ba == "c":
            print("becomes an infamous serial killer\ndies in prison\nserial killer ending")
            input()
    if option_1b == "b":
        option_1bb = input("(a)overpowers the pirates\n(b)makes a deal with the pirates\n(a/b):\n")
        if option_1bb == "a":
            print("dies while trying to fight all the pirates\n----------------------------\nstupid ending")
            input()
        if option_1bb == "b":
            option_1bbb = input("(a)made part of the pirate gang\n(b)left on a remote island\n(a/b):\n")
            if option_1bbb == "a":
                print("lives his life with the pirates\n--------------------------\npirate ending")
                input()
            if option_1bbb == "b":
                print("starves on the island\n-----------------------\nstarvation ending")
                input()
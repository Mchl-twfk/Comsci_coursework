import random as r


def dish_no_gen():
    dishnum = ()
    for i in range(1,7):
        randnum = (r.randint(0,9))
        dishnum.append(randnum)
    print(dishnum)

dish_no_gen()
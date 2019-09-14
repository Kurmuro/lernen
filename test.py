from random import shuffle

Liste = "Super Toller Extremer Harter Cooler Nerviger".upper().split()
shuffle(Liste)
lol = 0


for strophe in range(2):
    for g in range(2):
        for i in range(4):
            print("SPAM", end=' ')
        print()
    print(Liste.pop() +" SPAM", Liste.pop() +" SPAM")
    print()

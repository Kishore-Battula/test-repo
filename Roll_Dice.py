import random

def rolldice():
    """ Roll a six sided die, 6,000,000 times """
    #face frequency conters
    frequencey1=0
    frequencey2=0
    frequencey3=0
    frequencey4=0
    frequencey5=0
    frequencey6=0

    for roll in range(6_000_000):
        face = random.randrange(1,7)

        #increment appropriate face counter

        if face == 1:
            frequencey1 += 1
        elif face == 2:
            frequencey2 += 1
        elif face == 3:
            frequencey3 += 1
        elif face == 4:
            frequencey4 += 1
        elif face == 5:
            frequencey5 += 1
        elif face == 6:
            frequencey6 +=1

    # print the counter accordingly.
    
    print(f'Face{"Frequency":>13}')
    print(f'{1:>4}{frequencey1:>13}')
    print(f'{2:>4}{frequencey2:>13}')
    print(f'{3:>4}{frequencey3:>13}')
    print(f'{4:>4}{frequencey4:>13}')
    print(f'{5:>4}{frequencey5:>13}')
    print(f'{6:>4}{frequencey6:>13}')



rolldice()

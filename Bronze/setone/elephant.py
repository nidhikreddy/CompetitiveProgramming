
inp = int(input())
count = 0
if inp >= 0:
    while inp >= 5:
        inp = inp - 5
        count = count + 1
    if inp == 4: 
        inp = inp - 4
        count = count + 1
        print(count)
        exit
    elif inp == 3:
        inp = inp - 3
        count = count + 1
        print(count)
        exit
    elif inp == 2:
        inp = inp - 2
        count = count + 1
        print(count)
        exit
    elif inp == 1:
        inp = inp - 1
        count = count + 1
        print(count)
        exit 
    else: 
        print(count)
        exit

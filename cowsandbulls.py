import random

def cnb():
    print('welcome to cows and bulls')
    random_num=random.sample(range(1,10),4)
    x=[]
    print(random_num)
    cows=0
    bulls=0

    while x!=random_num:
        x=list(map(int,input('give me a 4 digit number: ')))

        if len(x)!=4:
            print('you should enter 4 digit number!')
            continue
        cows=0
        bulls=0
        for i in range(4):
            for j in range(4):
                if x[i]==random_num[j]:
                    if i==j:
                        bulls+=1
                    else:
                        cows+=1

                    
        print(f'cows:{cows} bulls:{bulls}')
    print('you got it right!!')

cnb()


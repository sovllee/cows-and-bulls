if __name__=="__main__":
    x=int(input('give me a number: '))
    if x==1:
        fib=[1]
    if x==2:
        fib=[1,1]
    if x>2:
        fib=[1,1]
        for i in range(1,x-1):
            fib.append(fib[i]+fib[i-1])
    print(fib)

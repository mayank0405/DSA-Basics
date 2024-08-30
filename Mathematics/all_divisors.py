def divisors(n: int) -> None:
    i = n
    while i > 0:
        if n%i == 0:
            if i == 1:
                print(1)
            print(i, end = ' ')
        i = i - 1

def divisors_2(n: int) ->None:
    i=1 
    while(i*i<=n):
        if(n%i==0):
            print(i)
            if(i!=n/i):
                print(int(n/i))
        i+=1

if __name__ == '__main__':
    num = int(input('Enter num: '))
    divisors_2(num)

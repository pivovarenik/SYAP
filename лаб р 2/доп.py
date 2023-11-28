n=int(input("Введите n: "))
N=1
def fact(n):
    z=1
    while n>=1:
        z=z*n
        n=n-1
    return z

N=fact(n)
print("n!=", N)

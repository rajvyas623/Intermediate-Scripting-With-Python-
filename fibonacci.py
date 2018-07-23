def fibonacci():
    a=0
    b=1
    while True:
        yield(a)
        a,b=b,a+b
        
def callfibo(fibo, number):
    for i in range(number):
        yield next(fibo)

g = callfibo(fibonacci(),10)

[print(i) for i in g]


n = int(input('Introdu numărul n de termeni: '))
init = 0
n1 = 1
fibonacci_legh = []

count = 0
while count < n:
    fibonacci_legh.append(init)
    urmator = init + n1
    init = n1
    n1 = urmator
    count+=1

print('Lista Fibonacci este:', fibonacci_legh)

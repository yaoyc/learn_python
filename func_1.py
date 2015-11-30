'''1*2*3*4...*n'''
def func(n):
    x = 1
    for i in range(1, (n+1)):
	x = x * i
    return x

print func(5)

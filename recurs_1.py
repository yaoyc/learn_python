'''1*2*3....*n'''
def f(N):
    if N == 1:
	return 1
    else:
	return N * f(N-1)

print f(99)

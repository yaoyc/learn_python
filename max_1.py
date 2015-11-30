'''Alist = [a1,a2,...an]'''
aslit = []
def maxlist(aslit):
    a = aslit[0]
    for i in aslit:
	if i > a:
	    a = i 
    return a

print maxlist([1,3,5,7,9])

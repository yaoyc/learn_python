'''Alist = [a1,a2,...an]'''
def maxlist(aslit):
    a = aslit[0]
    for i in aslit:
	if i > a:
	    i = a 
    return a

aslit = [ 1,3,5,7,9]
print maxlist(aslit)

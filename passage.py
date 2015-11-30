'''passage = "I have a Dream,do you have one ?"'''
passage = "I have a Dream, do you have one?"
def count(passage):
    L1 = passage.split()
    D1 = {}
    for i in L1:
        D1[i] = (L1.count(i))
    return D1
print count(passage)

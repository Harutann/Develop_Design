def exercise(a,b):
    return b(a)

print(exercise([54,63,87,86,97],lambda x:sum(x)/len(x)))
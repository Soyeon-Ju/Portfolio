name = ("Soyeon", 1989)
like = [ 'music', 'reading', 'travel']

print(name, like)
print(id(name), id(like))

def Idendify(name, like):
    print(id(name), id(like))
    name=("Soyeon Ju", 1989)
    like[0] = 'computer'
    print(id(name), id(like))
  
Idendify(name, like)

print(name, like)



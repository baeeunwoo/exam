'''
람다 함수



def plus_one(x):
    return x + 1

print(plus_one(1))

plus_two = lambda x : x + 2
print(plus_two(1))
'''
def plus_one(x):
    return x + 1

a = [1, 2, 3]
print(list(map(plus_one, a))) #map(함수, )
print(list(map(lambda x: x + 1, a)))   #위2줄이 lambda x: x + 1 똑같
sort

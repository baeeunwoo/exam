def hello(name):
    print("Hello World!")
    print("Hello %s!\n" % (name))

hello("옥옥")
hello("무녕")


def print_sum(a, b, c):
    print(a + b)
    print(a * b)
    print(a % b)
    print((a + b + c) / 3)

print_sum(500, 600, 1000)

def print_profile(name, age):
     print(name)
     print(age)

my_name = "\n옥옥"
my_age = 28

print_profile(my_name, my_age)
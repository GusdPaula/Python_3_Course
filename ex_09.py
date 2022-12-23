# Exercise with closures

def create_multiplier(n):
    def multiplier(value):
        return n * value
    
    return multiplier

number = create_multiplier(4)

for i in range(2,5,1):
    print(number(i))
   
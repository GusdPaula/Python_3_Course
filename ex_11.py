# Finding the duplicity

list_duplicated = [
                        [1,2,3,4,5,5,9,6,3],
                        [2,1,77,7,5,3,9,11]
                    ]

def find_first_diplicated(list_duplicated):
    check_set = set()
    i = False
    for l in list_duplicated:
        if l in check_set:
            check_set.clear()
            i = False
            break

        # It's not necessary add an else statement in a function, the return and the break will do its job

        check_set.add(l)
        i = True
    
    if i == True:
        return f'We can not find any values duplicated... {-1}'
    
    return f'The value {l} is duplicated'

for l in list_duplicated:
    print(find_first_diplicated(l))

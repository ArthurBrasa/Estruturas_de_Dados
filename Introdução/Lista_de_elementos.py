'''
Lista de elementos
Defina a função remove_duplicatas, que recebe uma
lista e retorna uma nova lista com os mesmos eleme
ntos e na mesma ordem, mas sem valores duplicados.
'''

# def remove_duplicatas(arg):
#     return list(set(arg))


# def remove_duplicatas(arg):
#     new_arg = arg
#     for element in arg:
#         if arg.count(element)>1:
#             new_arg.remove(element)
#             remove_duplicatas(new_arg)       
#     return new_arg


def remove_duplicatas(arg):
    new_arg = []
    verified = []
    for element in arg:
        if arg.count(element)>1:
            if element not in verified:
                new_arg.append(element)
                verified.append(element)
        else:
            new_arg.append(element)      
    return new_arg

print(remove_duplicatas([-1, 'a', 'a', 0, 'b', 1, 1, 2, 2, 3, 3]))


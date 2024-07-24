def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(2, 4)
print_params(False, 2, 'Anime')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = (1, False, 'Manga')
values_dict = {'a': 2, 'b': True, 'c': 'Movie'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [14.22, 'String']
print_params(*values_list_2, 42)
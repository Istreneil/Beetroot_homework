from math import pi as p
int_p=int(p) #можливо неправильно зрозуміла умову "ціле числе p"

def pow_p(int_number, return_type = 'int'):
    if type(int_number) is float: #так само тут, може не варто було флоат змінювати в інт, а просто не пропускати таке число
        int_number=int(int_number)
        return pow(int_number, int_p)
    elif type(int_number) is not int:
        return
    else:
        return pow(int_number, int_p)

def pow_p_numbers(int_numbers_list, return_type = 'list'):
    if type(int_numbers_list) is not list:
        return
    else:
        return [pow_p(n) for n in int_numbers_list]



list1 = [1,3,5]
list2 = [2,4,6,8,12,89]
list3 = (2,5,6)
list4 = [2.14, 3.8, 9.356]


print(pow_p_numbers(list1))
print(pow_p_numbers(list2, 'dict'))
print(pow_p_numbers(list3, 'list'))
print(pow_p_numbers(list4, 'list'))
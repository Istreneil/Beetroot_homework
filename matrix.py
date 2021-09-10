from math import pi as p

def transpose(initial):
    transposed=[]
    for row in range(3):
        transposed.append([])
        for column in range(3):
            transposed[row].append(None)

    for row in range(3):
        for column in range(3):
            transposed[column][row] = initial[row][column]
    return transposed

transposed_matrix = transpose(matrix)


def circle(rad):
    return p*pow(rad,2)

def circles_from_list(rads_list, return_type):
    if type(rads_list) is not list:
        return
    if return_type.lower() == 'dict':
        circle_dict = {}
        for r in rads_list:
            circle_dict[r]=circle(r)
        return circle_dict
    else:
        return [circle(r) for r in rads_list]

rads1 = [1,3,5]
rads2 = [2,4,6,8]
print(circles_from_list(rads2, 'dict'))

print()

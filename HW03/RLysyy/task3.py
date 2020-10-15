var_1 = 14
var_2 = 88

print(f'variable before: {var_1} {var_2}')

var_1 = [var_1, var_2]
var_2 = var_1[0]
var_1 = var_1[1]

print(f'variable after: {var_1} {var_2}')
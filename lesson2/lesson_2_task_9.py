def swap(var_1, var_2):
	return var_2, var_1
var_1 = 37
var_2 = 99
print("var_1:", var_1)
print("var_2:", var_2)
var_1, var_2 = swap(var_1, var_2)
print("var_1:", var_1)
print("var_2:", var_2)
def  reverse_list(lst):
    reversed_lst = lst[::-1]
    return reversed_lst


my_list = [1,2,3,4,5,6,7,8,9,10]
reversed_list = reverse_list(my_list)
print("original list:", my_list)
print("reversed list:", reversed_list)

#
def  double_values(lst):
     doubled_lst = []
     for value in lst:
         doubled_lst .append(value * 2 )
     return doubled_lst


my_list = [1,2,3,4,5,6,7,8,9,10]
doubled_list = double_values(my_list)
print("original list:", my_list)
print("doubled list:", doubled_list)


#
def   sum_of_list(numbers):
     total = 0
     for number in numbers:
         total += number
     return total


my_list = [1,2,3,4,5,6,7,8,9,10]
result = sum_of_list(my_list)
print("original list:", my_list)
print("sum_of_list:", result)

#
def even_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
for x in range(1,5):
    user_input = int(input(f"write your {x} number"))
    print(even_odd(user_input))
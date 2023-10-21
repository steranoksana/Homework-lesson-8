# def my_pow(number, degree):
#     if degree <= 1:
#         return number
#
#     return number * my_pow(number, degree - 1)
#
# print(my_pow(3, 3))
# # my_pow(3, 3) => 3 * my_pow(3,2) => 27
# # my_pow(3, 2) => 3 * my_pow(3,1) => 9
# # my_pow(3, 1) => 3

def sum_range(a, b):

    if a > b:

        return 0

    return a + sum_range(a+1, b)



print(sum_range(2, 5))

# sum_range(2, 5) => 2 + 3  => 5
# sum_range(2, 5) => 4+ 5 => 9

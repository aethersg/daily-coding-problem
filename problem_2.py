'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
'''


def get_factors(input_list):
    cumulative = 1
    right_prod_list = list()
    for num in input_list:
        cumulative *= num
        right_prod_list.append(cumulative)

    cumulative = 1
    left_prod_list = list()
    for num in input_list[::-1]:
        cumulative *= num
        left_prod_list.append(cumulative)
    left_prod_list = left_prod_list[::-1]

    output_list = list()
    for i in range(len(input_list)):
        num = None
        if i == 0:
            num = left_prod_list[i + 1]
        elif i == len(input_list) - 1:
            num = right_prod_list[i - 1]
        else:
            num = right_prod_list[i - 1] * left_prod_list[i + 1]
        output_list.append(num)

    return output_list


assert get_factors([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert get_factors([3, 2, 1]) == [2, 3, 6]

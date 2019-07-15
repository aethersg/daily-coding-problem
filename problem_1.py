'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''


def check(list_num, result):
    # create a set to store the possible solutions
    possible_solutions = set()
    # go through the list which is given.
    for num in list_num:
        # if the number appears in the set it means it is a possible solution
        if num in possible_solutions:
            return True
        # from the number we are checking we will make the new possible solution.
        possible_solutions.add(result - num)
    # if there is nothing after going through the list we will return false as it is not possible to make the sum.
    return False


assert not check([], 17)
assert check([10, 15, 3, 7], 17)
assert not check([10, 15, 3, 4], 17)
assert check([10, 15, 3, 8, 9, 9], 18)

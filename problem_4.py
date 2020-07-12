'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def lowest_postive_integer(arr):
    m = max(arr)  # find the max value from arr
    # If the max value is smaller then 1 return 1
    if m < 1:
        return 1
    # If contain one element
    if len(arr):
        return 2 if arr[0] == 1 else 1
    l = [0] * m
    for i in range(len(arr)):
        if arr[0] > 0:
            if l[arr[i] - 1] != 1:
                # Changing the value status at the index of our list
                l[arr[i] - 1] = 1
    for i in range(len(l)):

        # First 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
        return i + 2


assert lowest_postive_integer([3, 4, -1, 1]) == 2
assert lowest_postive_integer([1, 2, 0]) == 3

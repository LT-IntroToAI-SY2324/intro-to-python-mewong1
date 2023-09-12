"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


# def absolute(n: int) -> int:
#     """Gives the absolute value of the passed in number. Cannot use the built in
#     function `abs`.

#     Args:
#         n - the number to take the absolute value of

#     Returns:
#         the absolute value of the passed in number
#     """
#     if (n>0):
#         return (n)
#     else:
#         return (n*-2 + n)
#     raise NotImplementedError("absolute")

# print (absolute(-2349))

# def factorial(n: int) -> int:

#     """Takes a number n, and computes the factorial n! You can assume the passed in
#     number will be positive

#     Args:
#         n - the number to compute factorial of

#     Returns:
#         factorial of the passed in number
#     """
#     raise NotImplementedError("factorial")
#     i = n + 1
#     for x in range (1, n):
#         n = n*x
#     return n
# print(factorial(7))


# T = TypeVar("T")

# def every_other(lst: List[T]) -> List[T]:
#     for var in range(len(lst)):
#         print(var)

#     return T
# """Takes a list and returns a list of every other element in the list, starting with
#     the first.

#     Args:
#         lst - a list of any (constrained by type T to be the same type as the returned
#             list)

#     Returns:
#         a list of every of other item in the original list starting with the first
#     """
#     raise NotImplementedError("every_other")


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 34, 100]
# def sum_list(lst: List[int]) -> int:  
#     sum1 = 0
#     for r in range(0, len(lst),2):
#         sum1 += r
#     return sum1

# print(sum_list(lst))


# def sum_list(lst: List[int]) -> int:  
#     sum1 = 0
#     for r in range(len(lst)):
#          sum1 += r
#     return sum1

# print(sum_list(lst))

#     """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
#     use the built in function `sum`.

#     Args:
#         lst - a list of numbers

#     Returns:
#         the sum of the passed in list
#     """
#     raise NotImplementedError("sum_list")


# def mean(lst: List[int]) -> float:
#     sum1 = 0
#     count = 0
#     for r in range(len(lst)):
#         sum1 += r
#         count += 1
#     return sum1/count

# print(mean(lst))

#     """Takes a list of numbers, and returns the mean of the numbers.

#     Args:
#         lst - a list of numbers

#     Returns:
#         the mean of the passed in list
#     """
#     raise NotImplementedError("mean")


# def median(lst: List[int]) -> float:
#     count = len(lst)
#     if count%2 == 1:
#          return lst[int(count/2)]
#     else:
#          return (lst[int(count/2)] + lst[int((count-1)/2)]) /2.0

# print (median(lst))
#     """Takes an ordered list of numbers, and returns the median of the numbers.

#     If the list has an even number of values, it computes the mean of the two center
#     values.

#     Args:
#         lst - an ordered list of numbers

#     Returns:
#         the median of the passed in list
#     """
#     raise NotImplementedError("median")

lst_names= ["megan", "jane", "nina", "youin", "berg"]
def duck_duck_goose(lst: List[str]) -> List[str]:
    indx = 0
    while len(lst)>2:
        indx = (indx+2) % len(lst)
        removed = lst.pop(indx)
        print(removed + " is removed")

    return lst_names

print(duck_duck_goose(lst_names))
#     """Given an list of names (strings), play 'duck duck goose' with it, knocking out
#     every third name (wrapping around) until only two names are left.

#     In other words, when you hit the end of the list, wrap around and keep counting from
#     where you were.

#     For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
#     knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
#     'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

#     You may assume the list has 3+ names to start

#     Args:
#         lst - a list of names (strings)

#     Returns:
#         the resulting list after playing duck duck goose
#     """
#     raise NotImplementedError("duck_duck_goose")


# # this line causes the nested code to be skipped if the file is imported instead of run
# if __name__ == "__main__":
#     assert absolute(-1) == 1, "absolute of -1 failed"
#     assert factorial(4) == 24, "factorial of 4 failed"
#     assert every_other([1, 2, 3, 4, 5]) == [
#         1,
#         3,
#         5,
#     ], "every_other of [1,2,3,4,5] failed"
#     assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
#     assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
#     assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

#     names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
#     assert duck_duck_goose(names) == ["roscoe", "law"]

#     print("All tests passed!")
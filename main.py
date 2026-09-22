# Programmer: Stephen Borch
# Class: CPSC 222, Fall 2026
# Data Assignment #1
# 9/20/26
# I attempted the bonus
# Description: This program computes the count, mean, median, smallest number, 
# and largest number for the given list of values from the 2024 Gonzaga Men's
# Basketball Points per game. Replaces all the values in the list that are 
# at and in between user inputted start and stop values. Creates a function 
# that reverses a given list and puts a tilde between each value.

import math

ppg_list = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]

# Sorts the list in reverse order and prints the list
ppg_list.sort(reverse = True)
print("2024 Gonzaga Men's Basketball Points per game:", ppg_list)

# Prints the amount of values in the list
print(f"Count of the numbers: {len(ppg_list):.2f}")

# Computes and prints the average of the values in the list
ppg_avg = sum(ppg_list) / len(ppg_list)
print(f"Average of the numbers: {ppg_avg:.2f}")

# Computes and prints the median value in the list
ppg_median = ppg_list[int(len(ppg_list) / 2)]
print(f"Median number: {ppg_median:.2f}")

# Prints the smallest and largest values in the list
print(f"Smallest Number: {ppg_list[-1]:.2f}")
print(f"Largest Number: {ppg_list[0]:.2f}")

print("Enter a starting value:")
start = float(input())

print("Enter an ending value:")
end = float(input())

# Modifies the original list to put zeros at and between the start
# and stop values specified by the user
for i in range(len(ppg_list)):
    if start <= i <= end:
        ppg_list[i] = 0

print("New List with zeros at and in between the specified values:", ppg_list)

def print_reverse_bonus(alist):
    """
    Takes a list and reverses the order of the values in 
    the given list and puts a tilde in between each value

    Args:
    any list to be reversed, in this case it accepts an example list, bonus_list

    Returns: 
    the new reversed list

    (e.g.): [1, 2, 3] becomes [3 ~ 2 ~ 1]
    """
    reverse_alist = []

# Reverses the given list without using the built-in reverse function
    for i in range(len(alist) - 1, -1, -1):
        reverse_alist.append(alist[i])

# Puts a tilde (~) between each value instead of a comma
    string_alist = [str(i) for i in reverse_alist]
    tilde_alist = " ~ ".join(string_alist)

    return tilde_alist

# Example of a list to make use of the above function
bonus_list = [1, 2, 3]
print("Reversed List Example:", print_reverse_bonus(bonus_list))
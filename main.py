import math

ppg_list = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]

ppg_list.sort(reverse = True)
print("2024 Gonzaga Men's Basketball Points per game:", ppg_list)

print(f"Count of the numbers: {len(ppg_list):.2f}")

ppg_avg = sum(ppg_list) / len(ppg_list)
print(f"Average of the numbers: {ppg_avg:.2f}")

ppg_median = ppg_list[int(len(ppg_list) / 2)]
print(f"Median number: {ppg_median:.2f}")

print(f"Smallest Number: {ppg_list[-1]:.2f}")
print(f"Largest Number: {ppg_list[0]:.2f}")

print("Enter a starting value:")
start = float(input())

print("Enter an ending value:")
end = float(input())

for i in range(len(ppg_list)):
    if start <= i <= end:
        ppg_list[i] = 0

print("New List:", ppg_list)

def print_reverse_bonus(alist):
    """
    takes a list and reverses the order of the values in 
    the given list and puts a tilde in between each value

    returns the new reversed list

    (e.g.): [1, 2, 3] becomes [3 ~ 2 ~ 1]
    """
    reverse_alist = []

    for i in range(len(alist) - 1, -1, -1):
        reverse_alist.append(alist[i])

    string_alist = [str(i) for i in reverse_alist]
    tilde_alist = " ~ ".join(string_alist)

    return tilde_alist

bonus_list = [1, 2, 3]
print("Reversed List Example:", print_reverse_bonus(bonus_list))
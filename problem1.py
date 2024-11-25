# Problem 1 : "Daily Steps Tracker"

# Description:
# You have a list of the number of steps taken each day in a month. Your task is to write a program that performs the following:
# Accepts the number of steps taken each day in the month as numbers separated by spaces.
# Calculates the highest and lowest step counts.
# Calculates the average daily step count.
# Sorts the step counts in descending order.

steps_input = input("Enter the  number of steps taken each day in a month")
steps = list(map(int, steps_input.split()))

heighest_steps = max(steps)

lowest_steps = min(steps)

average_steps = sum(steps)/len(steps)

sort_steps = sorted(steps , reverse = True)

print("Heighest steps = " ,heighest_steps )
print("lowest steps = "   ,  lowest_steps )
print("Average_steps = "  , average_steps )
print("sort steps = "     ,     sort_steps)

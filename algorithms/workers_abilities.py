"""
Algorithms that receive as input a list of workers' activity capacity
per day (list of integers), and the number of activities needed to be
done (integer). Each time a worker performs the number of activies for
a day, his capacity decreases to the floor of the current capacity
divided by 2. So for example if the capacity is initially 6, after
working for one day, the capacity will decrease to 3, and the next
time to 1, until it reaches 0. Only one worker can be called per day.
The output of the algorithm returns the number of days needed to
perform the activities number (the second input parameter), or -1 if
the number of activities cannot be performed by the workers (all have
reached capacity of 0 activities).
"""


def calculate_minimum_days(workers_capacity, activities):
    days = 0

    while activities > 0 and workers_capacity:
        workers_capacity.sort(reverse=True)
        greatest_activites_capacity = workers_capacity[0]
        activities -= greatest_activites_capacity
        workers_capacity[0] = greatest_activites_capacity // 2
        if not workers_capacity[0]:
            workers_capacity.pop(0)
        days += 1

    if activities > 0:
        return -1
    return days


def calculate_minimum_days_optimized(workers_capacity, activities):
    days = 0
    x = y = z = 0
    workers_capacity.sort(reverse=True)
    workers_capacity_length = len(workers_capacity)

    while activities > 0 and workers_capacity:
        if y > 1 and x < workers_capacity_length - 2 and \
                workers_capacity[x] < workers_capacity[x + 1]:
            x += 1
        if x > 1 and workers_capacity[x] < workers_capacity[0]:
            x, y, z = 0, 0, 0
        if y < workers_capacity_length - 2 and \
                workers_capacity[y] < workers_capacity[y + 1]:
            y += 1
        if workers_capacity[z] < workers_capacity[y]:
            z = y
        if workers_capacity[z] < workers_capacity[x]:
            workers_capacity.sort(reverse=True)
            x = y = z = 0
            continue

        activities -= workers_capacity[z]
        workers_capacity[z] //= 2

        if not workers_capacity[z]:
            workers_capacity.pop(z)
            workers_capacity_length -= 1

            if y >= workers_capacity_length - 1:
                y -= 1
                z -= 1
            if x >= workers_capacity_length - 1:
                x -= 1

        days += 1

    if activities > 0:
        return -1
    return days

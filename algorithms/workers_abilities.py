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
import heapq


def calculate_minimum_days(workers_capacity, activities):
    """This function uses heapq module to create a priority queue in
    order to make it faster to pop the greatest values and also to
    push changed activities values but keeping them in order. Since
    the heapq module only works as a min heap, the idea here is to
    create a hack or workaround to turn positive numbers into negative
    ones, in order to keep the greatest values as the first to be
    popped out. Just after being popped out, the value it is turned
    into a positive integer, and it is turned back into a negative one
    just before being pushed in.
    """
    days = 0

    for i, capacity in enumerate(workers_capacity):
        workers_capacity[i] = -capacity

    heapq.heapify(workers_capacity)

    while activities > 0 and workers_capacity:
        greatest_activities_capacity = -(heapq.heappop(workers_capacity))
        activities -= greatest_activities_capacity
        heapq.heappush(workers_capacity, -(greatest_activities_capacity // 2))
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

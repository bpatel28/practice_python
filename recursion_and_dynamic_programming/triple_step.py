"""
A child is running up a staircase with n steps and can hope either 1 step, 2 step or 3 steps at a time.Implement a
method to count how many possible ways the child can run up the stairs.
"""


def count_ways(steps):
    if steps == 0:
        return 0
    memo = [-1 for i in range(steps + 1)]
    return _count_ways(steps, memo)


def _count_ways(steps, memo):
    if steps == 0:
        memo[0] = 0
        return 0
    elif steps == 1:
        memo[0] = 1
        return 1
    elif steps == 2:
        memo[1] = 2
        return 2
    elif steps == 3:
        memo[2] = 4
        return 4
    elif memo[steps] > -1:
        return memo[steps]
    else:
        return _count_ways(steps - 1, memo) + _count_ways(steps - 2, memo) + _count_ways(steps - 3, memo)


print(count_ways(0))
print(count_ways(1))
print(count_ways(2))
print(count_ways(3))
print(count_ways(20))

import random


def solution(A):
    # delete 'pass' and fill in your code
    pass


######## Test Cases
example = [23171, 21011, 21123, 21366, 21013, 21367]
v_pattern = [40, 30, 20, 10, 20, 30, 40]
simple_desc = [50, 40, 30, 20, 10]
simple_asc = [10, 20, 30, 40, 50]
empty = []
simple = [0, 200000]
two_hills = [30, 20, 22, 24, 26, 28, 20, 10, 0, 2, 4, 7]
max_profit_after_max_and_before_min = [25, 30, 100, 30, 40, 0, 5]
medium_1 = [99, 1, 2, 3, 4, 5] * 100
large_1 = [99, 1, 2, 3, 4, 5, 6] * 10000
first, second = [i for i in range(100000, 120000)], [i for i in range(100000)]
large_2 = [random.sample(first, k=1)[0] for i in range(200000)] + [random.sample(second, k=1)[0] for i in range(200000)]
third = [i for i in range(200000)]
large_3 = [random.sample(third, k=1)[0] for i in range(200000)]


######## Runs and Expected Output
print(solution(example))  # 356
print(solution(v_pattern))  # 30
print(solution(simple_desc))  # 0
print(solution(simple_asc))  # 40
print(solution(empty))  # 0
print(solution(simple))  # 200000
print(solution(two_hills))  # 8
print(solution(max_profit_after_max_and_before_min))  # 75
print(solution(medium_1))  # 98
print(solution(large_1))  # 98
print(solution(large_2))  # random but should be close to 100,000
print(solution(large_3))  # random but should be close to 200,000

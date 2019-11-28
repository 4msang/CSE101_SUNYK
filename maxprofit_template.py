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

test_cases = [example, v_pattern, simple_desc, simple_asc, empty, simple, two_hills,
              max_profit_after_max_and_before_min, medium_1, large_1, large_2, large_3]


######## Runs
for test_case in test_cases:
    try:
        print(solution(test_case))
    except:
        print("Your codes produced a run-time error for this test.")


######## Expected Output
"""
356
30
0
40
0
200000
8
75
98
98
random but should be close to 100,000
random but should be close to 200,000
"""

from lib import count_identities

test_data = [
    (([1, 2, 3], [2, 3, 4], [0, 2, 3]), 2),
    (([5, 6, 7], [7, 8], [7, 9, 7]), 1),
    (([1, 2], [3, 4]), 0),
    (([], [1, 2], [2, 3]), 0),
    (([1, 1, 2], [1, 2, 2], [1, 2]), 2)
]

for input, expected in test_data:
    result = count_identities(*input)
    print(f'{input} : {result} :: {expected == result}')

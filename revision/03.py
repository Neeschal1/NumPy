import numpy as np

main_arr = np.array(
    [
        [
            [
                ["A", "B", "C"],
                ["D", "E", "F"],
            ],
            [
                ["G", "H", "I"],
                ["J", "K", "L"],
            ],
        ],
        [
            [
                ["M", "N", "O"],
                ["P", "Q", "R"],
            ],
            [
                ["S", "T", "U"],
                ["V", "W", "X"],
            ],
        ],
        [
            [
                ["Y", "Z", " "],
                [" ", " ", " "],
            ],
            [
                [" ", " ", " "],
                [" ", " ", " "],
            ],
        ],
    ]
)


word = (
    main_arr[0, 0, 1, 2]
    + main_arr[1, 1, 0, 2]
    + main_arr[0, 0, 0, 2]
    + main_arr[0, 1, 1, 1]
    + main_arr[2, 0, 1, 0]
    + main_arr[1, 1, 0, 2]
)

print(word, main_arr.ndim)

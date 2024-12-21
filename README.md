# 3D Sudoku Solver

## Overview
It doesn't work for complesx ones, working on it tho

---

## Input Example
```python
mainMatrix = [[[[0,8,2],
                [0,0,1],
                [6,0,3]],[[0,0,0],
                          [4,0,6],
                          [0,1,8]],[[1,0,6],
                                    [8,0,2],
                                    [7,0,0]]],[[
            [9,4,0],
            [0,0,6],
            [0,0,0]],[[8,0,7],
                      [5,0,1],
                      [0,4,0]],[[6,0,0],
                                [0,0,0],
                                [2,5,7]]],[[
            [0,1,0],
            [3,6,0],
            [0,0,9]],[[9,0,0],
                      [0,8,0],
                      [3,0,4]],[[0,7,0],
                                [4,2,0],
                                [5,0,0]
        ]
    ]
]
```

---

## Output Example
```python
[[[[4, 8, 2], 
  [7, 5, 1], 
  [6, 9, 3]], [[7, 5, 3], 
                [4, 9, 6], 
                [2, 1, 8]], [[1, 9, 6], 
                            [8, 3, 2], 
                            [7, 4, 5]]], 
 [[[9, 4, 5], 
  [2, 7, 6], 
  [1, 3, 8]], [[8, 2, 7], 
                [5, 3, 1], 
                [6, 4, 9]], [[6, 1, 3], 
                            [9, 8, 4], 
                            [2, 5, 7]]], 
 [[[5, 1, 4], 
  [3, 6, 7], 
  [8, 2, 9]], [[9, 6, 2], 
                [1, 8, 5], 
                [3, 7, 4]], [[3, 7, 8], 
                            [4, 2, 9], 
                            [5, 6, 1]]]]
```

---

## Running the Code
1. Save the code in a Python file (e.g., `sudoku_solver.py`).
2. Execute the file:
```bash
python sudoku_solver.py
```

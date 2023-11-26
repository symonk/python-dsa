[![codecov](https://codecov.io/gh/symonk/python-dsa/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/python-dsa)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/python-dsa/)

# python-dsa
:snake: Data structures and Algorithms in python

-----

![Cheatsheet](.github/images/bigO.png)


-----

# Constant Complexity [O(1)]

-----

Where the algorithm time remains the same, regardless of the input size growing.

```python
# O(1) constant time
x = [1,2,3]
assert x[0] == 1
```

-----

# Linear Complexity [O(n)]

-----
Linear complexity is when the time/space of the algorithm grows in line with the size 
of the input, for example: A bigger array takes longer than a smaller one to traverse.

```python
numbers = list(range(10_000))
for n in numbers:
    # We have to iterate every element in numbers; O(n) depending on numbers size.
    _ = n * 2
```

-----

# Logarithmic Time [O(log n)]

-----

...

-----

# Polynomial Time [O(n²)]

-----

...

-----

# Exponential Time [O(n^²)]

-----

...

-----

###  Combinations

-----

Unlike `permutations`, intricate details of the group do not matter as much.

```python
from itertools import combinations
x = (1,2,3)
for combo in itertools.combinations(x, len(x)):
    print(combo)

# (1,2,3)
```

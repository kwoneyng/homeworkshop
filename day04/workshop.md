1.

```python
def mk_sqrt(x):
    a = int(x)
    i = 1
    while a > i ** 2:
        i += 1
    b = i - 1
    c = i
    for j in range(20):
        if a < ((b+c)/2)**2 :
            c = (b+c)/2
        elif a > ((b+c)/2)**2:
            b = (b+c)/2
    return max(b, c)
```


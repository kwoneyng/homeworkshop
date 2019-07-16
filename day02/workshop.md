1

```python
n = 5
m = 9
for i in range(m):
    result = ''
    for j in range(n):
        result = result + '*'
    print(result)
```



2.

```python
student = {'python':80, 'algorithm':99, 'django':89, 'flask':83,}
a = list(student.values())
print(sum(a)/len(a))
```



3.

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
a = {}
for i in blood_types:
    su = 0
    for j in range(len(blood_types)):
        if blood_types[j] == i:
            su += 1
    a.update({i:su})
print(a)
```


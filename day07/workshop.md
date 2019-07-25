1.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')
```



2.

```python
class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
```


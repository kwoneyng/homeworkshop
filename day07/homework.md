1.

```python
class Calculator:
	count = 0
    
    def info(self):  # 인스턴스 메서드
        print('나는 계산기입니다.')
    
    @staticmethod
    def add(a,b):  #스태틱 메서드
        Calculator.count += 1
        print(f'{a} + {b}는 {a + b} 입니다.')
        
    @classmethod
    def history(cls):  #클래스 메서드
        print(f'총 {cls.count}번 계산했습니다.')
```





2.

```
ct = Calculator()
ct.info()
ct.add(1,3)
Calculator.history()
```



3.

```python
self 는 인스턴스가 할당되고 cls 는 클래스가 할당된다.
```


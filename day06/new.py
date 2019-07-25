class Mylist:

    stack = []
    def empty(self):
        # if len(self.stack) == 0 :
        #     return True
        # else : 
        #     return False
        return not bool(self.stack)
    
    def top(self):
        # if len(self.stack) == 0 :
        #     return None
        # else :
        #     return self.stack[-1]
        if not self.empty():
            return self.stack[-1]

    
    def pop(self) :
        if len(self.stack) == 0 :
            return None
        else :
            target = self.stack[-1]
            del self.stack[-1]
            return target
    

    def push(self,x) :
        self.stack += [x]

    def __repr__(self):
        return f'내 스택에는 {self.stack}이 담겨있다.'

ml1 = Mylist()
print(ml1.empty())
ml1.push('강아지')
print(ml1.empty())
print(ml1.top())
abc = ml1
print(abc)
ml1.push('고양이')
print(ml1.pop())
print(ml1.pop())
ml1
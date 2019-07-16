#https://leetcode.com/problems/remove-outermost-parentheses/

class Stack:
    def __init__(self):
        '''Stack()创建一个新的空栈。不需要参数，并返回一个空栈'''
        self.items = []      

    def push(self, item):
        '''Push(item)将新项添加到堆栈的顶部。它需要参数 item 并且没有返回值'''
        self.items.append(item)

    def pop(self):
        '''pop()从栈顶删除项目。它不需要参数,返回 item。栈被修改'''
        return self.items.pop()

    def peek(self):
        """返回栈顶的项，不删除它。它不需要参数。堆栈不被修改。"""
        return self.items[-1]

    def isEmpty(self):
        """测试看栈是否为空。它不需要参数，返回一个布尔值。"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        """返回栈的项目数。它不需要参数，返回一个整数。"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)




def removeOuterParentheses(S: str) -> str:
    answer = ""

    num = 0
    strs = ""

    for i in S:
        if num > 0:
            if i == "(":
                num += 1
                strs += i
            else:
                num -= 1
                if num > 0:
                    strs += i
                else:
                    answer += strs
                    strs = ""

        else:
            if i == "(":
                num += 1
                strs = ""

    return answer

a = "(()())(())"
b = "(()())(())(()(()))"
c = "()()"

print(removeOuterParentheses( a))
print(removeOuterParentheses( b))
print(removeOuterParentheses(c))

def removeOuterParenthesesStack(S: str) -> str:
    answer = ""
    stack = Stack()
    for i in S:
        if stack.size != 0:
            if i == "(":
                stack.push("(")
            else:
                
        
        else:
            stack.push("(")
            
        

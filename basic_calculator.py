class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        res = 0
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in ['+', '-']:
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # previous result
        return res + sign * num

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        base = 48
        res = 0 
        for n1_10,n1 in enumerate(reversed(num1)): 
            for n2_10,n2 in enumerate(reversed(num2)): 
                number1 = ord(n1)-base
                number2 = ord(n2)-base
                res += number1*number2*(10**(n1_10+n2_10))
        return str(res)
                
        
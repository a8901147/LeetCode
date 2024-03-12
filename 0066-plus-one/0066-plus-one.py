class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i]=0
                carry = 1
            else:
                carry = 0
        return [1]+digits if carry else digits
                
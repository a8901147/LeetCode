class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False

        def gcd(a,b):
            while b != 0:
                temp = b
                b = a%b
                a = temp
            return a
        
        return targetCapacity%gcd(jug1Capacity,jug2Capacity)==0
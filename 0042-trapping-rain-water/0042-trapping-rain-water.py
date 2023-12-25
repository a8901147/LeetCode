class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxWall = height[0]
        rightMaxWall = height[len(height)-1]

        left = 1
        right = len(height)-2
        res = 0
        while left<=right:

            if leftMaxWall<=rightMaxWall:
                water =leftMaxWall - height[left] if leftMaxWall > height[left] else 0
                left += 1
                leftMaxWall = max(leftMaxWall,height[left-1])               
            else:
                water = rightMaxWall - height[right] if rightMaxWall > height[right] else 0
                right -= 1
                rightMaxWall =max(rightMaxWall,height[right+1])
                
            res += water

        return res

        
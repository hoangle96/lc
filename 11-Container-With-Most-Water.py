class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            ans = max(ans, min(height[left], height[right]) * width)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return ans
'''class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=heights
        max_area = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                area = min(a[i], a[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
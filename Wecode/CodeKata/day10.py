def get_max_area(height):
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
            continue
        right -= 1
    return area


#
#
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         result = []

#         for i in range(len(height) - 1):
#             for j in range(i + 1, len(height)):
#                 if height[i] <= height[j]:
#                     result.append(height[i] * (j - i))
#                 else:
#                     result.append(height[j] * (j - i))

#         return max(result)


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) - 1
#         area = 0

#         while l < r:
#             area = max(area, min(height[l], height[r]) * (r - l))
#             if height[l] < height[r]:
#                 l += 1
#                 continue
#             r -= 1
#         return area

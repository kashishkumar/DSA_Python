from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

https://leetcode.com/problems/two-sum/description/
"""

# Using Brute Force - two nested loops ~ O(n^2) time and O(1) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, number1 in enumerate(nums):
            for index2, number2 in enumerate(nums):
                if index1 != index2 and number1 + number2 == target:
                    return [index1, index2]
        return []


print(f"Using Brute Force")
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))


# Using sort and two pointer ~ O(nlogn) time and O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            if sorted_nums[left] + sorted_nums[right] == target:
                return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]
            elif sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            else:
                right -= 1
        return []


print(f"Using sort and two pointer")
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))


# Using Dictionary ~ O(n) time and O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in num_dict.keys():
                return [index, num_dict[difference]]
            else:
                num_dict[number] = index
        return []


print(f"Using dictionary with keys as numbers and values as index")
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))

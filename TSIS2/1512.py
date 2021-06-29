class Solution(object):
    def numIdenticalPairs(self, nums):
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j: cnt += 1
        return cnt


# class Solution(object):
#     def largestAltitude(self, gain):
#         a = 0
#         m = a
#         for i in gain:
#             a += i
#             if a > m: m = a
#         return m
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ret = [1] * l

        cur = 1
        for i in range(l):
            ret[i] *= cur
            cur *= nums[i]

        cur = 1
        for i in range(l - 1, -1, -1):
            ret[i] *= cur
            cur *= nums[i]

        return ret

        
class Solution:
    def bigger(self, x: int, y: int) -> bool:
        x = str(x)
        y = str(y)
        return int(x + y) >= int(y + x)

    def largestNumber(self, nums: List[int]) -> str:
        ret = ""
        while len(nums) > 0:
            maxi = 0
            m = nums[0]
            for i in range(1, len(nums)):
                if self.bigger(nums[i], m):
                    m = nums[i]
                    maxi = i
            
            nums.pop(maxi)
            ret += str(m)

        return str(int(ret))
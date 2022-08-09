class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        imax = 1
        imin = 1
        r = nums[0]

        for index in range(len(nums)):

            if nums[index] < 0:
                storage = imax
                imax = imin
                imin = storage

            imax = max(nums[index], nums[index] * imax)
            imin = min(nums[index], nums[index] * imin)

            r = max(r, imax)

        return r
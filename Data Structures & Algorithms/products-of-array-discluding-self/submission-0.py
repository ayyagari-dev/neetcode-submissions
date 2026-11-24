class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Prefix products (left to right)
        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]

        # Step 2: Suffix products (right to left)
        suffix = 1

        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]

        return result
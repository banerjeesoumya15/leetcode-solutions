class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            j = i+1
            k = n-1
            # target = -nums[i]
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j+=1
                else:
                    k-=1
        return [list(x) for x in set(map(tuple, result))]
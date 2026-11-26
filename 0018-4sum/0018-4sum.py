class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        # print(nums)
        result = []
        n = len(nums)
        for i in range(0, n-3):
            for j in range(i+1,n-2):
                left = j+1
                right = n-1
                
                while left < right:
                    # sum = (nums[i] + nums[j] + nums[left] + nums[right])
                    # print(nums[i],nums[j],nums[left],nums[right])
                    # print(sum)
                    if (nums[i] + nums[j] + nums[left] + nums[right]) == target:
                        result.append(tuple([nums[i],nums[j],nums[left],nums[right]]))
                        left+=1
                        right-=1
                    elif (nums[i] + nums[j] + nums[left] + nums[right]) < target:
                        left+=1
                    elif (nums[i] + nums[j] + nums[left] + nums[right]) > target:
                        right-=1

        result = set(result)
        result2 = [list(x) for x in result]
        return result2
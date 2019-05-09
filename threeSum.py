class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        # write your code here
        nums.sort()
        triples = []
        
        for i in range(0,len(nums)-2):
            target = 0 - nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    if [nums[i],nums[left],nums[right]] not in triples:
                        triples.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                if nums[left] + nums[right] < target:
                    left += 1
                if nums[left] + nums[right] > target:
                    right -= 1
   
        return triples
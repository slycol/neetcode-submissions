class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        answers = [0,0]
        for i in range(len(nums)):
            if (target - nums[i]) in seen.keys():
                answers[1]=i
                answers[0]=seen[target-nums[i]]
                return answers
            seen[nums[i]]=i
        return null
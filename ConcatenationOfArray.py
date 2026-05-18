from ast import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer: List[int] = []
        count = 0
        for k, v in enumerate(nums * 2, 0):
            answer.append(max(nums[k - len(nums)], 0))

sol = Solution()
sol.getConcatenation([1, 2, 1])
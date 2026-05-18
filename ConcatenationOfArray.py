
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

sol = Solution()
sol.getConcatenation([1, 2, 1])
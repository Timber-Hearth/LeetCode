from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i + n])

        return answer

sol = Solution()
sol.shuffle([2,5,1,3,4,7], 3)
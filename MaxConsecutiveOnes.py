from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count = 0
        else:
            count += 1
            max_count = max(count, max_count)
    return max_count

findMaxConsecutiveOnes([1,1,0,1,1,1])
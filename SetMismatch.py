def SetMismatch(nums):
    n = len(nums)
    expected_sum = n * (n + 1)
    real_sum = sum(nums)

    dup = -1
    seen = set()

    for num in nums:
        if num in seen:
            dup = num
        seen.add(num)

    missing = expected_sum - (real_sum - dup)
    return [dup, missing]




print(SetMismatch([1, 2, 2, 4]))
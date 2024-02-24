

def maximumSubarraySum(nums: list[int], k: int) -> int:
    highest = 0
    p0 = 0
    while p0 <= len(nums)-k:
        breakpoint()
        window = set(nums[p0:p0+k])
        if len(set(window)) == 3:
            highest = max(highest, sum(window))
        p0 += 1
    return highest


if __name__ == "__main__":
    maximumSubarraySum([1,2,3,4,5], 2)
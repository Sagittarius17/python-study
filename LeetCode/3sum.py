def three_sum(nums):
    result = []
    length = len(nums)
    nums.sort()
    for i in range(length):
        if i != 0 and nums[1] == nums[i-1]:
            continue
        j = i + 1
        k = length - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                result.append(
                    [nums[i], nums[j], nums[k]]
                )
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return result


if __name__ == "__main__":
    test_case = [-1, 0, 1, 2, -1, -4]
    ans = three_sum(test_case)
    print(ans)
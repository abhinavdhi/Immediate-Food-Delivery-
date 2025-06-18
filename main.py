def divideArray(nums, k):
    nums.sort()
    result = []
    i = 0
    n = len(nums)

    while i < n:
        if i + 2 >= n:
            return []

        group = [nums[i], nums[i + 1], nums[i + 2]]

        if group[2] - group[0] <= k:
            result.append(group)
            i += 3
        else:
            return []

    return result


# Example usage
if __name__ == "__main__":
    nums = [1, 3, 4, 6, 8, 9]
    k = 2
    print(divideArray(nums, k))

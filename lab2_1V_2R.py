def found_triple_sum(arr, k):
    arr.sort()
    for i in range(0, len(arr) - 1):
        left_ptr = i + 1
        right_ptr = len(arr) - 1
        while left_ptr < right_ptr:
            triple_sum = arr[i] + arr[left_ptr] + arr[right_ptr]
            if triple_sum == k:
                return True
            if triple_sum < k:
                left_ptr += 1
            elif triple_sum > k:
                right_ptr -= 1
    return False


def solve(a, k):
    a.sort()
    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):
            low = j + 1
            high = n - 1

            while low <= high:
                middle = (low + high) // 2
                _sum = a[middle] + a[i] + a[j]
                if _sum == k:
                    return True
                if _sum > k:
                    high = middle - 1
                if _sum < k:
                    low = middle + 1

    return False


nums = [1, 4, 1000, 20, 700, 300, 8, 6, 500, 501]
target_sum = 720

print(solve(nums, target_sum))

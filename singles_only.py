
lst1 = [1,1,5,3,2,5,2]
arr1 = [5, 3, 4, 3, 5, 5, 3]
arr2 = [-1, 1, 1, -1, -1, 1, 0, 3]

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    for i in range(1,len(nums)):
        ans ^= nums[i]
    return ans

#print(singleNumber(lst1))


def single_number(arr):
    ones, twos = 0, 0
    for x in arr:
        ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x)
    assert twos == 0
    return ones

print(single_number(arr1))
print(single_number(arr2))
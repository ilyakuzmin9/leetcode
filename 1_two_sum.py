from typing import List
import time
import random


# def twoSum(nums: List[int], target: int) -> List[int]:
#     list_len = range(len(nums))
#     for i in range(len(nums)):
#         sub_list_len = range(i+1, len(nums))
#         for j in range(i+1, len(nums)):
#             try:
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#             except IndexError:
#                 break
#     return[]


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    # for i in range(len(nums)):
    #     hash_table[nums[i]] = i
    for i, val in enumerate(nums):
        hash_table[val] = i

    for j in range(len(nums)):
        item = target - nums[j]
        if item in hash_table and j != hash_table[item]:
            return [j, hash_table[item]]
    return []


# def twoSum(nums: List[int], target: int) -> List[int]:
#     hash_map = {}
#     for i in range(len(nums)):
#         if nums[i] in hash_map:
#             return [i, hash_map[nums[i]]]
#         else:
#             hash_map[target - nums[i]] = i


if __name__ == '__main__':
    # Generate 5 random numbers between 10 and 30
    random_list = random.sample(range(1, 100), 99)
    # nums = [1, 2, 9, 9, 4]
    target = 1555
    start = time.time()
    print(twoSum(random_list, target))
    end = time.time()
    print(end - start)

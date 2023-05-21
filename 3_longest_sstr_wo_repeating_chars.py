class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     set_elem = set()
    #     left_pointer = 0
    #     result_len = 0
    #     for right_pointer in range(len(s)):
    #         rpoin = s[right_pointer]
    #         lpoin = s[left_pointer]
    #         while s[right_pointer] in set_elem:
    #             set_elem.remove(s[left_pointer])
    #             left_pointer += 1
    #         set_elem.add(s[right_pointer])
    #         ipoin = right_pointer - left_pointer + 1
    #         result_len = max(result_len, right_pointer - left_pointer + 1)
    #
    #     return result_len


    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        cur_len = 0
        substr_pointer = 0
        hash_table = {}

        for i, val in enumerate(s):
            if s[i] in hash_table and hash_table[val] >= substr_pointer:
                substr_pointer = hash_table[val] + 1
                cur_len = i - hash_table[val]
                hash_table[val] = i
            else:
                hash_table[val] = i
                cur_len += 1
                max_len = max(max_len, cur_len)

        print(hash_table)

        return max_len


if __name__ == '__main__':
    st = 'qwwewq'
    sol = Solution()
    result = sol.lengthOfLongestSubstring(st)
    print(result)

"""
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false.
He wants to confuse the students by maximizing the number of consecutive questions with the same answer
(multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question.
 In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.


"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = 0
        i = 0
        d = {'T': 0, 'F': 0}

        for j in range(len(answerKey)):
            d[answerKey[j]] += 1
            max_freq = max(max_freq, d[answerKey[j]])
            if j - i + 1 > max_freq + k:
                d[answerKey[i]] -= 1
                i += 1


        return len(answerKey) - i


if __name__ == '__main__':
    answerKey = "TTFF"
    k = 2
    sol = Solution()
    result = sol.maxConsecutiveAnswers(answerKey, k)
    print(result)
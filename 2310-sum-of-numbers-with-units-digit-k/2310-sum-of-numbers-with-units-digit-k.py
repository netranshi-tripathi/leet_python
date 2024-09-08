class Solution:
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
        for n in range(1, 11):  # Since k can only affect the last digit, check up to 10 times.
            if (n * k) % 10 == num % 10 and n * k <= num:
                return n
        return -1

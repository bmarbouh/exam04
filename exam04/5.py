def palindrome_partitioner(s: str) -> int:
    n = len(s)

    if n <= 1:
        return 0

    dp = [0] * n
    
    for i in range(n):
        dp[i] = i
    
    for i in range(n):
        for j in range(i + 1):
            left = j
            right = i
            palindrome = True

            while left < right:
                if s[left] != s[right]:
                    palindrome = False
                    break
                left += 1
                right -= 1

            if palindrome:
                if j == 0:
                    dp[i] = 0
                elif dp[j - 1] + 1 < dp[i]:
                    dp[i] = dp[j - 1] + 1

    return dp[n - 1]

palindrome_partitioner("aab")
# print(palindrome_partitioner("aba"))
# print(palindrome_partitioner("abc"))

def longest_common_subsequence(str1, str2):

    m = len(str1)
    n = len(str2)


    # Create a table to store the lengths of LCS for subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]


    # Fill up the table using dynamic programming
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # I don't really get this part


    # Backtrack to find the LCS
    lcs = []
    i, j = m, n


    while i > 0 and j > 0:

        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1


    # Reverse the LCS list to get the correct order
    lcs.reverse()


    # Convert the list to a string and return
    return ''.join(lcs)





# Example usage:

seq1 = "ABCDGH"
seq2 = "AEDFHR"

print("LCS:", longest_common_subsequence(seq1, seq2))  # Output: "ADH"
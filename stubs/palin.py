
def isPalindtrome(string):
    return (string[::] == string[::-1])


def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substr = string[i:j+1]
            if len(substr) > len(longest) and isPalindtrome(substr):
                longest = substr
    return longest


#  Longest palindrome substring

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

# (a)
# def longestPalindrome(self, s):
#     self.maxlen = 0
#     self.start = 0
#
#     for i in range(len(s)):
#         self.expandFromCenter(s, i, i)
#         self.expandFromCenter(s, i, i + 1)
#     return s[self.start:self.start + self.maxlen]
#
#
# def expandFromCenter(self, s, l, r):
#     while l > -1 and r < len(s) and s[l] == s[r]:
#         l -= 1
#         r += 1
#
#     if self.maxlen < r - l - 1:
#         self.maxlen = r - l - 1
#         self.start = l + 1



if __name__ == '__main__':

    #Problem 1: given a string of words, reverse the words
    #given an input string, reverse the words
    line = 'aa dfdfs fsdfsfs sfsdfs'
    print ('input is :' + line)

    #convert to a list by splitting on a space
    lst_line = line.split(' ')
    print ('split line:' + str(lst_line))

    # now reverse the list by using slice
    print (lst_line[::-1])

    # Problem2: isPalindrome
    s = "abaa"
    if isPalindtrome(s):
        print('%s is a palindrom' % s)
    else:
        print('%s is not a palindrom' % s)

    # Problem2: longestPalindromicSubstring
    s = "abaxxyyzyyxxzzABC"
    s2 = longestPalindromicSubstring(s)
    print("longest palindrome in [%s] is [%s]" % (s, s2))
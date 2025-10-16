"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def common_prefix(s):
    s=s
    res=''
    for i in range(len(s[0])):
        for j in s[1:]:
            if i == len(j) or j[i]!=s[0][i]:
                return res
        res +=s[0][i]
print(common_prefix(["flower","flow","flight"]))

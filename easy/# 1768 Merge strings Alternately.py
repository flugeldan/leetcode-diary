# 1768. Merge Strings Alternately
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=programming-skills  
class Solution(object):
    def mergeAlternately(self, word1, word2):
        finalword=[]

        for c1, c2 in zip(word1, word2):
            finalword.append(c1)
            finalword.append(c2)
        finalword.extend(word1[len(word2):])
        finalword.extend(word2[len(word1):])
        return ''.join(finalword)

        











        
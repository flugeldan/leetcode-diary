# 389. Find the Difference
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-difference/description/?envType=study-plan-v2&envId=programming-skills

class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) == t.count(i):
                continue
            elif s.count(i) != t.count(i):
                return (i)

Легкая задачка, сравнивал кол во определенной буквы в двух словах, если какая то буква отличалась возвращал ее

        

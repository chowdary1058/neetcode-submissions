'''class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="".join(s.split())
        b=a.lower()
        c=""
        for i in a:
            if i.isalnum():
                c+=i
        if c.lower()==c[::-1].lower():
            return True
        else:
            return False'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(s.split())
        b = a.lower()
        c = ""

        for i in b:
            if i.isalnum():
                c += i

        if c == c[::-1]:
            return True
        else:
            return False








'''        a = ""

        for ch in s:
            if ch.isalnum():
                a += ch.lower()

        return a == a[::-1]'''
    
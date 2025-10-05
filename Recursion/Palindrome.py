def check(s,l,r):
    if l >= r :
        return True
    if s[l] != s[r]:
        return False
    else :
        return check(s ,l + 1 , r - 1)
def isPalindrome(s):
    # code here
    return check(s,0,len(s) - 1)

print(isPalindrome("aba"))
print(isPalindrome("abax"))
        
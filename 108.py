def areAnagram(str1, str2):
    hm = {}
    for i in str1:
        if hm.get(i):
            hm[i] += 1
        else:
            hm[i] = 1
            
    for i in str2:
        if hm.get(i):
            hm[i] += 1
        else:
            hm[i] = 1
            
    vals = list(set(list(hm.values())))
    for v in vals:
        if v%2 != 0:
            return False
        
    return True

str1 = "notmwhvwrb"
str2 = "norwvhwmtb"

print(areAnagram(str1, str2))
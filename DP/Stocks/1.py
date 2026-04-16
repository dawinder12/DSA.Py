a = [3,2,3,4,5,6,7]
prev = a[0]
maxi = 0
for i in range(1, len(a)):
    profit = a[i] - prev 
    if profit > maxi :
        maxi = profit 
    elif profit < 0 :
        prev = a[i]
print(maxi)

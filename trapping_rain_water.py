# Rain Water Trapping
arr = [3,0,0,2,0,4]
# ans = 10

maxL = [-1] * len(arr)
maxR = [-1] * len(arr)

maxL[0] = arr[0]
for i in range(1, len(arr)):
    maxL[i] = max(maxL[i-1], arr[i])
    
maxR[len(arr)-1] = arr[len(arr)-1]
for i in range(len(arr)-2, -1, -1):
    maxR[i] = max(maxR[i+1], arr[i])

total = 0
for i in range(len(arr)):
    total += min(maxR[i], maxL[i]) - arr[i]
print(total)

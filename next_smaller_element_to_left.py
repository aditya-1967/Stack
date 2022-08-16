# Next Smaller Element to left
arr = [4,5,2,10,8]
#ans = [-1, 4, -1, 2, 2]

ans = []
stack = []

for i in range(len(arr)):
    if len(stack) == 0:
        ans.append(-1)
    elif len(stack) > 0 and stack[-1] < arr[i]:
        ans.append(stack[-1])
    elif len(stack) > 0 and stack[-1] >= arr[i]:
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])
print(ans)

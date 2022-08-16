# Next Greater Element to Right
arr = [1,3,2,4]
#ans = [3,4,4,-1]
ans = []
stack = []
for i in range(len(arr)-1, -1, -1):
    if len(stack) == 0:
        ans.append(-1)
    elif len(stack) != 0 and stack[-1] > arr[i]:
        ans.append(stack[-1])
    elif len(stack) != 0 and stack[-1] <= arr[i]:
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])

print(ans[::-1])

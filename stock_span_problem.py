# Stock Span Problem
stock = [100, 80, 60, 70, 60, 75, 85]
# ans = [1, 1, 1, 2, 1, 4, 6]
ans = []
stack = []


for i in range(len(stock)):
    if len(stack) == 0:
        ans.append(-1)
    elif len(stack) > 0 and stack[-1][0] > stock[i]:
        ans.append(stack[-1][1])
    elif len(stack) > 0 and stack[-1][0] <= stock[i]:
        while len(stack) > 0 and stack[-1][0] <= stock[i]:
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
    stack.append([stock[i], i])

ans = [i - ans[i] for i in range(len(stock))]
print(ans)

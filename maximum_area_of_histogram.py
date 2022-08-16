# Maximum Area of Histogram
bars = [6, 2, 5, 4, 5, 1, 6]
# ans = 12

nsr = []
nsl = []
stack = []
bars.append(0)
for i in range(len(bars)):
    if len(stack) == 0:
        nsl.append(-1)
    elif len(stack) > 0 and stack[-1][0] < bars[i]:
        nsl.append(stack[-1][1])
    elif len(stack) > 0 and stack[-1][0] >= bars[i]:
        while len(stack) > 0 and stack[-1][0] >= bars[i]:
            stack.pop()
        if len(stack) == 0:
            nsl.append(-1)
        else:
            nsl.append(stack[-1][1])
    stack.append([bars[i], i])
    

stack.clear()

for i in range(len(bars)-1, -1, -1):
    if len(stack) == 0:
        nsr.append(-1)
    elif len(stack) != 0 and stack[-1][0] < bars[i]:
        nsr.append(stack[-1][1])
    elif len(stack) != 0 and stack[-1][0] >= bars[i]:
        while len(stack) > 0 and stack[-1][0] >= bars[i]:
            stack.pop()
        if len(stack) == 0:
            nsr.append(-1)
        else:
            nsr.append(stack[-1][1])
    stack.append([bars[i], i])

nsl.pop()
nsr = nsr[::-1]
nsr.pop()
# print(nsl)
# print(nsr)

width = [nsr[i] - nsl[i] - 1 for i in range(len(nsr))]
# print(width)
area = [bars[i] * width[i] for i in range(len(width))]
print(max(area))

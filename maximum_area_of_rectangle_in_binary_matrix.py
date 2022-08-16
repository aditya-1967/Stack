# Maximum Area of Rectangle in Binary Matrix

def NSR(bars):
    stack = []
    nsr = []
    bars.append(0)
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
    nsr = nsr[::-1]
    nsr.pop()
    return nsr


def NSL(bars):
    stack = []
    nsl = []
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

    nsl.pop()
    return nsl


def max_area_histogram(bars):
    right = NSR(bars)
    left = NSL(bars)
    width = [right[i] - left[i] - 1 for i in range(len(right))]
    area = [bars[i] * width[i] for i in range(len(width))]
    return max(area)

arr = [[0,1,1,0], [1,1,1,1], [1,1,1,1], [1,1,0,0]]

bars = []
area = 0
for j in range(len(arr[0])):
    bars.append(arr[0][j])
area = max_area_histogram(bars)

for i in range(1, len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            bars[j] = 0
        else:
            bars[j] = bars[j] + arr[i][j]
    area = max(area, max_area_histogram(bars))

print(area)

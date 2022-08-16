# Minimum Element in Stack without extra space

stack = []
min_element = float('inf')

def get_min():
    if len(stack) == 0:
        return -1
    return min_element


def push(ele):
    if len(stack) == 0:
        return -1
    else:
        if ele >= min_element:
            stack.append(ele)
            min_element = ele
        elif ele < min_element:
            stack.append(2 * ele - min_element)
            min_element = ele
    return


def pop():
    if len(stack) == 0:
        return -1
    else:
        if stack[-1] >= min_element:
            stack.pop()
        elif stack[-1] < min_element:
            min_element = 2 * min_element = stack[-1]
            stack.pop()
    return

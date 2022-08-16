# Minimum Element in Stack with extra space

arr = [18, 19, 29, 15, 16]
stack = []
support = []

def get_min():
    if len(support) == 0:
        return -1
    return support[-1]


def push(ele):
    stack.append(ele)
    if len(support) == 0 or support[-1] >= ele:
        support.append(ele)
    return


def pop():
    if len(stack) == 0:
        return -1
    ans = stack[-1]
    stack.pop()
    if support[-1] == ans:
        support.pop()
    return

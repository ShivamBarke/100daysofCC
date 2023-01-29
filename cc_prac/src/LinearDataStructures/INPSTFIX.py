for _ in range(int(input())):
    n = int(input())
    A = input().rstrip()
    precedence = {'(': 0, ')': 0, '^': 3, '/' : 2, '*' : 2, '+' : 1, '-' : 1}
    stack = []
    ans = []
    for i in A:
        if i.isalnum():
            ans+=i
        else:
            if i=="(":
                stack.append(i)
            elif i==")":
                while len(stack)>0 and stack[-1] != "(":
                    ans.append(stack[-1])
                    stack.pop()
                if stack[-1] == "(":
                    stack.pop()
            else:
                while len(stack)>0 and precedence.get(i) <= precedence.get(stack[-1]):
                    ans.append(stack[-1])
                    stack.pop()
                stack.append(i)

    while(len(stack)>0):
        ans.append(stack[-1])
        stack.pop()
    
    print("".join(ans))
            
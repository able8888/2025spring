from collections import deque

b={')':'(','}':'{',']':'['}
c=[')','}',']']
d=['(','{','[']
def f(a):
    q=deque()
    for i in range(len(a)):
        if a[i] in c:
            if q == deque([]):
                return 'No'
            else:
                if q.pop()==b[a[i]]:
                    continue
                elif q.pop() in d:
                    return 'No'
                elif q[len(q)-1] in c:

                    q.append(a[i])

        else:
            if q == deque([]):
                q.append(a[i])
                continue
            elif q[len(q)-1] in d:
                q.append(a[i])
            elif q[len(q)-1] in c :
                return 'No'
    if q == deque([]):
        return 'Yes'
a=list(input())
print(f(a))



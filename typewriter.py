def typewriter(S):
    A = S.split()
    lst = []
    for i in range(0, len(A)):
        if (A[i] == '+'):
            sum = lst[len(lst) - 2] + lst[len(lst) - 1]
            lst.remove(lst[len(lst) - 2])
            lst.remove(lst[len(lst) - 1])
            lst.append(sum)
        elif (A[i] == '-'):
            minus = abs(int(lst[len(lst) - 2]) - int(lst[len(lst) - 1]))
            lst.remove(lst[len(lst) - 2])
            lst.remove(lst[len(lst) - 1])
            lst.append(minus)
        elif (A[i] == 'DUP'):
            lst.append(lst[len(lst) - 1])
        elif (A[i] == 'POP'):
            # solve this to find out what is wrong then use this as a debugging exercise for blog post.
            # lst.pop(lst[len(lst) - 1]) causes an error
            # solution
            lst.remove(lst[len(lst) - 1])
        if (A[i] == 'DUP' or A[i] == 'POP' or A[i] == '-' or A[i] == '+'):
            continue

        # int with base 10 conversion to int
        lst.append(int(float(A[i])))

    return lst[len(lst) - 1]

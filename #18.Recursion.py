# Finding factorial

def facto(n):
    if n!=1:
        return n*facto(n-1)
    else:
        return 1

print(facto(5))
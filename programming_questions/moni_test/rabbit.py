

# 1,1,2,3
def rabbit(month):
    if month == 1 or month == 2:
        return 1
    a,b = 1,1
    for i in range(3,month + 1):
        c = a + b
        a = b
        b = c
    return b

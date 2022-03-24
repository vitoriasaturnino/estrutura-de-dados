def fat(n):
    if n == 0 or n == 1: return 1
    return n * fat(n-1)
print(fat(4)) #repetição feita usando dado

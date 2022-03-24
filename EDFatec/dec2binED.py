def dect2bin(n):
    p = []
    while n != 0:
        p.append(n%2)
        n = n // 2 #divisão inteira

    while len(p) > 0:
        print (p.pop(), end='')

dec2bin(18);


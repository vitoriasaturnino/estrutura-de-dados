Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 42
id(x)
2749017818640

a = [1, 2, 3]
b = a
a[0] = 42
a
[42, 2, 3]
b
[42, 2, 3]


id(a)
2749055728512
id(b)
2749055728512
//a e b são o mesmo objeto
SyntaxError: invalid syntax

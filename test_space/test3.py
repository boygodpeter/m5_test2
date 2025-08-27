# test_inner.py
for i in range (10):
    print(i)

def foo(num):
    print("start")
    for i in range(num):
        print("  loop", i)
    print("end")

def a():
    print('a')

foo(3)
# 你知道嘛？python 的 print 有四种写法！看我给你慢慢写来...

def foo(abab: list):
    abab.sort()


def bar(woc):
    print("{}".format(woc))


if __name__ == '__main__':
    print("Hello, Python!")

    nums = [1, 2, 3, 4, 5]
    print('init nums >> ', nums)
    nums.reverse()
    print(f"after reverse >> {nums}")
    foo(nums)
    print("final res >>", end=' ')
    bar(nums)  # Output: [1, 2, 3, 4, 5]

# 小知识点：
# 代码文件的名字无所谓
# 不加 __name__ == '__main__' 那一行，也可以运行
# python，tnnd，不需要类型指定哦！
# I love `f"{param-a} {param-b}"` in python!

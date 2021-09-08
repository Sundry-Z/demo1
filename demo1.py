"""
计算1到M（含M）之间的合数数量，输出其值。
"""
def com_num():
    M = eval(input("Please enter a positive integer M(M<10000) :"))
    i = 0
    for m in range(2, M + 1):  #
        for n in range(2, m - 1):  # The range of factors of composite Numbers
            if m % n == 0:
                i += 1
                break
    print(i)

com_num()
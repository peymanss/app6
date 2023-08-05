def k_m_m(a, b):
    max_num = max(a , b)
    min_num = min(a , b)
    
    for i in range(max_num, (max_num * min_num) + 1, max_num):
        if i % min_num == 0:
            return i

a = int(input("input the first number=="))
b = int(input("input the first number=="))

lcm = k_m_m(a, b)
print("the answer is==" , lcm)
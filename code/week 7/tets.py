import time


def pipeizhi(p):
    # abcdabcy
    # next函数偏移表next[]:-1    0    0    0    0    1    2    3
    j = 0
    k = -1
    next = [-1]
    for i in range(1, len(p)):
        next.append(0) # 先指定一个next数组为[-1,0,0,0...]
    try:
        while j < len(p) - 1:
            if k == -1 or p[j] == p[k]:
   # 如果找到了，那就开始滑动。j 遍历的事数组下标，而k则是为偏离表赋值的。画个图可能更加好理解
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]
    except IndexError:
        print (next, k, j)  # 不可能错的放心
    return next


def KMP(s, t): #s是目标船 ，t是模式串
    slen = len(s)
    tlen = len(t)
    if slen >= tlen:
        i = 0
        j = 0
        next = pipeizhi(t)
       # print next
        while i < slen: #开始遍历
            #print (i,j)
            if j == -1 or s[i] == t[j]:
       #i是遍历，j是目标串中找到的模式串中前面一部分的长度。
                i += 1
                j += 1
            else:
                j = next[j]
            if j == tlen:
                return i - tlen
    return -1 #-1就是没有找到啊


def multiple_kmp(aim_str, model_str):
    result = []
    m = 0
    #print(aim_str)
    #print(len(aim_str))
    while True:
        #print(m)
        if m == len(aim_str)-1:
            break
        else:
            out = KMP(aim_str[m:], model_str)
            if out != -1:
                result.append(m + out)
                m = m + out + 1
            if out == -1:
                break
    return result
start = time.time()
print(multiple_kmp("AAATTTAAATTTAAATTTAAATTT"*10000,"TTT"))
print(time.time()-start)
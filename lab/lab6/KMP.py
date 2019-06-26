import time


def get_next_array(the_str):
    j = 0
    k = -1
    next_array = [-1] + [0] * (len(the_str)-1)
    while j < len(the_str) - 1:
        if k == -1 or the_str[j] == the_str[k]:
            j += 1
            k += 1
            next_array[j] = k
        else:
            k = next_array[k]
    return next_array


def kmp(aim_str, model_str):
    aim_len = len(aim_str)
    model_len = len(model_str)
    re = []

    if aim_len >= model_len:
        i = 0
        j = 0
        next_array = get_next_array(model_str)
        while i < aim_len:
            if j == -1 or aim_str[i] == model_str[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]
            if j == model_len:
                re.append(i - model_len)
                i = i - model_len + 1
                j = 0

    return ["time: " + str(len(re))] + re


start = time.time()

print(kmp("ABAB"*10,"AB"))

print(time.time()-start)


print(get_next_array("abaabcac"))
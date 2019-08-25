def sub_group(tsum, set, cache):
    if cache[tsum][set[0]]:
        return cache[tsum][set[0]]

    print(tsum, set, cache)
    print("*************")
    sub_group_count = sub_index = 0
    for i in set:
        sub_index += 1
        if i < tsum:
            nset = set[sub_index:]
            if len(nset) > 0:
                sub_group_count += sub_group(tsum-i, nset, cache)
        else:
            if i == tsum:
                sub_group_count += 1
            else:
                break
    cache[tsum][set[0]] = sub_group_count
    return sub_group_count

def solution(n):
    cache = [[None for x in range(n+1)] for y in range(n+1)]
    return sub_group(n, range(1,n), cache)


    
# for i in range(3,200):
#     print "step", i
#     print solution(i)

# print solution(2)
# print solution(3)
# print solution(4)
print (solution(6))
# # print solution(20)
# print (solution(200))
# print (solution(300))
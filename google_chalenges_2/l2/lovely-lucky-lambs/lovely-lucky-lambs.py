def handout_generous(total_lambs):
    total_paid_henchman = 1

    available_lamb = total_lambs - 1

    next_henchman_price = 2

    while next_henchman_price <= available_lamb:
        total_paid_henchman += 1
        available_lamb -= next_henchman_price
        next_henchman_price = next_henchman_price * 2

    return total_paid_henchman    

def handout_stingy(total_lambs):
    if total_lambs < 3:
        return total_lambs

    total_paid_henchman = 2
    available_lamb = total_lambs - 2
    paid_henchman1_price = 1
    paid_henchman2_price = 1

    next_henchman_price =  2

    while next_henchman_price <= available_lamb:
        total_paid_henchman += 1
        available_lamb -= next_henchman_price
        paid_henchman1_price, paid_henchman2_price = paid_henchman2_price, next_henchman_price
        next_henchman_price =  paid_henchman1_price + paid_henchman2_price

    return total_paid_henchman

def solution(total_lambs):
    h1 = handout_stingy(total_lambs)
    h2 = handout_generous(total_lambs)
    # print(h1, h2)
    return h1 - h2
    
# print(handout_stingy(10))
# print(handout_generous(10000000000))
print(solution(10))
print(solution(143))


# Lovely Lucky LAMBs
# ==================

# Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). 
# Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

# However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt 
# and you'll all get demoted back to minions again! 

# There are 4 key rules which you must follow in order to avoid a revolt:
#     1. The most junior henchman (with the least seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.)
#     2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do.
#     3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get.  
#       (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.  The 2nd most junior henchman would require at least as many LAMBs 
#       as the most junior henchman.)
#     4. You can always find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that another henchman could be added as 
#       the most senior while obeying the other rules, you must always add and pay that henchman.

# Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

# Write a function called solution(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which 
# represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy 
# as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 
# 3 henchmen (1, 2, and 4 kLAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). 
# cTherefore, solution(10) should return 4-3 = 1.

# To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. You can expect total_lambs to always be a positive integer less than 1 billion (10 ^ 9).

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases -- 
# Input:
# solution.solution(143)
# Output:
#     3

# Input:
# solution.solution(10)
# Output:
#     1

# -- Java cases -- 
# Input:
# Solution.solution(143)
# Output:
#     3

# Input:
# Solution.solution(10)
# Output:
#     1
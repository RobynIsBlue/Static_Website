











#def dumb(n):



def rec_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n != 4:
        count = rec_fib(n-2) + rec_fib(n - 1)
    else:
        count = rec_fib(n - 1) + 1
    return count


def rec_fibby(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return rec_fibby(n - 1) + rec_fibby(n - 2)

print(rec_fibby(10))
    


def fib(n):
    if n <= 1:
        return 0
    current_count = 1
    past_count = 0
    future_count = 0
    for x in range(n - 2):
        future_count = past_count + current_count
        print(future_count, past_count, current_count)
        past_count = current_count
        current_count = future_count
        
    return current_count

#print(fib(6))
#print(rec_fib(9))

"""
=0
=1
=1
=2
=3
=5
=8
"""

#print(dumb_bs(5))

from bisect import bisect
from itertools import combinations
from functools import wraps

from benchmark import benchmark

def naive_longest_inc_subseq(seq):
    """ 1) 단순한 방법"""
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)
            
            
def dp_longest_inc_subseq(seq):
    """ 2) 동적 계획법"""
    L = [1] * len(seq)
    res = []
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+L[pre])
    return max(L)


def memo(func):
    cache = {}
    
    @warps(func)
    def warp(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def memoized_longest_inc_subseq(seq):
    """3) 메모이제이션"""
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1+L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

def longest_inc_bisec(seq):
    """4) 이진 검색"""
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
        # print(end)
    return len(end)


@benchmark
def test_naive_longest_inc_subseq():
    print(naive_longest_inc(subseq(s1)))
    
@benchmark
def test_dp_longest_inc_subseq():
    print(test_dp_longest_inc_subseq(subseq(s1)))
    
@benchmark
def test_memoized_longest_inc_subseq():
    print(test_memoized_longest_inc_subseq(s1))
    
@benchmark
def test_longest_inc_bisec():
    print(test_longest_inc_bisec(s1))
    
s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
print(s1)
test_naive_longest_inc_subseq()
test_dp_longest_inc_subseq()
test_memoized_longest_inc_subseq()
test_longest_inc_bisec()

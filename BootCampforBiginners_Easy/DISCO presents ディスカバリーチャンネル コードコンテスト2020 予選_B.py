import itertools

'''
累積和(itertools.accumulate)を使って配列を作って最小差を求める
愚直にfor文を回してsum()関数を使うと計算量がO(N^2)になって間に合わない
'''

N = int(input())
A = list(map(int, input().split()))

mini = float('inf')

cumsum = list(itertools.accumulate(A))
A.reverse()
rev = list(itertools.accumulate(A))
rev.reverse()
cumsum.pop()
rev.pop(0)

for i, j in zip(cumsum,rev):
    if abs(i-j) < mini:
        mini = abs(i-j)

print(mini)
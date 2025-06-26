V = int(input())
vote = list(input())

if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') < vote.count('B'):
    print('B')
else:
    print('Tie')
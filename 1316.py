n = int(input())
word = [
    input()
    for _ in range(n)
]

group_word_n = 0
for i in range(n):
    v = [0] * 26
    flg = 0
    for wi in range(1, len(word[i])):
        w = word[i][wi]
        if wi == 1:
            if word[i][0] != w:
                asc_n = ord(word[i][0]) - ord('a')
                v[asc_n] += 1
        else:
            if word[i][wi-1] == w:
                continue

        asc_n = ord(w) - ord('a')
        v[asc_n] += 1
        if v[asc_n] > 1:
            flg = 1
            break
    if flg == 0:
        group_word_n += 1

print(group_word_n)
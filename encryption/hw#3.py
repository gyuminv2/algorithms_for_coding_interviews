# | 2019253043 | 박규민 |
# | 과제3 - 대치 암호 문제 |
table = dict(
    {
        'a' : 'N',
        'b' : 'O',
        'c' : 'A',
        'd' : 'T',
        'e' : 'R',
        'f' : 'B',
        'g' : 'E',
        'h' : 'C',
        'i' : 'F',
        'j' : 'U',
        'k' : 'X',
        'l' : 'D',
        'm' : 'Q',
        'n' : 'G',
        'o' : 'Y',
        'p' : 'L',
        'q' : 'K',
        'r' : 'H',
        's' : 'V',
        't' : 'I',
        'u' : 'J',
        'v' : 'M',
        'w' : 'P',
        'x' : 'Z',
        'y' : 'S',
        'z' : 'W'
    }
)


평문 = "this message is easy to encrypt but hard to find the key"
암호문 = ""

for c in 평문:
    if c in table:
        암호문 += table[c]
    else:
        암호문 += c
print('평문 :', 평문)
print('암호문 :', 암호문)
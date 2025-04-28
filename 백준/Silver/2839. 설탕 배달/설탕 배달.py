n = int(input())
rtn = 0

while 1:
	if n == 0:
		break
	if n % 5 == 0:
		n -= 5
		rtn += 1
		continue
	if n % 3 == 0:
		n -= 3
		rtn += 1
		continue
	if n >= 5:
		n -= 5
		rtn += 1
		continue
	if n >= 3:
		n -= 3
		rtn += 1
		continue
	break

if n != 0:
	print('-1')
else:
	print(rtn)
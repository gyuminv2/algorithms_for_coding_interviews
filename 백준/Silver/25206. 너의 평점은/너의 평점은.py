mean = 0.0
div = 0.0

for i in range(20):
	sub = list(input().split())
	tool = float(sub[1])
	if sub[2] == 'P':
		continue
	if sub[2] == 'A+':
		mean = mean + (4.5 * tool)
	if sub[2] == 'A0':
		mean = mean + (4.0 * tool)
	if sub[2] == 'B+':
		mean = mean + (3.5 * tool)
	if sub[2] == 'B0':
		mean = mean + (3.0 * tool)
	if sub[2] == 'C+':
		mean = mean + (2.5 * tool)
	if sub[2] == 'C0':
		mean = mean + (2.0 * tool)
	if sub[2] == 'D+':
		mean = mean + (1.5 * tool)
	if sub[2] == 'D0':
		mean = mean + (1.0 * tool)
	div = div + float(sub[1])

rtn = mean / div
print(f'{rtn:.6f}')
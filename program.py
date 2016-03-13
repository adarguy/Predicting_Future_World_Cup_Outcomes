import sys

def main():
	f = open('Teams.txt','r+').read().splitlines()
	#print(team)

	x = open('list.txt', 'r+').read().splitlines()
	#lists = x.read().splitlines()
	print(f[0])
	print(x)
	list2 = []
	for l in range(len(f)):
		if f[l] not in list2:
			list2.append(f[l])
			print(f[l])

	print(list2)

	a = open('newlist.txt','w')
	for p in list2:
		a.write(p+', ')
	a.close
if __name__ == '__main__':
	main()
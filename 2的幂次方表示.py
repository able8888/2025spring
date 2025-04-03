def f(a):
	def find(a):
		n=0
		while 2**n<=a:
			n+=1
		return n-1
	def express(n):
		if n==0:
			return '2(0)'
		elif n==1:
			return '2'
		elif n==2:
			return '2(2)'
		else:
			return '2('+f(n)+')'
	if a==0:
		return ''
	result=''
	while a>0:
		max_power=find(a)
		if result:
			result += '+'
		result += express(max_power)
		a-=2**max_power
	return result
print(f(int(input())))


import heapq
heap=[]
lis=[]
while True:
	try:
		i=input().split()
		if len(i) == 0:
			continue
		elif i[0]=='push':
			heapq.heappush(heap,int(i[1]))
			lis.append(int(i[1]))
		elif i[0]=='pop' and len(heap)>0:
			lis.pop(len(lis)-1)
			heapq.heapify(lis)
			heap=lis
		elif i[0]=='min' and len(heap)>0:
			b=heap[0]
			print(b)
		else:
			continue
	except EOFError:
		break
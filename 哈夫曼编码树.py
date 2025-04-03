import heapq
class Node:#建类
	def __init__(self, char,freq):
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None
	def __lt__(self, other):
		if self.freq == other.freq:
			return self.char< other.char
		return self.freq < other.freq
def huf_build_tree(characters):#建树——>返回根
	heap=[]
	for char,freq in characters.items():
		heapq.heappush(heap,Node(char,freq))
	while len(heap)>1:
		left = heapq.heappop(heap)
		right = heapq.heappop(heap)
		merge = Node(min(left.char,right.char),left.freq+right.freq)
		merge.left = left
		merge.right = right
		heapq.heappush(heap,merge)
	return heap[0]
def encode_tree(root):#生成每个字符的编码
	codes={}
	def f(node,code):
		if node.left is None and node.right is None:
			codes[node.char]=code
		else:
			f(node.left,code+'0')
			f(node.right,code+'1')
	f(root,'')
	return codes
def encoding_tree(codes,string):#对于输入的字符进行编码
	encoded=''
	for char in string:
		encoded+=codes[char]
	return encoded
def decoding_tree(root,encoded_string):#对于输入的数字进行解码
	decoded=''
	node=root
	for a in encoded_string:
		if a=='0':
			node = node.left
		else:
			node = node.right
		if node.left is None and node.right is None:
			decoded+=node.char
			node=root
	return decoded
#主程序
n=int(input())
characters={}
for _ in range(n):
	char,freq=input().split()
	characters[char]=int(freq)
root=huf_build_tree(characters)
codes=encode_tree(root)
strings=[]
while True:
	try:
		line=input()
		strings.append(line)
	except EOFError:
		break
results=[]
for string in strings:
	if string[0]=='0' or string[0]=='1':
		results.append(decoding_tree(root,string))
	else:
		results.append(encoding_tree(codes,string))
for result in results:
	print(result)





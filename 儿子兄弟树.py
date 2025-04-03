def buildTreeInBinary(level):
	global nodesPtr
	if nodesPtr >= len(nodes):
		return None

	current_level, current_data = nodes[nodesPtr]
	if current_level != level:
		return None

	# 创建当前节点
	node = BinaryTree(current_data)
	nodesPtr += 1

	# 第一个子节点作为左孩子
	node.left = buildTreeInBinary(level + 1)

	# 其余子节点作为右兄弟
	if node.left:
		current_sibling = node.left
		while True:
			next_sibling = buildTreeInBinary(level + 1)
			if not next_sibling:
				break
			current_sibling.right = next_sibling
			current_sibling = next_sibling

	return node

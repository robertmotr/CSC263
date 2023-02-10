def swapHelper(x: BSTNode, min: int, max: int) -> List[BSTNode]:
	if x.left != None:
		if x.left.key > x.key and x.left.visited == False:
			x.left.visited = True
			return [x.left]
		elif x.left.key > max and x.left.visited == False:
			x.left.visited = True
			return [x.left]
		else:
			max = x.key
			return swapHelper(x.left, min, max)
	if x.right != None:
		if x.right.key > x.key and x.right.visited == False:
			x.right.visited = True
			return [x.right]
		elif x.right.key < min and x.right.visited == False:
			x.right.visited = True
			return [x.right]
		else:
			min = x.key
			return swapHelper(x.right, min, max)
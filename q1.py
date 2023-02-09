import typing

def swapHelper(x: BSTNode, min: int, max: int) -> List[Any]:
	# 1. In-order traversal on BST
	# 2. For each node, update min/max and check if it is violated
	if x.left != None:
		if x.left.value > x.value and x.left.visited == False:
			x.left.visited = True
			return [x]
		elif x.value > max and x.left.visited == False:
			x.left.visited = True
			return [x]
		else:
			max = x.value
			return swapHelper(x.left, min, max)
	if x.right != None:
		if x.right.value > x.value and x.right.visited == False:
			x.right.visited = True
			return [x]
		elif x.right.value < min and x.right.visited == False:
			x.right.visited = True
			return [x]
		else:
			min = x.value
			return swapHelper(x.right, min, max)


def findSwappedSubtrees(x: BSTNode, min: int, max: int) -> List[Any]:
	# 1. Level order search
	# 2. Check for easy BST property violations
	# 3. For each node, update min and max and recurse

	first_subtree = swapHelper(x, float("-inf"), float("inf"))
	second_subtree = swapHelper(x, float("-inf", float("inf")))

	return first_subtree + second_subtree
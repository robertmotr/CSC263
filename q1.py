import typing

def swapHelper(x: BSTNode, min: int, max: int) -> List[Any]:
	# 1. In-order traversal on BST
	# 2. For each node, update min/max and check if it is violated
	if x.left != None and not x.left.visited:
		if x.left.value > x.value:
			return [x]
		elif x.value > max:
			return [x]
		else:
			max = x.value
			return swapHelper(x.left, min, max)
	if x.right != None and not x.right.visited:
		if x.right.value > x.value:
			return [x]
		elif x.right.value < min:
			return [x]
		else:
			min = x.value
			return swapHelper(x.right, min, max)


def findSwapped(x: BSTNode, min: int, max: int) -> List[Any]:
	# 1. Level order search
	# 2. Check for easy BST property violations
	# 3. For each node, update min and max and recurse

	left = swapHelper(x.left, float("-inf"), float("inf"))
	right = swapHelper(x.right, float("-inf", float("inf")))

	return left + right



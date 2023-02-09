def findSwappedSubtrees(x: BSTNode, min: int, max: int) -> List[BSTNode]:
	# 1. Level order search
	# 2. Check for easy BST property violations
	# 3. For each node, update min and max and recurse

	first_subtree = swapHelper(x, float("-inf"), float("inf"))
	second_subtree = swapHelper(x, float("-inf", float("inf")))

	return first_subtree + second_subtree
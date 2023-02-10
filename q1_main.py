def findSwappedSubtrees(x: BSTNode, min: int, max: int) -> List[BSTNode]:

	first_subtree = swapHelper(x, float("-inf"), float("inf"))
	second_subtree = swapHelper(x, float("-inf", float("inf")))

	return first_subtree + second_subtree
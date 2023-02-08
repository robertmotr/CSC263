import typing


def findSwappedHelper():
	


def findSwapped(x: BSTNode, min: Any, max: Any) -> List[Any]:
	# 1. Level order search
	# 2. Check for easy BST property violations
	# 3. For each node, update min and max and recurse


	left = []
	right = []
	if x.left != None:
		# If you go left, then the maximum value is the root (draw this out)
		max = x.value

		# Check for max/min violations for child
		if x.left.value > max:

	
		# Check for easy BST violations
		if x.left.value > x.value:
			left = [x.left]
		else:
			# No violations found, keep recursing
			left = findSwapped(x.left, min, max)
			right = findSwapped(x.left, min, max)
	if x.right != None:

		min = x.value

		if x.right.value > min:


	
		# Check for easy BST violations
		if x.right.value < x.value:
			right = [x.right]
		else:
			# No violations found, keep recursing
			left = findSwapped(x.left, min, max)
			right = findSwapped(x.left, min, max) 

	return left + right



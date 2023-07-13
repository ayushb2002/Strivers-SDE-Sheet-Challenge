def searchInBST(root, x):

	def trav(root):
		if not root:
			return False
		
		if root.data == x:
			return True
		elif root.data > x:
			return trav(root.left)
		else:
			return trav(root.right)

	return trav(root)
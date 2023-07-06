def getPreOrderTraversal(root):
	res = []

	def trav(root):
		if not root:
			return 
		
		res.append(root.data)
		trav(root.left)
		trav(root.right)

	trav(root)
	return res
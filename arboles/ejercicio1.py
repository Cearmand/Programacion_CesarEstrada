"""Ejercicio 1 busqueda binaria equilibrada utilizando elementos de una matriz donde los elemtos
de la matriz se ordenan en orden ascendente"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.rigth=None
def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid_val=len(nums)//2
    node=TreeNode(nums[mid_val])
    node.left=sorted_array_to_bst(nums[:mid_val])
    node.rigth=sorted_array_to_bst(nums[mid_val+1:])
    return node
def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.rigth)

result=sorted_array_to_bst([1,2,3,4,5,6,7])
preOrder(result)
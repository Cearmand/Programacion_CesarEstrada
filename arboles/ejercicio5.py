"""Convertir los elementos de una matriz determinada en un arbol de busqueda binaria equilibado en altura"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.right=None
def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num=len(array_nums)//2
    node=TreeNode(array_nums[mid_num])
    node.left=array_to_bst(array_nums[:mid_num])
    node.right=array_to_bst(array_nums[mid_num+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

array_nums=[1,2,3,4,5,6,7]
print("Array original: ")
print(array_nums)
result=array_to_bst(array_nums)
preOrder(preOrder(result))
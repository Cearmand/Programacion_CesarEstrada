"""Encontrar el valor mas cercano de un valor objetivo dado en un arbol
de busqueda binaria no vacio dado de valores unicos"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.rigth=None
def closest_value(root, target):
    a = root.val
    kid=root.left if target < a else root.rigth
    if not kid:
        return a
    b= closest_value(kid,target)
    return min((a,b),key=lambda x:abs(target-x))

root=TreeNode(8)
root.left=TreeNode(5)
root.rigth=TreeNode(14)
root.left.left=TreeNode(4)
root.left.rigth=TreeNode(6)
root.left.rigth.left=TreeNode(8)
root.left.rigth.rigth=TreeNode(7)
root.rigth.rigth=TreeNode(24)
root.rigth.rigth.left=TreeNode(22)

result=closest_value(root,19)
print(result)
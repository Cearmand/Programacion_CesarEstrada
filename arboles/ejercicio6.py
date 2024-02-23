"""Encontrar el k-ésimo elemento mas pequeño en un arbol de busqueda binario daro"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.right=None

def kth_smallest(root,k):
    stack=[]
    while root or stack:
        while root:
            stack.append(root)
            root=root.left
        root=stack.pop()
        k-=1
        if k==0:
            break
        root=root.right
    return root.val

root=TreeNode(8)
root.left=TreeNode(5)
root.rigth=TreeNode(14)
root.left.left=TreeNode(4)
root.left.rigth=TreeNode(6)
root.left.rigth.left=TreeNode(8)
root.left.rigth.rigth=TreeNode(7)
root.rigth.rigth=TreeNode(24)
root.rigth.rigth.left=TreeNode(22)

print(kth_smallest(root,2))
print(kth_smallest(root,3))
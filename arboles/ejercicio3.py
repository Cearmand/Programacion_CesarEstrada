"""Verifica si un arbol binario dado es un arbol de busqueda binaria valido o no"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.rigth=None
def is_bst(root):
    stack=[]
    prev=None
    while root or stack:
        while root:
            stack.append(root)
            root=root.left
        root=stack.pop()
        if prev and root.val<=prev.val:
            return False
        prev=root
        root=root.rigth
    return True
root=TreeNode(2)
root.rigth=TreeNode(5)
root.left=TreeNode(3)

result=is_bst(root)
print(result)

root=TreeNode(1)
root.rigth=TreeNode(2)
root.left=TreeNode(3)
result=is_bst(root)
print(result)
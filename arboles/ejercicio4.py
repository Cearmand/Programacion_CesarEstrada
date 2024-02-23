"""Elimina un nodo con la clave dada en un arbol de bisqueda binaria dado"""
class TreeNode(object):
    def __init__(self,x) -> None:
        self.val=x
        self.left=None
        self.rigth=None
def delete_Node(root,key):
    if not root:
        return root
    if root.val>key:
        root.left=delete_Node(root.left,key)
    elif root.val<key:
        root.rigth=delete_Node(root.rigth,key)
    else:
        if not root.rigth:
            return root.left
        if not root.left:
            return root.rigth
        temp_val=root.rigth
        mini_val=temp_val.val
        while temp_val.left:
            temp_val=temp_val.left
            mini_val=temp_val.val
    root.rigth=delete_Node(root.rigth,root.val)
    return root
def preOrder(node):
    if not node:
        return
    print(node.left)
    preOrder(node.left)
    preOrder(node.rigth)

root=TreeNode(5)
root.left=TreeNode(3)
root.rigth=TreeNode(6)
root.left.left=TreeNode(2)
root.left.rigth=TreeNode(4)
root.left.rigth.left=TreeNode(7)

print("Original node: ")
print(preOrder(root))
result=delete_Node(root,4)
print("Despues de eliminar el nodo: ")
print(preOrder(result))
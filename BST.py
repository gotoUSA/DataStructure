# Binary Search Tree

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BSTree:
    def __init__(self):
        self.root=None
        
    def __contains__(self,data):
        node=self.root
        while node:
            if node.data==data:
                return True
            elif node.data>data:
                node=node.left
            else:
                node = node.right
        return False
    
    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)
        res=[]
        _inorder(self.root)
        return res
    
    def _insert(self,node,data):
        if node is None:
            return Node(data)
        if node.data > data:
            node.left = self._insert(node.left,data)
        else:
            node.right=self._insert(node.right,data)
        return node
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
                    
    def _del_node1(self,del_node):
        if del_node.left:
            return del_node.left
        return del_node.right
    
    def _del_node2(self,del_node):
        parent=del_node
        leftmost=del_node.right
        while leftmost.left:
            parent=leftmost
            leftmost=leftmost.left
            
        del_node.data=leftmost.data
        
        if del_node == parent:
            parent.right=self._del_node1(leftmost)
        else:
            parent.left = self._del_node1(leftmost)
            
    def get_leftmost(self, node):
        while node.left:
            node = node.left
        return node
        
    def _delete(self,node,data):
        if node is None:
            return None
        
        if node.data>data:
            node.left = self._delete(node.left,data)
        elif node.data<data:
            node.right = self._delete(node.right,data)
        else:
            if node.left and node.right:
                leftmost=self.get_leftmost(node.right)
                node.data=leftmost.data
                node.right=self._delete(node.right, leftmost.data)
                return node
            elif node.left:
                return node.left
            else:
                return node.right
        return node
    
    def delete(self,data):
        self.root = self._delete(self.root, data)

def balancing(root):
    def _sort_nodes(node):
        if node is not None:
            _sort_nodes(node.left)
            nodes.append(node)
            _sort_nodes(node.right)
            
    def _balancing(left,right):
        if left>right:
            return None
        mid = (left+right) // 2
        node = nodes[mid]
        node.left = _balancing(left,mid-1)
        node.right = _balancing(mid+1,right)
        return node
    
    nodes=[]
    _sort_nodes(root)
    root = _balancing(0,len(nodes)-1)
    
if __name__ == "__main__":        
    bst = BSTree()
    for x in (8, 3, 10, 1, 6, 9, 12, 4, 5, 11):
        bst.insert(x)

    print(f"삭제 전 트리: {bst.inorder()}")
    bst.delete(10)
    print(f"10를 삭제 후: {bst.inorder()}")
    bst.delete(3)
    print(f"3을 삭제 후: {bst.inorder()}")
    bst.delete(8)
    print(f"8를 삭제 후: {bst.inorder()}")
    bst.insert(7)
    print(f"7을 삽입 후: {bst.inorder()}")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_blocks():
    blocks = []
    n = int(input("Скільки блоків ти хочеш ввести? "))
    for i in range(n):
        print(f"Введи блок {i + 1}:")
        block_id = input("  ID (напр. 0xabc): ").strip()
        view = int(input("  View (напр. 0): "))
        value = float(input("  Value (напр. 1.5): "))  
        blocks.append({'id': block_id, 'view': view, 'value': value})
    return blocks

def get_votes():
    votes = []
    m = int(input("Скільки голосів ти хочеш ввести? "))
    for i in range(m):
        print(f"Введи голос {i + 1}:")
        block_id = input("  ID блоку, за який проголосовано: ").strip()
        votes.append({'block_id': block_id})
    return votes

def extract_voted_ids(votes):
    return set(vote['block_id'] for vote in votes)

def build_chain(blocks, voted_ids):
    sorted_blocks = sorted(blocks, key=lambda x: x['view'])  
    chain = []

    for block in sorted_blocks:
        block_id = block['id']
        block_view = block['view']
        block_value = block['value']  

        if block_id not in voted_ids:
            continue

        if block_view == 0 and not chain:
            chain.append(block)
        elif chain and block_view == chain[-1]['view'] + 1:
            chain.append(block)

    return chain

def print_chain(chain):
    print("\n📦 Побудований ланцюг:")
    for block in chain:
        print(f"ID: {block['id']}, View: {block['view']}, Value: {block['value']}")

def insert_into_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def build_bst_from_chain(chain):
    root = None
    for block in chain:
        root = insert_into_bst(root, block['value'])  
    return root

def preorder(node):
    if node:
        print(node.value, end=' ')  
        preorder(node.left)       
        preorder(node.right)        

def inorder(node):
    if node:
        inorder(node.left)         
        print(node.value, end=' ')  
        inorder(node.right)      

def postorder(node):
    if node:
        postorder(node.left)      
        postorder(node.right)   
        print(node.value, end=' ') 

def is_complete_tree(root, index, node_count):
    if root is None:
        return True
    if index >= node_count:
        return False
    return (is_complete_tree(root.left, 2 * index + 1, node_count) and
            is_complete_tree(root.right, 2 * index + 2, node_count))

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def check_tree_type(root):
    node_count = count_nodes(root)
    if is_complete_tree(root, 0, node_count):
        print("Дерево є повним.")
    else:
        print("Дерево не є повним.")

def main():
    print("🔧 Введення блоків:")
    blocks = get_blocks()

    print("\n🗳️ Введення голосів:")
    votes = get_votes()

    voted_ids = extract_voted_ids(votes)
    chain = build_chain(blocks, voted_ids)

    print("\n📦 Побудований ланцюг:")
    print_chain(chain)

    
    bst_root = build_bst_from_chain(chain)

    
    check_tree_type(bst_root)

   
    print("\nОбхід дерева (Pre-order):")
    preorder(bst_root)
    print("\nОбхід дерева (In-order):")
    inorder(bst_root)
    print("\nОбхід дерева (Post-order):")
    postorder(bst_root)

if __name__ == "__main__":
    main()

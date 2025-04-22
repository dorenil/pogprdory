def get_blocks():
    blocks = []
    n = int(input("Скільки блоків ти хочеш ввести? "))
    for i in range(n):
        print(f"Введи блок {i + 1}:")
        block_id = input("  ID (напр. 0xabc): ").strip()
        view = int(input("  View (напр. 0): "))
        blocks.append({'id': block_id, 'view': view})
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
        print(f"ID: {block['id']}, View: {block['view']}")

def main():
    print("🔧 Введення блоків:")
    blocks = get_blocks()

    print("\n🗳️ Введення голосів:")
    votes = get_votes()

    voted_ids = extract_voted_ids(votes)
    chain = build_chain(blocks, voted_ids)
    print_chain(chain)

if __name__ == "__main__":
    main()


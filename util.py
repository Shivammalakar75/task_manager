def print_table(tasks):
    if not tasks:
        print("Task Not Found")
        return

    print("=" * 115)
    print(f"{'ID':<5} | {'TITLE':<30} | {'DESCRIPTION':<60} | {'STATUS':<10}")
    print("=" * 115)

    for t in tasks:
        desc = (
            t['description'][:57] + "..."
            if len(t['description']) > 60
            else t['description']
        )

        print(
            f"{t['id']:<5} | "
            f"{t['title']:<30} | "
            f"{desc:<60} | "
            f"{t['status']:<10}"
        )

    print("=" * 115)




def generate_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1
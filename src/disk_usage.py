# src/disk_usage.py

def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    # Handle None input
    if node is None:
        return 0

    # Handle file node
    if node.get("type") == "file":
        # Get size, defaulting to 0 if 'size' is missing
        return node.get("size", 0)

    # Handle directory node
    elif node.get("type") == "dir":
        total = 0
        # Recursively sum the sizes of all children
        for child in node.get("children", []):
            total += total_size(child)
        return total

    # Handle unknown node type (ignored)
    else:
        return 0

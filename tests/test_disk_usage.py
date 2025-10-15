import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.disk_usage import total_size

# ---- Normal (4) ----
def test_single_file():
    """Test a single file node."""
    f = {"type": "file", "name": "a.txt", "size": 10}
    assert total_size(f) == 10

def test_flat_dir():
    """Test a directory containing multiple files."""
    d = {"type": "dir", "name": "root", "children": [
        {"type": "file", "name": "a", "size": 5},
        {"type": "file", "name": "b", "size": 7},
    ]}
    assert total_size(d) == 12

def test_nested_dir_two_levels():
    """Test a simple nested directory structure."""
    d = {"type": "dir", "name": "root", "children": [
        {"type": "file", "name": "a", "size": 3},
        {"type": "dir", "name": "sub", "children": [
            {"type": "file", "name": "b", "size": 4},
            {"type": "file", "name": "c", "size": 8},
        ]}
    ]}
    assert total_size(d) == 15

def test_mixed_missing_size_defaults_zero():
    """Test files where 'size' key is missing, ensuring it defaults to 0."""
    d = {"type": "dir", "name": "root", "children": [
        {"type": "file", "name": "a"},  # missing size -> 0
        {"type": "file", "name": "b", "size": 2},
    ]}
    assert total_size(d) == 2

# ---- Edge (3) ----
def test_empty_dir():
    """Test a directory with no children."""
    d = {"type": "dir", "name": "empty", "children": []}
    assert total_size(d) == 0

def test_none_input():
    """Test handling of None input."""
    assert total_size(None) == 0

def test_unknown_type_ignored():
    """Test an unknown node type, which should be ignored (size 0)."""
    d = {"type": "weird", "name": "x"}
    assert total_size(d) == 0

# ---- Complex (3) ----
def test_deep_nesting_chain():
    """Test a deeply nested directory chain (for recursion depth)."""
    node = {"type": "file", "name": "end", "size": 1}
    for i in range(100):
        node = {"type": "dir", "name": f"d{i}", "children": [node]}
    assert total_size(node) == 1

def test_wide_tree_many_files():
    """Test a directory with many children (many files)."""
    d = {"type": "dir", "name": "root", "children": [
        {"type": "file", "name": str(i), "size": i} for i in range(50)
    ]}
    assert total_size(d) == sum(range(50))

def test_mixed_large_tree():
    """Test a large tree with nested directories and many files."""
    d = {"type": "dir", "name": "root", "children": []}
    total_expected = 0
    for j in range(5):
        sub = {"type": "dir", "name": f"s{j}", "children": [
            {"type": "file", "name": f"f{j}_{i}", "size": i} for i in range(10)
        ]}
        d["children"].append(sub)
        total_expected += sum(range(10))
    assert total_size(d) == total_expected

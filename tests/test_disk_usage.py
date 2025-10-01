from src.disk_usage import total_size

# ---- Normal (4) ----
def test_single_file():
    f = {"type": "file", "name": "a.txt", "size": 10}
    assert total_size(f) == 10

def test_flat_dir():
    d = {"type":"dir","name":"root","children":[
        {"type":"file","name":"a", "size":5},
        {"type":"file","name":"b", "size":7},
    ]}
    assert total_size(d) == 12

def test_nested_dir_two_levels():
    d = {"type":"dir","name":"root","children":[
        {"type":"file","name":"a","size":3},
        {"type":"dir","name":"sub","children":[
            {"type":"file","name":"b","size":4},
            {"type":"file","name":"c","size":8},
        ]}
    ]}
    assert total_size(d) == 15

def test_mixed_missing_size_defaults_zero():
    d = {"type":"dir","name":"root","children":[
        {"type":"file","name":"a"},  # missing size -> 0
        {"type":"file","name":"b","size":2},
    ]}
    assert total_size(d) == 2

# ---- Edge (3) ----
def test_empty_dir():
    d = {"type":"dir","name":"empty","children":[]}
    assert total_size(d) == 0

def test_none_input():
    assert total_size(None) == 0

def test_unknown_type_ignored():
    d = {"type":"weird","name":"x"}
    assert total_size(d) == 0

# ---- Complex (3) ----
def test_deep_nesting_chain():
    node = {"type":"file","name":"end","size":1}
    for i in range(100):
        node = {"type":"dir","name":f"d{i}","children":[node]}
    assert total_size(node) == 1

def test_wide_tree_many_files():
    d = {"type":"dir","name":"root","children":[
        {"type":"file","name":str(i),"size":i} for i in range(50)
    ]}
    assert total_size(d) == sum(range(50))

def test_mixed_large_tree():
    d = {"type":"dir","name":"root","children":[]}
    # add dirs with 10 files each
    for j in range(5):
        sub = {"type":"dir","name":f"s{j}","children":[
            {"type":"file","name":f"f{j}_{i}","size":i} for i in range(10)
        ]}
        d["children"].append(sub)
    assert total_size(d) == 5 * sum(range(10))

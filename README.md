[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/F_XAqDne)
e: “What’s Eating My SSD?”
README.md
# Disk Usage — What's Eating My SSD?

## Story
Your laptop’s SSD is gasping. You open your backup tool, which summarizes a directory tree as nested folders and files with sizes. Before you delete your thesis by mistake, you want a quick script that reports the **total size** of any nested directory structure.

## Technical Description
Write a recursive function:

```py
total_size(node) -> int
```

- node is either:

    - a file: {"type": "file", "name": "notes.txt", "size": 1234}

    - a directory: {"type": "dir", "name": "docs", "children": [<nodes>]}

Return the total of all file sizes contained in node. If node is a file, return its size. If node is a directory, sum total_size(child) for each child. Ignore unknown keys.

## Assumptions

- Sizes are nonnegative integers.

- Empty directories have children: [].

- Depth can be large; use recursion.

## Hints

- Base case: file → return size.

- Recursive case: directory → sum the sizes of children.

- Guard against None or missing keys by treating them as zero.

##Run Tests Locally
```py
python -m pytest -q
```

## Common Problems

- Forgetting the base case (treating files like dirs) → infinite recursion.

- Summing None because a child is malformed → coerce with or 0.

- Mutating input — unnecessary; just read fields.
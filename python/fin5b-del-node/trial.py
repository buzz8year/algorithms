def remove(root, val):
    if root is None:
        return None

    if val < root.value:
        root.left = remove(root.left, val)
        return root

    elif val > root.value:
        root.right = remove(root.right, val)
        return root

    if root.left is None and root.right is None:
        return None

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    succ_parent = root

    succ = root.right

    while succ.left is not None:
        succ_parent = succ
        succ = succ.left

    if succ_parent != root:
        succ_parent.left = succ.right
    else:
        succ_parent.right = succ.right

    root.value = succ.value

    return root

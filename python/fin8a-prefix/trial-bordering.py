def one_edit_distance(lhs, rhs):
    if len(lhs) - len(rhs) > 1:
        return False

    if len(lhs) > len(rhs):
        return one_edit_distance(rhs, lhs)

    lhs_pos = 0
    rhs_pos = 0
    one_diff = False
    while lhs_pos < len(lhs) and rhs_pos < len(rhs):
        if lhs[lhs_pos] != rhs[rhs_pos]:
            if one_diff:
                return False
            one_diff = True

            if len(lhs) == len(rhs):
                lhs_pos += 1
        else:
            lhs_pos += 1

        rhs_pos += 1

    return True


if __name__ == '__main__':
    lhs = input()
    rhs = input()
    print('OK' if one_edit_distance(lhs, rhs) else 'FAIL')

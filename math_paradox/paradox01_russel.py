

def check_is_belong_R(x):
    """
    检查 x 是不是一个应该属于 R 的元素
    如果 x 不在自己中，则是 R 的元素
    """
    return x not in x


if __name__ == '__main__':
    l1 = [1, 2, 3]
    print(f"{check_is_belong_R(l1) = }")

    l2 = [2, 1, 3]
    l2.append(l2)  # 包含自己
    print(f"{check_is_belong_R(l2) = }")

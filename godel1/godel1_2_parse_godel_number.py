from collections import defaultdict


def prime_factorization(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors


MAP = {
    1: r"\sim",  # 非
    2: r"\vee",  # 或
    3: r"\supset",  # 如果…则…
    4: r"\exists",  # 存在
    5: "=",  # 等于
    6: "0",  # 零
    7: "s",  # 后继
    8: "(",  # 左括号
    9: ")",  # 右括号
    10: ",",  # 逗号
    11: "+",  # 加
    12: r"\times",  # 乘
    13: "x",  # 变量 x
    15: "y",  # 变量 y
    17: "z",  # 变量 z
}

def parse_godel_number(godel_number: int) -> str:
    # 质因数分解
    primes = prime_factorization(godel_number)
    print("质因数分解：", primes)

    # 计算数量
    prime2cnt = defaultdict(int)
    for p in primes:
        prime2cnt[p] += 1

    tips = []
    label_list = []
    next_add = 0
    for prime, cnt in prime2cnt.items():
        tips.append(f"{prime}^{cnt}")
        label = MAP[cnt]
        if label == "s":
            next_add += 1
            continue
        elif label == "0":
            label = str(next_add)
            next_add = 0
        elif label != "0" and next_add == 1:
            label_list.append("s")
            next_add = 0

        label_list.append(label)

    print("计算过程：", "  x  ".join(tips))
    return " ".join(label_list)


if __name__ == '__main__':
    number = 23403180503121036356761714113406299710314692481511385567664956507146714708056647542459466306001890272956089036238639458469687500000000
    print("哥德尔数：", number)
    print("命题（latex）：", parse_godel_number(number))
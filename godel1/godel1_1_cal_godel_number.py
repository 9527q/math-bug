def generate_primes(n):
    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True

        for divisor in range(2, int(candidate ** 0.5) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

        candidate += 1

    return primes

MAP = {
    r"\sim": 1,  # 非
    r"\vee": 2,  # 或
    r"\supset": 3,  # 如果…则…
    r"\exists": 4,  # 存在
    "=": 5,  # 等于
    "0": 6,  # 零
    "s": 7,  # 后继
    "(": 8,  # 左括号
    ")": 9,  # 右括号
    ",": 10,  # 逗号
    "+": 11,  # 加
    r"\times": 12,  # 乘
    "x": 13,  # 变量 x
    "y": 15,  # 变量 y
    "z": 17,  # 变量 z
    "l": 19,  # 变量 l
    "m": 23,  # 变量 m
    "n": 29,  # 变量 n
    "p": 31,  # 变量 p
    "q": 37,  # 变量 q
    "r": 41,  # 变量 r
    "k": 43,  # 变量 k
    # 以下三个符号为自定义的，其实都可以转换为基本符号表示
    r"\wedge": 43,  # 并且
    "<": 47,  # 小于
    ">": 53,  # 大于
}


def convert_label(label: str) -> list[str]:
    label = label.strip()
    if not label:
        return []

    # 数字处理
    if label.isdigit():
        if label == "0":
            return ["0"]
        else:
            return ["s"] * int(label) + ["0"]

    # 检验有效性
    if label not in MAP:
        raise ValueError(f"error label: {label}")

    return [label]


def cal_godel_number(latex: str) -> int:
    labels = latex.strip("$").split(" ")
    labels = sum([convert_label(l) for l in labels], [])

    tips = []
    result = 1
    for i, base in enumerate(generate_primes(len(labels))):
        label_godel_number = MAP[labels[i]]
        result *= pow(base, label_godel_number)
        tips.append(f"{base}^{label_godel_number}")

    print(f"命题（Latex）：", latex)
    print("哥德尔数计算：", "  x  ".join(tips))

    return result



if __name__ == '__main__':
    latex = r"( s x = s y ) \supset ( x = y )"
    print("哥德尔数：", cal_godel_number(latex))

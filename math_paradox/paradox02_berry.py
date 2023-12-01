import random

def gen_random_int(length: int) -> int:
    """生成一个随机整数，位数为 length"""
    return random.randint(10**(length-1), 10**length-1)



if __name__ == '__main__':
    print(f"随便来一个一百位的数： {gen_random_int(100)}")


""

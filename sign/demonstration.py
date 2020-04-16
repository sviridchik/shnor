import math
import random

def eratosfen(number, filename, a):
    with open(filename, "w") as f:
        cur_number = a
        count = 0

        while cur_number <= number:
            flag = True
            for divider in range(2, int(math.ceil(math.sqrt(cur_number))) + 1):
                if cur_number % divider == 0:
                    flag = False
            if flag:
                count += 1
                f.write(str(cur_number))
                f.writelines("\n")
            cur_number += 1
        return count

def gen_simple_range(a, b, f):
    que = 0
    count = eratosfen(b, f, a)
    index = random.randint(1, count)
    with open(f, "r") as f:
        for nummber in f:
            que += 1
            if que == index:
                P = int(f.readline())
                return P


def issimple(cur_number):
    flag = True
    for divider in range(2, int(math.ceil(math.sqrt(cur_number))) + 1):
        if cur_number % divider == 0:
            flag = False
    return flag

def find_simple_dividers(number, flag):
    number -= 1
    for div in range(number, 1, -1):
        if number % div == 0:
            if issimple(div) and flag:
                return div



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def opppsite_for_module(G, W, P):
    a = G**W
    if gcd(a,P) != 1:
        print("bye")
        return
    else:
        fi = elier(P)-1
        return a**fi%P

def elier(a):
    count = 0
    answer = 1
    l = factorization(a)
    for key, value in l.items():
        answer *= key ** value - key ** (value - 1)
    return answer

def factorization(n):
    Ans = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            if d in Ans:
                Ans[d] += 1
            else:
                Ans[d] = 1
            n //= d
        else:
            d += 1
    if n > 1:
        if n in Ans:
            Ans[n] += 1
        else:
            Ans[n] = 1
    return Ans


if __name__ == "__main__":

        P = gen_simple_range(100,1000,"data1.txt")
        print("P = ", P)
        Q = find_simple_dividers(P,True)
        print("Q = ",Q)
        flag = True
        init_g = 10
        while flag:
            if ((init_g**Q)-1) % P == 0 or P % ((init_g**Q)-1) == 0:
                G = init_g
                flag = False
            init_g += 1
        print("G = ", G)
        W = gen_simple_range(3, Q - 1, "data1.txt")
        print("W = ", W)


        Y = opppsite_for_module(Q,W,P)
        print("Y = ", Y)
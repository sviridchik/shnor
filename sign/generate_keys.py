import math
import random


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



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


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


def eratosfen(number, filename, a):
    with open(filename, "w") as f:
        cur_number = a
        # cur_number = 1000
        count = 0

        while cur_number <= number:
            flag = True
            c = int(math.ceil(math.sqrt(cur_number)))
            for divider in range(2, int(math.ceil(math.sqrt(cur_number))) + 1):
                if cur_number % divider == 0:
                    flag = False
            if flag:
                # print(cur_number)
                count += 1
                f.write(str(cur_number))
                f.writelines("\n")
            cur_number += 1
        return count


def gen_simple_range(a, b, f):
    que = 0
    count = eratosfen(b, f, a)
    # print("hj"+str(count))
    index = random.randint(1, count)
    with open(f, "r") as f:
        for nummber in f:
            que += 1
            if que == index:
                P = int(f.readline())
                return P


# GG = opppsite_for_module()
if __name__ == "__main__":

        P = gen_simple_range(100,1000,"data.txt")

        print("P = ",P)
        Q = find_simple_dividers(P,True)
        print("Q = ",Q)

        #find all dividers p
        # dividers_p = []
        # for div in range(2,P-1):
        #     if (P-1)%div == 0:
        #         dividers_p.append(div)

        flag = True
        init_g = 10
        while flag:
            if ((init_g**Q)-1) % P == 0 or P % ((init_g**Q)-1) == 0:
                G = init_g
                flag = False
            init_g += 1


        print("G = ", G)
        W = gen_simple_range(3, Q-1, "data1.txt")
        print("W = ",W)

        #print(factorization(18))

        Y = opppsite_for_module(2132,5,14301)
        print("Y = ", Y)
##############################################
        r = gen_simple_range(3, Q - 1, "data1.txt")
        print("r = ",r)
        x =(G**r)%P
        # x = (354 ** 11) % 2267
        print("x = ",x)
        m = random.randint(1,500)
        print("M = ", m)
        s1 = 200
        # s2 = 11 + (30 * s1) % 103
        s2 = r+(W*s1)%Q
        print(s2)


print(opppsite_for_module(58,2,61))
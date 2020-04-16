from generate_keys import *

import hashlib


if __name__ == "__main__":

        P = gen_simple_range(100,1000,"data.txt")

        print("P = ",P)
        Q = find_simple_dividers(P,True)
        print("Q = ",Q)

        #find all dividers p
        dividers_p = []
        for div in range(2,P-1):
            if (P-1)%div == 0:
                dividers_p.append(div)

        flag = True
        while flag:
            init_g = 10
            if ((init_g**Q)-1) % P == 0 or P % ((init_g**Q)-1):
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



from lib2to3.pgen2.token import LEFTSHIFT
from turtle import left
from tables import SHIFT, PC1, PC2


class Key:
    def __init__(self, _key):
        self.round = 0
        self.key = _key

        self.preprocessing()

    def preprocessing(self):
        key_n = []

        for ind in PC1:
            key_n.append(self.key[ind-1])

        self.key = key_n

        self.Lk = key_n[:28]
        self.Rk = key_n[28:]

    def inverse_transformation(self):
        res = []
        for ind in PC2:
            if ind < 29:
                res.append(self.Lk[ind-1])
            else:
                res.append(self.Rk[ind-29])

        return res

    def leftShift(self, key, ind):
        if ind > len(key):
            raise "The ind can't be greater than the length of the key"
        lft = key[0:ind]
        rgt = key[ind:]
        return rgt+lft

    def roundKey(self):
        if self.round >= 16:
            raise "You have passed the limit for rounds exist in des"

        # print("Round Key for:-", self.round)
        self.Lk = self.leftShift(self.Lk, SHIFT[self.round])
        self.Rk = self.leftShift(self.Rk, SHIFT[self.round])

        self.round += 1
        ki = self.inverse_transformation()
        # print(ki)
        # Subkeys are ok
        return ki

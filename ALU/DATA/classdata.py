class Alu:
    def xor(a, b):
        Flag = a or b
        dataNum = False
        c = False
        l = [i for i in range(2)]
        if a == b:
            c = True
        else:
            dataNum = True
        if not Flag:
            c = False
        l[0] = int(c)
        l[1] = int(dataNum)
        return l

    def s_xor(a, b):
        Flag = False
        strings1 = list(map(int, str(a)))
        strings2 = list(map(int, str(b)))
        k = []
        if (len(strings1) - len(strings2)) < False:
            Flag = not Flag
        if Flag:
            for i in range(len(strings1)):
                l = [i for i in range(2)]
                l = Alu.xor(strings1[i], strings2[i])
                c = bool(l[0])
                dataNum = bool(l[1])
                k.append(dataNum + c)
        else:
            for i in range(len(strings2)):
                l = [i for i in range(2)]
                l = Alu.xor(strings1[i], strings2[i])
                c = bool(l[0])
                dataNum = bool(l[1])
                k.append(dataNum + c)
        k.append(0)
        return k

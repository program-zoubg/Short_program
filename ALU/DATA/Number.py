def maps(li):
    k = 0
    wei = 1
    for n in range(len(li)):
        if li[n] == 0:
            k *= wei
            continue
        k += wei * li[n]
        wei *= 10
    return k

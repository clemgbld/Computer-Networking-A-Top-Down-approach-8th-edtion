def rsa_d(e, z):
    d = 1
    while True:
        if (e * d - 1) % z == 0:
            return d
        d += 1


print(rsa_d(3, 40))

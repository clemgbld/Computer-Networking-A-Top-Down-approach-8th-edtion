def internet_checksum(payload):
    length = len(payload)
    i = 0
    sum = 0
    while i < length:
        if i + 1 >= length:
            sum = wrap_arround(
                sum
                + int(
                    f"{payload[i].encode('ascii').hex()}00",
                    16,
                )
            )
            i += 1
            continue
        sum = wrap_arround(
            sum
            + int(
                f"{payload[i].encode('ascii').hex()}{payload[i + 1].encode('ascii').hex()}",
                16,
            )
        )
        i += 2

    return ~sum & 0xFFFF


def wrap_arround(checksum):
    while checksum > 0xFFFF:
        carry = checksum >> 16
        remainder = checksum & 0xFFFF
        checksum = remainder + carry

    return checksum


print("Internet:")
print(hex(internet_checksum("Internet")))


print("binary reprensentation 1 - 10:")
print(hex(internet_checksum("12345678910")))

print("the ascii representation of the letter B - K")

print(hex(internet_checksum("BCDEFJHIJK")))


print("the ascii representation of the letter b - k")


print(hex(internet_checksum("bcdefjhijk")))

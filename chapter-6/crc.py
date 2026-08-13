def crc(D, G):
    r_bits = int(D[: len(G)], 2)
    g_bits = int(G, 2)
    r = "0" * (len(G) - 1)
    bits_to_iterate_on = (D + r)[len(G) :]

    bits_table = to_bits_table(len(G))
    i = 0

    while i < len(bits_to_iterate_on):
        r_bits ^= g_bits
        if r_bits == 0:
            r_bits = int(
                bits_to_iterate_on[i : i + min(len(G), len(bits_to_iterate_on) - i)], 2
            )
            i += len(G)
            continue

        if r_bits >= bits_table[0]:
            continue

        leading_zeros = min(
            get_leading_zeros(bits_table, r_bits), len(bits_to_iterate_on) - i
        )
        bits_to_add = int(bits_to_iterate_on[i : i + leading_zeros], 2)
        r_bits = r_bits << leading_zeros
        r_bits |= bits_to_add
        i += leading_zeros

    while r_bits >= g_bits:
        r_bits ^= g_bits

    return r_bits


def to_bits_table(length):
    table = []
    for _ in range(length):
        if len(table) == 0:
            table.append(1)
        else:
            table.append(table[len(table) - 1] * 2)
    table.reverse()
    return table


def get_leading_zeros(bits_table, bits):
    leading_zeros = 0
    for bit_value in bits_table:
        if bits >= bit_value:
            break
        leading_zeros += 1
    return leading_zeros

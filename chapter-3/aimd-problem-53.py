import math


def aimd(c1_seg, c2_seg, time, next_tick):
    if time > 2.2:
        return
    rate1 = c1_seg / 0.1
    rate2 = c2_seg / 0.1
    total = c1_seg + c2_seg
    if total > 30:
        return aimd(
            max(1, math.floor(c1_seg / 2)),
            max(1, math.floor(c2_seg / 2)),
            time,
            next_tick,
        )
    print(
        str(c1_seg)
        + "    |"
        + str(c2_seg)
        + "   |"
        + str(rate1)
        + "    |"
        + str(rate2)
        + "    |"
        + str(time)
        + "    |"
        + str(total)
    )

    new_time = time + 0.1
    return aimd(
        c1_seg + 1,
        c2_seg + 1,
        new_time,
        next_tick + 1,
    )


print("cwnd1     |cwnd 2     |rate 1      |rate 2     |time     |total   ")
aimd(15, 10, 0, 0)

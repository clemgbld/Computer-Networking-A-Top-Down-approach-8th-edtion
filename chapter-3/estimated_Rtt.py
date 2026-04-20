def cal_estimated_RTT(initial_estimated_RTT, initial_dev_RTT, samples_RTT):
    estimated_RTT = initial_estimated_RTT
    dev_rtt = initial_dev_RTT
    for sample_RTT in samples_RTT:
        dev_rtt = (1 - 0.25) * dev_rtt + 0.25 * abs(sample_RTT - estimated_RTT)
        print("Dev RTT " + str(dev_rtt) + " ms")
        estimated_RTT = 0.875 * estimated_RTT + 0.125 * sample_RTT
        print("Estimated RTT: " + str(estimated_RTT) + " ms")
        timeout_interval = estimated_RTT + 4 * dev_rtt
        print("Timeout interval " + str(timeout_interval) + " ms")
        print("")
    print("Final estimated RTT: " + str(estimated_RTT) + " ms")


cal_estimated_RTT(100, 5, [106, 120, 140, 90, 115])

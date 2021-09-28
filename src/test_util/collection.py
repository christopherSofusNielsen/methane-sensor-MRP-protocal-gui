import numpy as np


def generateData(length):
    values = []
    values_hex = []

    for i in range(length):
        val = np.random.randint(0, 60000)
        values.append(val)
        values_hex.append(hex((val >> 8) & 255))
        values_hex.append(hex(val & 255))

    print(values)
    prittyPrintHex(values_hex)


def prittyPrintHex(hex_vals):
    vals_str = ""
    for val in hex_vals:
        vals_str += ", "+val
    print(vals_str)


generateData(20)

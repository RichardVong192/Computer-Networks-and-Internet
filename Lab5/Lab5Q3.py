import math
def number_fdma_channels (b_hz, g_hz, u_hz):
    thing = b_hz - g_hz
    result = math.floor(thing / (g_hz + u_hz))
    return result

print (number_fdma_channels(1000000, 1000, 30000))
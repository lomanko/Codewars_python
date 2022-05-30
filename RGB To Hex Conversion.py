# The rgb function is incomplete. 
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

#The following are examples of expected output values:

#rgb(255, 255, 255) # returns FFFFFF
#rgb(255, 255, 300) # returns FFFFFF
#rgb(0,0,0) # returns 000000
#rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    symbols = '0123456789ABCDEF'
    hex_16 = []
    initial_rgb = [r,g,b]
    for colour in initial_rgb:
        hex_colour = ''
        if colour > 255:
            hex_16.append('FF')
        else:
            while  colour > 0:
                hex_colour = symbols[colour % 16] + hex_colour
                colour = colour // 16
            hex_16.append(hex_colour)
    
    index = 0
    for colour in hex_16:
        if len(colour) == 0: hex_16[index] = '00'
        if len(colour) == 1: hex_16[index] = '0' + hex_16[index]
        index += 1

    return "".join(hex_16)
""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

NAME : Jephthah Kwame Mensah (jkm255)
DATE : October 3rd, 2022
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB objec#t
    """
    #Get the values of the attributes red, green, blue
    red = rgb.red
    green = rgb.green
    blue = rgb.blue

    #Get the complements of the attributes
    red = 255 - red
    green = 255- green
    blue = 255 - blue

    #Correction made
    #Use the complements to modify the rgb
    #rgb.red = red
    #rgb.green = green
    #rgb.blue = blue
    #return introcs.RGB(rgb.red, rgb.green, rgb.blue)

    #Correction made
    cmp = introcs.RGB(red, green, blue)
    return cmp


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    
    str_value = str(value)

    #for arguments with exponent
    if 'e' in str_value:
        desired_string = '0.000'
    
    else:
        str_len = len(str_value)
        number_xzeros = 5-str_len

    #for arguments with number of characters less than 6
        if number_xzeros >= 0:
            if '.' in str_value:
                desired_string = str_value + number_xzeros*'0'
            else:
                desired_string = str_value + '.' + (number_xzeros-1)*'0'

    #for arguments with number of characters more than 5
        else:
            len_b4_dp1 = len(str_value[: (str_value.index('.')+1)])
            rounded_str = str(round(float(str_value), 5 - len_b4_dp1))
            number_xzeros = 5 - len(rounded_str)

            if number_xzeros >= 0:
                desired_string = rounded_str + number_xzeros*'0'
            else:
                desired_string = rounded_str
    
    return desired_string


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    c = str5(cmyk.cyan)
    m = str5(cmyk.magenta)
    y = str5(cmyk.yellow)
    k = str5(cmyk.black)

    desired_string = f"({c}, {m}, {y}, {k})"
    return desired_string


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    h = str5(hsv.hue)
    s = str5(hsv.saturation)
    v = str5(hsv.value)

    desired_string = f"({h}, {s}, {v})"
    return desired_string


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    
    #Jephthah's code
    r = rgb.red
    g = rgb.green
    b = rgb.blue

    #divide each of r, g, b by 255
    r = r/255.0
    g = g/255.0
    b = b/255.0
    #first compute k = 1 - max(r, g, b)
    k = 1 - max(r, g, b)
    #compute the other colors if k is not 1
    if k != 1:
        #compute c = (1- r - k)/( 1 - k)
        c = (1- r - k)/( 1 - k)
        #compute m = (1 - g - k)/(1 - k)
        m = (1 - g - k)/(1 - k)
        #compute y = (1 - b - k)/(1 - k)
        y = (1 - b - k)/(1 - k)
    else:
        #if k is 1, then c = 0, m = 0, y = 0
        c = 0
        m = 0
        y = 0

    cmyk = introcs.CMYK(c*100.0, m*100.0, y*100.0, k*100.0)
    return cmyk


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    
    #Jephthah's code
    c = cmyk.cyan
    m = cmyk.magenta
    y = cmyk.yellow
    k = cmyk.black

    #divide each of c, m, y, k by 100.0
    c = c/100.0
    m = m/100.0
    y = y/100.0
    k = k/100.0

    #compute r = (1 - c)(1 - k)
    r = (1 - c)*(1 - k)
    
    #compute g = (1 - m)(1 - k)
    g = (1 - m)*(1 - k)

    #compute b = (1 - y)(1 - k)
    b = (1 - y)*(1 - k)

    #convert r, g, b to ints in the range (0...255)
    r = round( r*255.0)
    g = round( g*255.0)
    b = round( b*255.0)

    rgb = introcs.RGB(r, g, b)
    return rgb


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    #Jephthah's code
    r = rgb.red
    g = rgb.green
    b = rgb.blue

    #divide each of r, g, b by 255.0
    r = r/255.0
    g = g/255.0
    b = b/255.0

    #get max, maximum of (r, g, b)
    mx = max(r, g, b)

    #get min, minimum of (r, g, b)
    mn = min(r, g, b)

    #compute v = max
    v = mx

    #compute h
    # h = 0, if max = min
    if mx == mn:
        h = 0
    # h = 60.0*(g - b)/(max - min) if max = r and g>=b
    elif (mx == r and g >= b):
        h = 60.0*(g - b)/(mx - mn)
    # h = 60.0*(g - b)/(max - min) + 360.0 if max = r and g<b
    #Correction made
    elif (mx == r and g<b):
        h = 60.0*(g - b)/(mx - mn) + 360.0
    # h = 60.0*(b - r)/(max - min) + 120.0 if max = g
    elif mx == g:
        h = 60.0*(b - r)/(mx - mn) + 120.0
    # h = 60.0*(r - g)/(max - min) + 240.0 if max = b
    elif mx == b:
        h = 60.0*(r - g)/(mx - mn) + 240.0

    # compute s
    # s = 0 if max = 0
    if mx == 0:
        s = 0
    # s = 1-min/max if otherwise
    else:
        s = 1 - mn/mx

    hsv = introcs.HSV(h, s, v)
    return hsv


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    #Jephthah's code
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value

    #compute hi, f, p, q, t
    hi = math.floor(h/60)
    f = (h/60) -hi
    p = v*(1 - s)
    q = v*(1- f*s)
    t = v*(1 - (1 - f)*s)

    #compute r

    #r = v if hi == 0 or 5
    if hi == 0 or hi == 5:
        r = v
    #r = q if hi == 1
    elif hi == 1:
        r = q
    #r = p if hi == 2 or 3
    elif hi == 2 or hi == 3:
        r = p
    #r = t if hi == 4
    elif hi == 4:
        r = t

    #compute g

    #g = t if hi == 0
    if hi == 0:
        g = t
    #g = v if hi == 1 or 2
    elif hi == 1 or hi == 2:
        g = v
    #g = q if hi == 3
    elif hi == 3:
        g = q
    #g = p if hi == 4 or 5
    elif hi == 4 or 5:
        g = p

    #compute b

    #b = p if hi== 0 or 1
    if hi== 0 or hi == 1:
        b = p
    #b = t if hi == 2
    elif hi == 2:
        b = t
    #b = v if hi == 3 or 4
    elif hi == 3 or hi == 4:
        b = v
    #b = q if hi == 5
    elif hi == 5:
        b = q

    r = round(r*255.0)
    g = round(g*255.0)
    b = round(b*255.0)

    rgb = introcs.RGB(r, g, b)
    return rgb  


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    #Jephthah's code
    #get the values of c and x
    c = contrast
    x = value
    #compute the value of y

    if c <1  and c>= -1 :
        if x < (0.25 + 0.25*c):
            y = ((1-c)/(1+c))*x 
        elif x>(0.75 -0.25*c):
            y = ((1-c)/(1+c))*(x - (3-c)/4)+ ((3+c)/4)
        else:   
            y = ((1+c)/(1-c))*(x - (1+c)/4)+ ((1-c)/4) 
    elif c == 1:
        if x >= 0.5:
            y = 1
        else:
            y = 0
    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    #Jephthaht's code's
    r = rgb.red
    g = rgb.green
    b = rgb.blue

    #Divide each of r, g, b with 255
    r = r/255
    g = g/255
    b = b/255
    #Apply contrast
    r = contrast_value(r, contrast)
    g = contrast_value(g, contrast)
    b = contrast_value(b, contrast)
    #Multiply each of r, g, b with 255 and round
    r = round(r*255)
    g = round(g*255)
    b = round(b*255)
    #Modify rgb with contrast outputs
    rgb.red, rgb.green, rgb.blue = r, g, b
    

    
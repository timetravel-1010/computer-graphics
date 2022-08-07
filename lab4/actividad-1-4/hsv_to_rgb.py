from aifc import Error
# Formula para convertir de RGB a HSV
'''def rgb_to_hsv(r, g, b): 
  r /= 255
  g /= 255 
  b /= 255 
    maxc = max(r, g, b) 
   minc = min(r, g, b) 
  v = maxc 
      if minc == maxc: return 0.0, 0.0, v 
         s = (maxc-minc) / maxc 
         rc = (maxc-r) / (maxc-minc) 
         gc = (maxc-g) / (maxc-minc) 
         bc = (maxc-b) / (maxc-minc) 
                if r == maxc: 
        h = 0.0+bc-gc 
                   elif g == maxc:
        h = 2.0+rc-bc 
                     else: h = 4.0+gc-rc 
            h = (h/6.0) % 1.0 
                      return h * 360, s * 100, v * 100'''
        
# Formula para convertir de HSV a RGB 
def hsv_to_rgb(h, s, v):
    """Esta función se encarga de transformar de hsv a rgb
        debe tener en cuenta lo siguiente: 0 <= H <= 360, 0 <= s <= 1, 0 <= v <= 1"""
        
    if not (0 <= h and h <= 360 and 0 <= s 
        and s <= 100 and 0 <= v and v <= 100):
        raise Error("Debe cumplir: 0 <= H <= 360, 0 <= s <= 1, 0 <= v <= 1")

    s=s/100
    v=v/100

    c = v*s
    x = c * (1 - abs((h/60)%2-1))
    m = v - c

    if h < 60:
        (r1, g1, b1) = (c, x, 0)
    elif h < 120:
        (r1, g1, b1) = (x, c, 0)
    elif h < 180:
        (r1, g1, b1) = (0, c, x)
    elif h < 240:
        (r1, g1, b1) = (0, x, c)
    elif h < 300:
        (r1, g1, b1) = (x, 0, c)
    else:
        (r1, g1, b1) = (c, 0, x)

    return (round((r1+m)*255), round((g1+m)*255), round((b1+m)*255))

print(hsv_to_rgb(360, 80, 60)) #(h, %, %)

# Formula para convertir de RGB a CMY
def rgb_a_cmy(r, g, b):
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    return (c, m, y)

print(rgb_a_cmy(r, g, b))

# Formula para convertir de CMY a RGB
def cmy_a_rgb(c, m, y):
    r = 1 - c
    g = 1 - m
    b = 1 - y
    return (r, g, b)

print(cmy_a_rgb(c, m, y))

# Formula para convertir de RGB a HLS
def rgb_a_hsl(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3

    if high == low:
        h = 0.0
        s = 0.0
    else:
        d = high - low
        s = d / (2 - high - low) if l > 0.5 else d / (high + low)
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return h, s, v

# Formula para convertir de HLS a RGB
def hsl_a_rgb(h, s, l):
    def hue_a_rgb(p, q, t):
        t += 1 if t < 0 else 0
        t -= 1 if t > 1 else 0
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: p + (q - p) * (2/3 - t) * 6
        return p

    if s == 0:
        r, g, b = l, l, l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_a_rgb(p, q, h + 1/3)
        g = hue_a_rgb(p, q, h)
        b = hue_a_rgb(p, q, h - 1/3)

    return r, g, b


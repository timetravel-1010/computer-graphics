from aifc import Error

def rgb_to_hsv(r, g, b): 
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
            return h * 360, s * 100, v * 100

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

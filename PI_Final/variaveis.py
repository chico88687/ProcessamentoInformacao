import random
import math


def our_Random(min: int, max: int):
    if (max > min):
        res = min + (max - min) * random.random()
        #   # print("our randon = ", res)
        return res


def define_platafromX():
    return our_Random(0, 200)


# A y estará de acordo com a altura q o personagem pode pular
def define_plataformY(yMin: float, yMax: float, media: float):
    if (yMax > yMin and yMin <= media and yMax >= media):
        p = our_Random(0, 1)
        q = 1 - p
        if (p <= (media - yMin) / (yMax - yMin)):
            x = yMin + math.sqrt((yMax - yMin) * (media - yMin) * p)
        else:
            x = yMax - math.sqrt((yMax - yMin) * (yMax - media) * q);
        return x


def discret(list):
    px = int(our_Random(0, 100))
    if (px > 50):
        return list[3]
    elif (25 <= px <= 50):
        return list[2]
    elif (10 < px < 25):
        return list[1]
    else:
        return list[0]


def enemy_X(x_min:int, x_max:int):
    res = our_Random(x_min, x_max)
    return res


def enemy_Y(l: int, p_inim: int):
    x = our_Random(0, 1200)
    res = (l * math.exp(-l * x)) + p_inim
    # print("enemy_y = ", res )
    return res


# def velocidade_lava(vel):
#     px = our_Random(0, 100)
#     if (px > 50):
#         return vel[3]
#     elif (25 < px <= 50):
#         return vel []


print("define y= ", define_plataformY(0, 20, 10))

# y = (1 / (math.sqrt(2 * math.pi) * desv) * math.exp(- math.pow((x - media), 2) / 2 * math.pow(desv, 2)))

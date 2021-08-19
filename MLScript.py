from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt


# plt.rcParams['toolbar'] = 'None'
def perforation_check():
    if '-T' in profile:
        if width == 102:  # 2holes
            coordX1 = int(-75)
            coordX2 = int(0)
            coordX12 = int(-25)
            coordX22 = int(50)

            holeX1 = array([coordX1, coordX2])
            holeY1 = array([82, 82])
            holeX3 = array([coordX1, coordX2])
            holeY3 = array([108, 108])

            holeX2 = array([coordX12, coordX22])
            holeY2 = array([95, 95])
            holeX4 = array([coordX12, coordX22])
            holeY4 = array([120, 120])

            coordX1_neg = int(-75)
            coordX2_neg = int(0)
            coordX12_neg = int(-25)
            coordX22_neg = int(50)

            holeX1_neg = array([coordX1_neg, coordX2_neg])
            holeY1_neg = array([-82, -82])
            holeX3_neg = array([coordX1_neg, coordX2_neg])
            holeY3_neg = array([-108, -108])

            holeX2_neg = array([coordX12_neg, coordX22_neg])
            holeY2_neg = array([-95, -95])
            holeX4_neg = array([coordX12_neg, coordX22_neg])
            holeY4_neg = array([-120, -120])

            n = length // 100
            for i in range(0, n - 1):
                width_102(holeX1, holeY1, holeX2, holeY2, holeX3, holeY3, holeX4, holeY4, holeX1_neg, holeY1_neg,
                          holeX2_neg, holeY2_neg, holeX3_neg, holeY3_neg, holeX4_neg,
                          holeY4_neg, i)
            plot(x, y, 'k-', x1, y1, 'k-', r1, r2, 'k-', r11, r12, 'k-', r13, r14, 'k-', arrow11, arrow12, 'k-',
                 arrow21, arrow22, 'k-', holeX1, holeY1, 'k-', holeX2, holeY2, 'k-', holeX3, holeY3, 'k-', holeX4,
                 holeY4, 'k-', holeX1_neg, holeY1_neg, 'k-',
                 holeX2_neg, holeY2_neg, 'k-', holeX3_neg, holeY3_neg, 'k-', holeX4_neg,
                 holeY4_neg, 'k-')

        elif width == 152:  # 6holes
            coordX1 = int(-75)
            coordX2 = int(0)
            coordX12 = int(-25)
            coordX22 = int(50)

            holeX1 = array([coordX1, coordX2])
            holeY1 = array([96, 96])
            holeX3 = array([coordX1, coordX2])
            holeY3 = array([120, 120])
            holeX5 = array([coordX1, coordX2])
            holeY5 = array([143, 143])

            holeX2 = array([coordX12, coordX22])
            holeY2 = array([107, 107])
            holeX4 = array([coordX12, coordX22])
            holeY4 = array([132, 132])
            holeX6 = array([coordX12, coordX22])
            holeY6 = array([154, 154])

            coordX1_neg = int(-75)
            coordX2_neg = int(0)
            coordX12_neg = int(-25)
            coordX22_neg = int(50)

            holeX1_neg = array([coordX1_neg, coordX2_neg])
            holeY1_neg = array([-96, -96])
            holeX3_neg = array([coordX1_neg, coordX2_neg])
            holeY3_neg = array([-120, -120])
            holeX5_neg = array([coordX1_neg, coordX2_neg])
            holeY5_neg = array([-143, -143])

            holeX2_neg = array([coordX12_neg, coordX22_neg])
            holeY2_neg = array([-107, -107])
            holeX4_neg = array([coordX12_neg, coordX22_neg])
            holeY4_neg = array([-132, -132])
            holeX6_neg = array([coordX12_neg, coordX22_neg])
            holeY6_neg = array([-154, -154])

            # SA-152-1.2-TU-OUT
            n = length // 100
            for i in range(0, n - 1):
                width_152(holeX1, holeY1, holeX2, holeY2, holeX3, holeY3, holeX4, holeY4, holeX5, holeY5, holeX6,
                          holeY6, holeX1_neg, holeY1_neg, holeX2_neg, holeY2_neg, holeX3_neg, holeY3_neg, holeX4_neg,
                          holeY4_neg, holeX5_neg, holeY5_neg, holeX6_neg, holeY6_neg, i)
            plot(x, y, 'k-', x1, y1, 'k-', r1, r2, 'k-', r11, r12, 'k-', r13, r14, 'k-', arrow11, arrow12, 'k-',
                 arrow21, arrow22, 'k-', holeX1, holeY1, 'k-', holeX2, holeY2, 'k-', holeX3, holeY3, 'k-', holeX4,
                 holeY4, 'k-', holeX5, holeY5, 'k-', holeX6, holeY6, 'k-', holeX1_neg, holeY1_neg, 'k-',
                 holeX2_neg, holeY2_neg, 'k-', holeX3_neg, holeY3_neg, 'k-', holeX4_neg,
                 holeY4_neg, 'k-', holeX5_neg, holeY5_neg, 'k-', holeX6_neg, holeY6_neg, 'k-')
            # for i in range(,n-1)
        elif width == 203:  # 8holes
            coordX1 = int(-75)
            coordX2 = int(0)
            coordX12 = int(-25)
            coordX22 = int(50)

            holeX1 = array([coordX1, coordX2])
            holeY1 = array([108, 108])
            holeX3 = array([coordX1, coordX2])
            holeY3 = array([132, 132])
            holeX5 = array([coordX1, coordX2])
            holeY5 = array([155, 155])
            holeX7 = array([coordX1, coordX2])
            holeY7 = array([177, 177])

            holeX2 = array([coordX12, coordX22])
            holeY2 = array([119, 119])
            holeX4 = array([coordX12, coordX22])
            holeY4 = array([144, 144])
            holeX6 = array([coordX12, coordX22])
            holeY6 = array([166, 166])
            holeX8 = array([coordX12, coordX22])
            holeY8 = array([188, 188])

            coordX1_neg = int(-75)
            coordX2_neg = int(0)
            coordX12_neg = int(-25)
            coordX22_neg = int(50)

            holeX1_neg = array([coordX1_neg, coordX2_neg])
            holeY1_neg = array([-108, -108])
            holeX3_neg = array([coordX1_neg, coordX2_neg])
            holeY3_neg = array([-132, -132])
            holeX5_neg = array([coordX1_neg, coordX2_neg])
            holeY5_neg = array([-155, -155])
            holeX7_neg = array([coordX1_neg, coordX2_neg])
            holeY7_neg = array([-177, -177])

            holeX2_neg = array([coordX12_neg, coordX22_neg])
            holeY2_neg = array([-119, -119])
            holeX4_neg = array([coordX12_neg, coordX22_neg])
            holeY4_neg = array([-144, -144])
            holeX6_neg = array([coordX12_neg, coordX22_neg])
            holeY6_neg = array([-166, -166])
            holeX8_neg = array([coordX12_neg, coordX22_neg])
            holeY8_neg = array([-188, -188])

            # SA-203-1.2-TU-OUT
            n = length // 100
            for i in range(0, n - 1):
                width_203(holeX1, holeY1, holeX2, holeY2, holeX3, holeY3, holeX4, holeY4, holeX5, holeY5, holeX6,
                          holeY6, holeX7, holeY7, holeX8, holeY8, holeX1_neg, holeY1_neg, holeX2_neg, holeY2_neg,
                          holeX3_neg, holeY3_neg, holeX4_neg,
                          holeY4_neg, holeX5_neg, holeY5_neg, holeX6_neg, holeY6_neg, holeX7_neg, holeY7_neg,
                          holeX8_neg, holeY8_neg, i)
            plot(x, y, 'k-', x1, y1, 'k-', r1, r2, 'k-', r11, r12, 'k-', r13, r14, 'k-', arrow11, arrow12, 'k-',
                 arrow21, arrow22, 'k-', holeX1, holeY1, 'k-', holeX2, holeY2, 'k-', holeX3, holeY3, 'k-', holeX4,
                 holeY4, 'k-', holeX5, holeY5, 'k-', holeX6, holeY6, 'k-', holeX7, holeY7, 'k-', holeX8, holeY8, 'k-',
                 holeX1_neg, holeY1_neg, 'k-', holeX2_neg, holeY2_neg, 'k-', holeX3_neg, holeY3_neg, 'k-', holeX4_neg,
                 holeY4_neg, 'k-', holeX5_neg, holeY5_neg, 'k-', holeX6_neg, holeY6_neg, 'k-', holeX7_neg, holeY7_neg,
                 'k-', holeX8_neg, holeY8_neg, 'k-')
        elif width == 254 or width == 305:  # 10 holes
            if width == 254:
                coordX1 = int(-75)
                coordX2 = int(0)
                coordX12 = int(-25)
                coordX22 = int(50)

                holeX1 = array([coordX1, coordX2])
                holeY1 = array([120, 120])
                holeX3 = array([coordX1, coordX2])
                holeY3 = array([144, 144])
                holeX5 = array([coordX1, coordX2])
                holeY5 = array([167, 167])
                holeX7 = array([coordX1, coordX2])
                holeY7 = array([189, 189])
                holeX9 = array([coordX1, coordX2])
                holeY9 = array([213, 213])

                holeX2 = array([coordX12, coordX22])
                holeY2 = array([131, 131])
                holeX4 = array([coordX12, coordX22])
                holeY4 = array([156, 156])
                holeX6 = array([coordX12, coordX22])
                holeY6 = array([178, 178])
                holeX8 = array([coordX12, coordX22])
                holeY8 = array([200, 200])
                holeX10 = array([coordX12, coordX22])
                holeY10 = array([224, 224])

                coordX1_neg = int(-75)
                coordX2_neg = int(0)
                coordX12_neg = int(-25)
                coordX22_neg = int(50)

                holeX1_neg = array([coordX1_neg, coordX2_neg])
                holeY1_neg = array([-120, -120])
                holeX3_neg = array([coordX1_neg, coordX2_neg])
                holeY3_neg = array([-144, -144])
                holeX5_neg = array([coordX1_neg, coordX2_neg])
                holeY5_neg = array([-167, -167])
                holeX7_neg = array([coordX1_neg, coordX2_neg])
                holeY7_neg = array([-189, -189])
                holeX9_neg = array([coordX1_neg, coordX2_neg])
                holeY9_neg = array([-213, -213])

                holeX2_neg = array([coordX12_neg, coordX22_neg])
                holeY2_neg = array([-131, -131])
                holeX4_neg = array([coordX12_neg, coordX22_neg])
                holeY4_neg = array([-156, -156])
                holeX6_neg = array([coordX12_neg, coordX22_neg])
                holeY6_neg = array([-178, -178])
                holeX8_neg = array([coordX12_neg, coordX22_neg])
                holeY8_neg = array([-200, -200])
                holeX10_neg = array([coordX12_neg, coordX22_neg])
                holeY10_neg = array([-224, -224])

            elif width == 305:
                coordX1 = int(-75)
                coordX2 = int(0)
                coordX12 = int(-25)
                coordX22 = int(50)

                holeX1 = array([coordX1, coordX2])
                holeY1 = array([144, 144])
                holeX3 = array([coordX1, coordX2])
                holeY3 = array([168, 168])
                holeX5 = array([coordX1, coordX2])
                holeY5 = array([191, 191])
                holeX7 = array([coordX1, coordX2])
                holeY7 = array([213, 213])
                holeX9 = array([coordX1, coordX2])
                holeY9 = array([237, 237])

                holeX2 = array([coordX12, coordX22])
                holeY2 = array([155, 155])
                holeX4 = array([coordX12, coordX22])
                holeY4 = array([180, 180])
                holeX6 = array([coordX12, coordX22])
                holeY6 = array([202, 202])
                holeX8 = array([coordX12, coordX22])
                holeY8 = array([224, 224])
                holeX10 = array([coordX12, coordX22])
                holeY10 = array([248, 248])

                coordX1_neg = int(-75)
                coordX2_neg = int(0)
                coordX12_neg = int(-25)
                coordX22_neg = int(50)

                holeX1_neg = array([coordX1_neg, coordX2_neg])
                holeY1_neg = array([-144, -144])
                holeX3_neg = array([coordX1_neg, coordX2_neg])
                holeY3_neg = array([-168, -168])
                holeX5_neg = array([coordX1_neg, coordX2_neg])
                holeY5_neg = array([-191, -191])
                holeX7_neg = array([coordX1_neg, coordX2_neg])
                holeY7_neg = array([-213, -213])
                holeX9_neg = array([coordX1_neg, coordX2_neg])
                holeY9_neg = array([-237, -237])

                holeX2_neg = array([coordX12_neg, coordX22_neg])
                holeY2_neg = array([-155, -155])
                holeX4_neg = array([coordX12_neg, coordX22_neg])
                holeY4_neg = array([-180, -180])
                holeX6_neg = array([coordX12_neg, coordX22_neg])
                holeY6_neg = array([-202, -202])
                holeX8_neg = array([coordX12_neg, coordX22_neg])
                holeY8_neg = array([-224, -224])
                holeX10_neg = array([coordX12_neg, coordX22_neg])
                holeY10_neg = array([-248, -248])
            # SA-305-1.2-TU-OUT
            n = length // 100
            for i in range(0, n - 1):
                width_254_305(holeX1, holeY1, holeX2, holeY2, holeX3, holeY3, holeX4, holeY4, holeX5, holeY5, holeX6,
                              holeY6, holeX7, holeY7, holeX8, holeY8, holeX9, holeY9, holeX10, holeY10, holeX1_neg,
                              holeY1_neg, holeX2_neg, holeY2_neg,
                              holeX3_neg, holeY3_neg, holeX4_neg,
                              holeY4_neg, holeX5_neg, holeY5_neg, holeX6_neg, holeY6_neg, holeX7_neg, holeY7_neg,
                              holeX8_neg, holeY8_neg, holeX9_neg, holeY9_neg, holeX10_neg, holeY10_neg, i)
            plot(x, y, 'k-', x1, y1, 'k-', r1, r2, 'k-', r11, r12, 'k-', r13, r14, 'k-', arrow11, arrow12, 'k-',
                 arrow21, arrow22, 'k-', holeX1, holeY1, 'k-', holeX2, holeY2, 'k-', holeX3, holeY3, 'k-', holeX4,
                 holeY4, 'k-', holeX5, holeY5, 'k-', holeX6, holeY6, 'k-', holeX7, holeY7, 'k-', holeX8, holeY8, 'k-',
                 holeX9, holeY9, 'k-', holeX10, holeY10, 'k-',
                 holeX1_neg, holeY1_neg, 'k-', holeX2_neg, holeY2_neg, 'k-', holeX3_neg, holeY3_neg, 'k-', holeX4_neg,
                 holeY4_neg, 'k-', holeX5_neg, holeY5_neg, 'k-', holeX6_neg, holeY6_neg, 'k-', holeX7_neg, holeY7_neg,
                 'k-', holeX8_neg, holeY8_neg, 'k-', holeX9_neg, holeY9_neg, 'k-', holeX10_neg, holeY10_neg, 'k-')


def width_102(x1, y1, x2, y2, x3, y3, x4, y4, x1_neg, y1_neg, x2_neg, y2_neg, x3_neg, y3_neg, x4_neg, y4_neg, n):
    x1 += 100
    x2 += 100
    x3 += 100
    x4 += 100
    x1_neg += 100
    x2_neg += 100
    x3_neg += 100
    x4_neg += 100
    plot(x1, y1, 'k-', x2, y2, 'k-', x3, y3, 'k-', x4, y4, 'k-', x1_neg, y1_neg, 'k-', x2_neg, y2_neg, 'k-',
         x3_neg, y3_neg, 'k-', x4_neg, y4_neg, 'k-')


def width_152(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x1_neg, y1_neg, x2_neg, y2_neg, x3_neg, y3_neg, x4_neg,
              y4_neg, x5_neg, y5_neg, x6_neg, y6_neg, n):
    x1 += 100
    x2 += 100
    x3 += 100
    x4 += 100
    x5 += 100
    x6 += 100
    x1_neg += 100
    x2_neg += 100
    x3_neg += 100
    x4_neg += 100
    x5_neg += 100
    x6_neg += 100
    plot(x1, y1, 'k-', x2, y2, 'k-', x3, y3, 'k-', x4, y4, 'k-', x5, y5, 'k-', x6, y6, 'k-',
         x1_neg, y1_neg, 'k-', x2_neg, y2_neg, 'k-', x3_neg, y3_neg, 'k-', x4_neg, y4_neg, 'k-',
         x5_neg, y5_neg, 'k-', x6_neg, y6_neg, 'k-')


def width_203(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x1_neg, y1_neg, x2_neg, y2_neg, x3_neg,
              y3_neg, x4_neg, y4_neg, x5_neg, y5_neg, x6_neg, y6_neg, x7_neg, y7_neg, x8_neg, y8_neg, n):
    x1 += 100
    x2 += 100
    x3 += 100
    x4 += 100
    x5 += 100
    x6 += 100
    x7 += 100
    x8 += 100
    x1_neg += 100
    x2_neg += 100
    x3_neg += 100
    x4_neg += 100
    x5_neg += 100
    x6_neg += 100
    x7_neg += 100
    x8_neg += 100
    plot(x1, y1, 'k-', x2, y2, 'k-', x3, y3, 'k-', x4, y4, 'k-', x5, y5, 'k-', x6, y6, 'k-', x7, y7, 'k-', x8, y8, 'k-',
         x1_neg, y1_neg, 'k-', x2_neg, y2_neg, 'k-', x3_neg, y3_neg, 'k-', x4_neg, y4_neg, 'k-',
         x5_neg, y5_neg, 'k-', x6_neg, y6_neg, 'k-', x7_neg, y7_neg, 'k-', x8_neg, y8_neg, 'k-')


def width_254_305(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x1_neg, y1_neg,
                  x2_neg, y2_neg, x3_neg,
                  y3_neg, x4_neg, y4_neg, x5_neg, y5_neg, x6_neg, y6_neg, x7_neg, y7_neg, x8_neg, y8_neg, x9_neg,
                  y9_neg, x10_neg, y10_neg, n):
    x1 += 100
    x2 += 100
    x3 += 100
    x4 += 100
    x5 += 100
    x6 += 100
    x7 += 100
    x8 += 100
    x9 += 100
    x10 += 100
    x1_neg += 100
    x2_neg += 100
    x3_neg += 100
    x4_neg += 100
    x5_neg += 100
    x6_neg += 100
    x7_neg += 100
    x8_neg += 100
    x9_neg += 100
    x10_neg += 100
    plot(x1, y1, 'k-', x2, y2, 'k-', x3, y3, 'k-', x4, y4, 'k-', x5, y5, 'k-', x6, y6, 'k-', x7, y7, 'k-', x8, y8, 'k-',
         x9, y9, 'k-', x10, y10, 'k-',
         x1_neg, y1_neg, 'k-', x2_neg, y2_neg, 'k-', x3_neg, y3_neg, 'k-', x4_neg, y4_neg, 'k-',
         x5_neg, y5_neg, 'k-', x6_neg, y6_neg, 'k-', x7_neg, y7_neg, 'k-', x8_neg, y8_neg, 'k-', x9_neg, y9_neg, 'k-',
         x10_neg, y10_neg, 'k-')


profile = input('Введите профиль ')
length = int(input('Введите длину '))
if '89' in profile:
    width = int(89)
elif '102' in profile:
    width = int(102)
elif '152' in profile:
    width = int(152)
elif '203' in profile:
    width = int(203)
elif '254' in profile:
    width = int(254)
elif '305' in profile:
    width = int(305)

# ----Rectangle1----#
x = array([0, 0, length, length, 0])
y = array([-50, -width - 50, -width - 50, -50, -50])

# ----Rectangle2----#
x1 = array([0, 0, length, length, 0])
y1 = array([50, width + 50, width + 50, 50, 50])

# ----Size line----#
r1 = array([0, length])
r2 = array([-width - 40 - 0.4 * width, -width - 40 - 0.4 * width])

# ----Vertical size lines----#
r11 = array([0, 0])
r12 = array([-50 - width, -width - 50 - 0.4 * width])
r13 = array([length, length])
r14 = array([-50 - width, -width - 50 - 0.4 * width])

# ----Arrows on size line----#
arrow11 = array([0.035 * length, 0, 0.035 * length])
arrow12 = array(
    [-width - 40 - 0.4 * width + 0.2 * width, -width - 40 - 0.4 * width, -width - 40 - 0.4 * width - 0.2 * width])
arrow21 = array([length - 0.035 * length, length, length - 0.035 * length])
arrow22 = array(
    [-width - 40 - 0.4 * width + 0.2 * width, -width - 40 - 0.4 * width, -width - 40 - 0.4 * width - 0.2 * width])
perforation_check()

if 'U' in profile:
    plot(x, y, 'k-', x1, y1, 'k-', r1, r2, 'k-', r11, r12, 'k-', r13, r14, 'k-', arrow11, arrow12, 'k-', arrow21,
         arrow22, 'k-')
    fill(x, y, 'lightgreen')
    fill(x1, y1, 'lightgreen')

if 'C-IN' in profile:
    # ----Rectangle1 shelves----#
    x2 = array([0, length])
    y2 = array([-50 - 13, -50 - 13])
    x3 = array([0, length])
    y3 = array([-50 - width + 13, -50 - width + 13])

    # ----Rectangle2 shelves----#
    x21 = array([0, length])
    y21 = array([50 + 13, 50 + 13])
    x31 = array([0, length])
    y31 = array([50 + width - 13, 50 + width - 13])
    plot(x, y, 'k-', x1, y1, 'k-', x2, y2, 'k-', x3, y3, 'k-',
         x21, y21, 'k--', x31, y31, 'k--', r1, r2, 'k-', r11, r12, 'k-', r13, r14,
         'k-', arrow11, arrow12, 'k-', arrow21, arrow22, 'k-')
    fill(x, y, 'plum')
    fill(x1, y1, 'plum')

show()

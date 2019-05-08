import math

radius = float(input('請輸入半徑：'))

perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print('周長：%.2f' % perimeter)
print('面積：%.2f' % area)


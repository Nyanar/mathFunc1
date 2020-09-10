class Point:
    def __init__(self, p_x, p_y, **kwargs):
        self.x, self.y = p_x, p_y
        if 'id' in kwargs: self.id = kwargs['id']


def pointDist(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** (1 / 2)


p, q, points = Point(2, 7), Point(2, -3), [Point(12, -3, id='i'), Point(-6, -9, id='ii'), Point(-117, 2, id='iii')]

for i in points:
    sides = [pointDist(p, i), pointDist(q, i), pointDist(p, q)]
    if len(sides) != len(set(sides)):
        print(i.id)

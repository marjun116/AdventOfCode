rf = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def wins(p1, t1, p2, t2):
    if t2 <= 0:
        return (0, 1)

    w1, w2 = 0, 0
    for (r, f) in rf:
        c2, c1 = wins(p2, t2, (p1+r) % 10, t1 - 1 - (p1+r) % 10)
        w1, w2 = w1 + f * c1, w2 + f * c2

    return w1, w2


print("Bigger winner universes:", max(
    wins(3, 21, 2, 21)))

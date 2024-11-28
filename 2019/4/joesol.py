
rng = range(165432,707912)


def check(p, part2):
    last_char = p[0]
    for c in p[1:]:
        if c < last_char:
            return False
        last_char = c

    for i in range(0, 10):
        matches = len(list(filter(lambda x: x == str(i), p)))
        if matches == 2 or (not part2 and matches >= 2):
            return True
    return False


def do(part2):
    return sum(check(str(p), part2) for p in rng)


print("Part 1:", do(False))
print("Part 2:", do(True))

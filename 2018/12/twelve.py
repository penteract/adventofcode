orig = "#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............"

rules = """##... => .
##.## => .
.#.#. => #
#..#. => .
#.### => #
.###. => .
#.#.. => .
##..# => .
..... => .
...#. => .
.#..# => .
####. => #
...## => #
..### => #
#.#.# => #
###.# => #
#...# => #
..#.# => .
.##.. => #
.#... => #
.##.# => #
.#### => .
.#.## => .
..##. => .
##.#. => .
#.##. => .
#..## => .
###.. => .
....# => .
##### => #
#.... => .
..#.. => #"""

r = {x[:5]:x[-1] for x in rules.split("\n")}

def gen(x):
        xx = "..."+x+"..."#don't need more because of input
        res = []
        for i in range(2,len(xx)-2):
                res.append(r[xx[i-2:i+3]])
        return "".join(res)

def cut(s):
    n=0
    while s[0]==".":
        s=s[1:]
        n+=1
    while s[-1]==".":
        s=s[:-1]
    return (s,n)

def rep(n,g=orig):
    count=0
    for i in range(n):
        g=gen(g)
        print(g)
        g,d=cut(g)
        count+=d-1
    return count

def score(s):
    tot = 0
    for i,c in enumerate(s):
        if c=="#":
            tot+=i
    return tot

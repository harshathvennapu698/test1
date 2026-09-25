data = input()
n = int(data)

ranges = []
for _ in range(n):
    s, e = map(int, input().split())
    ranges.append((s, e))

ranges.sort()

merged = [ranges[0]]

for i in range(1, n):
    s, e = ranges[i]
    last_s, last_e = merged[-1]
    if s <= last_e:
        if e > last_e:
            merged[-1] = (last_s, e)
    else:
        merged.append((s, e))

for s, e in merged:
    print(s, e)
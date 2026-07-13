from sortedcontainers import SortedDict

d = SortedDict({
    1.0: "a",
    2.5: "b",
    4.0: "c",
    5.5: "d",
})

target = 4.8

idx = d.bisect_left(target)
if idx:
    prev_key = d.keys()[idx - 1]
    print(prev_key)  # 4.0

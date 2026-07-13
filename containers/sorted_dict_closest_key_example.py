# Source - https://stackoverflow.com/a/22997000
# Posted by GrantJ, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-13, License - CC BY-SA 4.0

from itertools import islice
from sortedcontainers import SortedDict

def closest(sorted_dict, key):
    "Return closest key in `sorted_dict` to given `key`."
    assert len(sorted_dict) > 0
    keys = list(islice(sorted_dict.irange(minimum=key), 1))
    keys.extend(islice(sorted_dict.irange(maximum=key, reverse=True), 1))
    return min(keys, key=lambda k: abs(key - k))

sd = SortedDict({-3: 'a', 0: 'b', 2: 'c'})
for num in range(-5, 5):
    key = closest(sd, num)
    print('Given', num, ', closest:', key)

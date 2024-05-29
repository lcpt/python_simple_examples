import json

d = {}
d["a"] = d # -> Circular reference
d["a"] = d.copy() # -> No circular reference.

json.dumps(d) # raises ValueError: Circular reference detected

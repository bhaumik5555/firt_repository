import json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
# '["foo", {"bar": ["baz", null, 1.0, 2]}]'
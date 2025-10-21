from itertools import product
from itertools import starmap

print(*starmap(str.__add__, product("ABCDEFGH", "12345678")))

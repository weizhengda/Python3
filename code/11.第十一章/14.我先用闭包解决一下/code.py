origin = 0

def go(step):
    new_pos = origin + step
    origin = new_pos
    return origin

print(go(2))
print(go(3))
print(go(6))
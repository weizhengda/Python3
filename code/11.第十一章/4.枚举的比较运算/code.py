# 枚举类型不可以做大小的比较,
# 但是可以做身份和等值（全等）比较
 from enum import Enum

 class VIP(Enum):
     YELLOW = 1
     GREEN = 2
     BLACK = 3
     RED = 4

class VIP1(Enum):
     YELLOW = 1
     GREEN = 2
     BLACK = 3
     RED = 4

 class Common():
     YELLOW = 1

result1 = VIP.GREEN is VIP.BLACK
console.log(result1)

result2 = VIP.GREEN == VIP1.GREEN
console.log(result2)
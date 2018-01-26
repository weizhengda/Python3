 from enum import Enum

 class VIP(Enum):
     YELLOW = 1
     GREEN = 2
     BLACK = 3
     RED = 4
# 别名
 class Common():
     YELLOW = 1
    
 for v in VIP:
     print(v)

 for v in VIP._menbers_:
     print(v)

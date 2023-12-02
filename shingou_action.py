import sys
from enum import Enum
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(args):
    if int(args[1]) == 1:
        print("とまれ")
    elif int(args[2]) == 2:
        print("すすめ")
    elif int(args[3]) == 3:
        print("ちゅうい")
    else:
        print("信号機の色に対応していません")
        
    return Shingou

args =  sys.argv
act_shingou(args)
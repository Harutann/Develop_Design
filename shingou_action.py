import sys
from enum import Enum
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

    def act_shingou(args):
        args = sys.argv
        if args == 1:
            print("とまれ")
        elif args == 2:
            print("すすめ")
        elif args == 3:
            print("ちゅうい")
        else:
            print("信号機の色に対応していません")
            
        
        return Shingou
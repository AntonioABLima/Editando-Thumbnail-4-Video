import os
from generateClock import buildClock
from generateThumb import buildThumbnail
from cropRoundBg import removeBackGround

def main():
    os.system("node Manipulating_Thumbnail/generateSub.js")
    removeBackGround()
    buildClock()
    buildThumbnail()


if __name__ == '__main__':
    main()
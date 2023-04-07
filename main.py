import os
from generateClock import buildClock
from generateThumb import buildThumbnail
from cropRoundBg import removeBackGround

def main():
    removeBackGround()
    buildClock()
    buildThumbnail()

    file_path = 'images/thumb/final_thumbnail.png'
    size = os.stat(file_path).st_size
    mBSize = size / 1024**2
    print(mBSize)

if __name__ == '__main__':
    main()
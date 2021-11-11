
from time import time
from time import sleep

def ft_progress(listing, sizebar=30):
    elapsed_time = 0
    loopend = 0.01
    count = len(listing)
    for i, item in enumerate(listing):
        loopstart = time()
        x = int(sizebar * (i + 1) / count)
        print("\rETA: %.2fs [%3d%%][%s>%s] %d/%d | elapsed time %.2fs"
              % (loopend * (len(listing) - i) + elapsed_time,
                 (i + 1) / count * 100,
                 "=" * x,
                 " " * (sizebar - x), (i + 1), count, elapsed_time),
              end='', flush=True)
        yield item
        loopend = time() - loopstart
        elapsed_time = elapsed_time + loopend
import asyncio
import datetime
import time


def f1(end, loop):
    print("f1 called")
    if (loop.time() + 1 < end):
        loop.call_later(1, f2, end, loop)
    else:
        loop.stop()

def f2(end, loop):
    print("f2 called")
    if(loop.time()+1 < end):
        loop.call_later(1, f1, end, loop)
    else:
        loop.stop()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    end = loop.time() + 8
    loop.call_soon(f1, end, loop)
    loop.run_forever()
    loop.close()

import subprocess as sp
import time
from concurrent.futures import ThreadPoolExecutor

def ping(a, b, x, y):
    ip = [str(a), str(b), str(x), str(y)]
    result = ".".join(ip)
    sp.run(["ping", "-c", "1", result])

def scan(a, b, x, target):
    with ThreadPoolExecutor(max_workers=target) as executor:
        for y in range(target):
            executor.submit(ping, a, b, x, y)

start = time.time()
scan(1,1,1,255)
end = time.time()

print(end - start)
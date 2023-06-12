from pwn import *
import re

conn = remote("challs.n00bzunit3d.xyz", 13541)

try:
    def counter(dest, num):
        nums = []
        count = 0
        for i in range(1, dest):
            if str(num) in str(i):
                count += str(i).count(str(num))
        return count

    for i in range(1000):
        print(conn.recvline())
        rec = conn.recvline()
        print(rec)
        x = int(re.search(r"(\d+)'s", rec.decode()).group(1))
        y = int(re.search(r"till (\d+)", rec.decode()).group(1))

        res = str(counter(y, x)).encode('utf-8')
        print(res)
        conn.sendline(res)
        print(conn.recvline())

except EOFError:
    print("Connection closed.")

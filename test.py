#encoding=utf-8
import time
from concurrent.futures import ProcessPoolExecutor
__author__ = 'lichunyu'


def a():
    print   ("hahha")
def c():
    print   ("hahha")
def b():
    with  ProcessPoolExecutor(max_workers=2) as pool:
        result = pool.submit(a)
        result_1 = pool.submit(c)
    print ("haha")

b()
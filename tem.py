
from datetime import datetime
from time import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        try:
            start = time()
            print(start)
            res = func(*args,**kwargs)
            end =start - time()
            print(end)
            return res
            
        except:
            print("failed")

@calculate_time
def revers():
    word = "selvakumar"
    r_word = word[::-1]

    res=' '.join(r_word)
    print(res)

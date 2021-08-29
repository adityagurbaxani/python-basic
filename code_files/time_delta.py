#Time Delta
#Print the absolute difference (in seconds) between two timestamps

#Sample Input
#1
#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000

#Sample Output
#25200

#!/bin/python3
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    diff = int(abs((dt.strptime(t1, format_str) - dt.strptime(t2, format_str)).total_seconds()))
    return diff

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
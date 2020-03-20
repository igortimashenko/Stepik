#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    #pass
    for i in range(1):
        move_right(2)
        move_down(1)

'''
        if i == 6:
            z = 1 / 0
'''
if __name__ == '__main__':
    run_tasks()

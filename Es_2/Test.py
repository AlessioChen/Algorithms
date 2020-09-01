from ARN import ARN
from ABR import ABR
from timeit import default_timer as timer
import random


def test_inorder(test_times, max_iterartion, increment):
    arn = ARN()
    abr = ABR()
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for el_numbers in range(0, max_iterartion, increment):
        print('----------- {} ------------------'.format(el_numbers))
        for j in range(1, el_numbers):
            arn.insert(j)
            abr.insert(j)
        y3.append(abr.get_lenght())
        y4.append(arn.get_lenght())
        avg1 = 0
        avg2 = 0

        for j in range(1, test_times):
            # inorder test on ABR
            start = timer()
            abr.find(j)
            end = timer()
            time = (end - start)
            avg1 = avg1 + time

            # inorder test on ARN
            start = timer()
            arn.find(j)
            end = timer()
            time = (end - start)
            avg2 = avg2 + time
        avg1 = avg1 / test_times
        avg2 = avg2 / test_times

        x.append(el_numbers)
        y1.append(avg1)
        y2.append(avg2)

    return x, y1, y2, y3, y4, test_times,


def test_randomized(test_times, max_iteration, increment):
    arn = ARN()
    abr = ABR()
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for el_numbers in range(0, max_iteration, increment):
        print('----------- {} ------------------'.format(el_numbers))
        for j in range(1, el_numbers):
            i = random.randint(0, 1000)
            arn.insert(i)
            abr.insert(i)
        y3.append(abr.get_lenght())
        y4.append(arn.get_lenght())
        avg1 = 0
        avg2 = 0

        for j in range(1, test_times):
            i = random.randint(0, 1000)
            # randomnized test on ABR
            start = timer()
            abr.find(i)
            end = timer()
            time = (end - start)
            avg1 = avg1 + time
            # randomnized test on ARN
            start = timer()
            arn.find(i)
            end = timer()
            time = (end - start)
            avg2 = avg2 + time
        avg1 = avg1 / test_times
        avg2 = avg2 / test_times

        x.append(el_numbers)
        y1.append(avg1)
        y2.append(avg2)

    return x, y1, y2, y3, y4, test_times

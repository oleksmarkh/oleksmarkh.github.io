#!/usr/bin/env python


from os import cpu_count


def fib(n):
    if n < 0:
        raise Exception("fib(n) is undefined for n < 0")

    if n == 0:
        return 0

    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


N = 36
NCORES = int(cpu_count() / 2)


class FibWorker(object):
    def fib(self, n):
        return fib(n)


print(fib(10))

## to read / play around

### concurrent.futures

`ThreadPoolExecutor` and `ProcessPoolExecutor`

https://docs.python.org/dev/library/concurrent.futures.html


### pyro

daemon is a socket server (`from socket import ...`)

`worker.py` example:

```python
import Pyro4

...

daemon = Pyro4.Daemon(host=IP)
uri = daemon.register(FibWorker)

qualified_name = '.'.join(FibWorker.__module__,
                          FibWorker.__name__,
                          str(n))

Pyro4.locateNS().register(qualified_name, uri)

...

daemon.requestLoop()
```

`main.py` example:

```python
# "sync"
...

worker_uris = itertools.cycle([uri for (name, uri) in ns.list().items()]
                              if name.startswith(...))
worker = Pyro4.Proxy(next(worker_uris))
serial_result = worker.fib(N)

...


# async
...

for n in args:
    worker = Pyro4.Proxy(next(worker_uris))
    async_worker = Pyro4.async(worker)
    async_results = [future.value for future in map(async_worker.fib, args)]

...
```


### celery

* can fork out child processes to work in parallel (to use all the cores available)
* has a cli: `celery -A tasks -c 4 -l info worker`
* topology "adapts"

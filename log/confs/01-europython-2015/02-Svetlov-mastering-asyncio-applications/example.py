import asyncio


@asyncio.coroutine
def go():
    print('a')
    yield from asyncio.sleep(0.1)
    print('b')
    return 234


@asyncio.coroutine
def outer():
    ret = yield from go()
    print('RET', ret)


loop = asyncio.get_event_loop()
loop.run_until_complete(outer())


print('done')

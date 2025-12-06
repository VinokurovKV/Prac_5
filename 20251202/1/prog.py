import asyncio

async def writer(queue, delay, event):
    counter = 0
    while not event.is_set():
        await asyncio.sleep(delay)
        if event.is_set():
            break
        item = f"{counter}_{delay}"
        await queue.put(item)
        counter += 1

async def stacker(queue, stack, event):
    while True:
        if event.is_set() and queue.empty():
            break
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.1)
            stack.append(item)
        except asyncio.TimeoutError:
            continue

async def reader(stack, count, delay, event):
    for _ in range(count):
        await asyncio.sleep(delay)
        while True:
            if stack:
                item = stack.pop()
                print(item)
                break
            else:
                await asyncio.sleep(0.01)
    event.set()

async def main():
    input_values = input().strip()
    d1, d2, d3, cnt = map(int, input_values.split(','))
    
    q = asyncio.Queue()
    s = []
    e = asyncio.Event()

    coroutines = [
        asyncio.create_task(writer(q, d1, e)),
        asyncio.create_task(writer(q, d2, e)),
        asyncio.create_task(stacker(q, s, e)),
        asyncio.create_task(reader(s, cnt, d3, e)),
    ]

    await coroutines[-1]

    for coroutine in coroutines:
        if not coroutine.done():
            coroutine.cancel()
    await asyncio.gather(*coroutines, return_exceptions=True)

asyncio.run(main())
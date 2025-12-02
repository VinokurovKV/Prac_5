import asyncio

async def snd(event):
    event.set()
    print(f'snd set evsnd')

async def mid(k, event, event2):
    await event.wait()
    print(f'mid get evsnd')
    event2.set()
    print(f'mid set midsnd{k}')

async def rcv(event0, event1):
    await event0.wait()
    print(f'rcv get evmid0')
    await event1.wait()
    print(f'rcv get evmid1')

async def main():
    evsnd = asyncio.Event()
    evmid0 = asyncio.Event()
    evmid1 = asyncio.Event()
    await asyncio.gather(
        rcv(evmid0, evmid1),
        mid(1, evsnd, evmid1),
        mid(0, evsnd, evmid0),
        snd(evsnd),
    )


asyncio.run(main())


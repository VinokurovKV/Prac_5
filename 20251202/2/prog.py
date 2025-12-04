import asyncio
import math

async def merge(source, target, start, mid, end, ev1, ev2, ev_out):
    await ev1.wait()
    await ev2.wait()
    
    left_idx = start
    right_idx = mid
    res_idx = start
    
    while left_idx < mid and right_idx < end:
        if source[left_idx] <= source[right_idx]:
            target[res_idx] = source[left_idx]
            left_idx += 1
        else:
            target[res_idx] = source[right_idx]
            right_idx += 1
        res_idx += 1
    
    while left_idx < mid:
        target[res_idx] = source[left_idx]
        left_idx += 1
        res_idx += 1
    
    while right_idx < end:
        target[res_idx] = source[right_idx]
        right_idx += 1
        res_idx += 1
    
    ev_out.set()

async def mtasks(original):
    n = len(original)
    if n <= 1:
        return [], original.copy()
    
    source = original.copy()
    target = [0] * n
    
    levels = math.ceil(math.log2(n))
    
    level_events = []
    
    base_events = [asyncio.Event() for _ in range(n)]
    for ev in base_events:
        ev.set()
    level_events.append(base_events)
    
    tasks = []
    
    for level in range(levels):
        segment_size = 1 << level 
        next_segment_size = segment_size * 2
        
        next_segments = (n + next_segment_size - 1) // next_segment_size
        next_level_events = [asyncio.Event() for _ in range(next_segments)]
        level_events.append(next_level_events)
        
        for i in range(next_segments):
            start = i * next_segment_size
            mid = min(start + segment_size, n)
            end = min(start + next_segment_size, n)
            
            left_event_idx = i * 2
            right_event_idx = i * 2 + 1
            
            ev_left = level_events[level][left_event_idx] if left_event_idx < len(level_events[level]) else None
            ev_right = level_events[level][right_event_idx] if right_event_idx < len(level_events[level]) else None
            ev_result = next_level_events[i]
            
            if ev_left is not None and ev_right is not None:
                task = asyncio.create_task(
                    merge(source, target, start, mid, end, ev_left, ev_right, ev_result)
                )
                tasks.append(task)
            elif ev_left is not None:
                async def copy_task(src, dst, s, e, ev_in, ev_out):
                    await ev_in.wait()
                    for idx in range(s, e):
                        dst[idx] = src[idx]
                    ev_out.set()
                
                task = asyncio.create_task(
                    copy_task(source, target, start, end, ev_left, ev_result)
                )
                tasks.append(task)
        
        source, target = target, source
    
    return tasks, source

import sys
exec(sys.stdin.read())
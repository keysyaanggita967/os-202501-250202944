reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames_count = 3


def fifo_table(ref, frames_count):
    frames = []
    faults = 0

    print("\nFIFO PAGE REPLACEMENT")
    print("-" * 35)
    print("| No | Page | Status | Frame Isi |")
    print("-" * 35)

    for i, page in enumerate(ref, 1):
        if page in frames:
            status = "HIT"
        else:
            status = "MISS"
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        frame_view = " ".join(map(str, frames))
        frame_view += " -" * (frames_count - len(frames))
        print(f"| {i:<2} | {page:<4} | {status:<6} | {frame_view:<10} |")

    print("-" * 35)
    print(f"Total Page Fault FIFO = {faults}")
    return faults


def lru_table(ref, frames_count):
    frames = []
    history = []
    faults = 0

    print("\nLRU PAGE REPLACEMENT")
    print("-" * 35)
    print("| No | Page | Status | Frame Isi |")
    print("-" * 35)

    for i, page in enumerate(ref, 1):
        if page in frames:
            status = "HIT"
            history.remove(page)
        else:
            status = "MISS"
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                old = history.pop(0)
                frames.remove(old)
                frames.append(page)

        history.append(page)
        frame_view = " ".join(map(str, frames))
        frame_view += " -" * (frames_count - len(frames))
        print(f"| {i:<2} | {page:<4} | {status:<6} | {frame_view:<10} |")

    print("-" * 35)
    print(f"Total Page Fault LRU = {faults}")
    return faults


fifo_fault = fifo_table(reference_string, frames_count)
lru_fault = lru_table(reference_string, frames_count)

print("\nRINGKASAN HASIL")

print(f"Total Page Fault FIFO : {fifo_fault}")
print(f"Total Page Fault LRU  : {lru_fault}")

if fifo_fault < lru_fault:
    print("Algoritma yang lebih efisien: FIFO")
elif lru_fault < fifo_fault:
    print("Algoritma yang lebih efisien: LRU")
else:
    print("Kedua algoritma memiliki efisiensi yang sama")


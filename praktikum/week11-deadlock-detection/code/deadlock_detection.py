# =========================
# DATASET PROSES & RESOURCE
# =========================
processes = {
    "P1": {"alloc": "R1", "req": "R2"},
    "P2": {"alloc": "R2", "req": "R3"},
    "P3": {"alloc": "R3", "req": "R1"},
}

# =========================
# MEMETAKAN RESOURCE → PROSES
# =========================
resource_owner = {}
for p, data in processes.items():
    resource_owner[data["alloc"]] = p

# =========================
# MEMBANGUN WAIT-FOR GRAPH
# =========================
wait_for = {}
for p, data in processes.items():
    req = data["req"]
    if req in resource_owner:
        wait_for[p] = resource_owner[req]
    else:
        wait_for[p] = None

# =========================
# DETEKSI SIKLUS (DEADLOCK)
# =========================
visited = set()
stack = []
deadlock = set()

def dfs(process):
    if process in stack:
        # Ambil semua proses yang membentuk siklus
        cycle_start = stack.index(process)
        for p in stack[cycle_start:]:
            deadlock.add(p)
        return

    if process in visited or wait_for[process] is None:
        return

    visited.add(process)
    stack.append(process)

    dfs(wait_for[process])

    stack.pop()

# Jalankan DFS untuk setiap proses
for p in wait_for:
    dfs(p)

# =========================
# OUTPUT HASIL
# =========================
print("WAIT-FOR GRAPH:")
for p, w in wait_for.items():
    print(f"{p} -> {w}")

print("\nHASIL DETEKSI DEADLOCK:")
if deadlock:
    for p in sorted(deadlock):
        print(f"{p} : DEADLOCK")
else:
    print("Tidak ada deadlock")

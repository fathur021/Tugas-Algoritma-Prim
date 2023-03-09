from queue import PriorityQueue

# fungsi untuk menambahkan sisi pada graf
def tambah_sisi(graf, sumber, tujuan, bobot):
    graf[sumber].append((tujuan, bobot))
    graf[tujuan].append((sumber, bobot))

# fungsi untuk menyelesaikan MST dengan algoritma Prim
def prim(graf):
    # inisialisasi simpul awal dan MST
    simpul_awal = list(graf.keys())[0]
    visited = {simpul_awal}
    mst = []
    sisi = PriorityQueue()
    for tetangga in graf[simpul_awal]:
        sisi.put(tetangga)

    # tambahkan simpul baru ke dalam MST
    while not sisi.empty():
        # pilih sisi dengan bobot terkecil
        min_sisi = sisi.get()
        if min_sisi[0] not in visited:
            visited.add(min_sisi[0])
            mst.append(min_sisi)
            # tambahkan sisi terhubung ke dalam MST
            for tetangga in graf[min_sisi[0]]:
                if tetangga[0] not in visited:
                    sisi.put(tetangga)
    return mst

# contoh penggunaan
graf = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print("Graf awal:")
print(graf)

mst = prim(graf)
print("Minimum Spanning Tree:")
print(mst)

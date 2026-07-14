import re


def validate_cfg(grammar_text):
    """
    Validasi grammar CFG sederhana.
    Return:
        (True, "Grammar valid.")
        atau
        (False, "Pesan error")
    """

    lines = grammar_text.strip().splitlines()

    if not lines:
        return False, "Grammar tidak boleh kosong."

    for nomor, line in enumerate(lines, start=1):

        line = line.strip()

        if line == "":
            continue

        if "->" not in line:
            return False, f"Baris {nomor}: simbol '->' tidak ditemukan."

        left, right = line.split("->", 1)

        left = left.strip()
        right = right.strip()

        if left == "":
            return False, f"Baris {nomor}: nonterminal kiri kosong."

        if len(left) != 1 or not left.isupper():
            return False, (
                f"Baris {nomor}: nonterminal kiri harus satu huruf kapital."
            )

        if right == "":
            return False, f"Baris {nomor}: produksi kosong."

        productions = right.split("|")

        for p in productions:

            p = p.strip()

            if p == "":
                return False, (
                    f"Baris {nomor}: terdapat produksi kosong."
                )

    return True, "Grammar valid."


def parse_cfg(grammar_text):

    grammar = {}

    lines = grammar_text.strip().splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        left, right = line.split("->", 1)

        left = left.strip()

        grammar[left] = []

        for prod in right.split("|"):

            grammar[left].append(prod.strip())

    return grammar


def tampilkan_cfg(grammar):

    hasil = []

    for left in grammar:

        hasil.append(
            f"{left} → {' | '.join(grammar[left])}"
        )

    return hasil


def is_nonterminal(ch):

    return len(ch) == 1 and ch.isupper()


def leftmost_derivation(grammar, target):

    hasil = []

    current = "S"

    hasil.append(current)

    batas = 100

    while batas > 0:

        batas -= 1

        if current == target:
            return hasil

        posisi = None

        for i, c in enumerate(current):

            if is_nonterminal(c):
                posisi = i
                break

        if posisi is None:
            break

        simbol = current[posisi]

        if simbol not in grammar:
            break

        kandidat = None

        for produksi in grammar[simbol]:

            baru = (
                current[:posisi]
                + produksi
                + current[posisi + 1:]
            )

            if len(baru.replace("ε", "")) <= len(target):
                kandidat = baru
                break

        if kandidat is None:
            break

        current = kandidat

        hasil.append(current)

    return hasil


def rightmost_derivation(grammar, target):

    hasil = []

    current = "S"

    hasil.append(current)

    batas = 100

    while batas > 0:

        batas -= 1

        if current == target:
            return hasil

        posisi = None

        for i in range(len(current) - 1, -1, -1):

            if is_nonterminal(current[i]):
                posisi = i
                break

        if posisi is None:
            break

        simbol = current[posisi]

        if simbol not in grammar:
            break

        kandidat = None

        for produksi in grammar[simbol]:

            baru = (
                current[:posisi]
                + produksi
                + current[posisi + 1:]
            )

            if len(baru.replace("ε", "")) <= len(target):
                kandidat = baru
                break

        if kandidat is None:
            break

        current = kandidat

        hasil.append(current)

    return hasil
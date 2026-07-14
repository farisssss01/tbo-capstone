def classify_grammar(grammar_text):

    grammar_type = "Type 3 (Regular)"

    reason = []

    lines = grammar_text.strip().splitlines()

    for line in lines:

        if "->" not in line:
            continue

        left, right = line.split("->")

        left = left.strip()

        productions = [p.strip() for p in right.split("|")]

        # Left side harus satu nonterminal
        if len(left) != 1 or not left.isupper():
            grammar_type = "Type 0 (Unrestricted)"
            reason.append(
                f"'{left}' bukan satu nonterminal."
            )
            break

        for prod in productions:

            uppercase = sum(c.isupper() for c in prod)

            if uppercase > 1:
                grammar_type = "Type 2 (Context-Free)"
                reason.append(
                    f"Produksi '{prod}' memiliki lebih dari satu nonterminal."
                )

            elif uppercase == 1:

                idx = next(i for i, c in enumerate(prod) if c.isupper())

                if idx != len(prod) - 1:
                    grammar_type = "Type 2 (Context-Free)"
                    reason.append(
                        f"Produksi '{prod}' tidak right-linear."
                    )

    if not reason:
        reason.append(
            "Semua produksi memenuhi bentuk grammar reguler."
        )

    return grammar_type, reason

def convert_to_cnf(grammar_text):

    langkah = []

    lines = grammar_text.strip().splitlines()

    grammar = []

    for line in lines:

        if "->" not in line:
            continue

        grammar.append(line.strip())

    langkah.append("Grammar Awal")

    langkah.extend(grammar)

    langkah.append("")

    langkah.append("Menghapus spasi yang tidak diperlukan")

    grammar = [g.replace(" ", "") for g in grammar]

    langkah.extend(grammar)

    langkah.append("")

    langkah.append("Catatan")

    langkah.append(
        "Versi awal simulator menampilkan tahapan konversi. "
        "Konversi CNF lengkap akan dikembangkan pada tahap berikutnya."
    )

    return langkah
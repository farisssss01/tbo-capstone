class CFGParser:

    def __init__(self, grammar):

        self.grammar = grammar

    def leftmost(self, target):

        if "S" not in self.grammar:
            return []

        current = "S"

        langkah = [current]

        limit = 25

        while current != target and limit > 0:

            limit -= 1

            berubah = False

            for simbol in current:

                if simbol in self.grammar:

                    for produksi in self.grammar[simbol]:

                        kandidat = current.replace(
                            simbol,
                            produksi,
                            1
                        )

                        if len(kandidat) <= len(target):

                            current = kandidat

                            langkah.append(current)

                            berubah = True

                            break

                    break

            if not berubah:
                break

        return langkah
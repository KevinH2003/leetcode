class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # docstring
        n = len(dominoes)
        straights = set()

        #
        dominoes = list(dominoes)
        dominoes = ["."] + dominoes + ["."]

        def fall_direction(index):
            #
            left = index - 1
            right = index + 1

            if dominoes[left] == "R" and dominoes[right] == "L":
                return "."
            elif dominoes[left] == "R":
                return "R"
            elif dominoes[right] == "L":
                return "L"
            else:
                return "."

        for i in range(1, n + 1):
            domino = dominoes[i]

            if domino == ".":
                straights.add(i)

        #
        for _ in range(n + 2):  # should be n i think(?)
            next_dominoes = dominoes.copy()
            changed = False
            removed = set()
            for straight_index in straights:
                new_orientation = fall_direction(straight_index)
                next_dominoes[straight_index] = new_orientation

                if new_orientation != ".":
                    changed = True
                    removed.add(straight_index)

            if not changed:
                break
            
            straights -= removed
            dominoes = next_dominoes

        return "".join(dominoes[1:n + 1])

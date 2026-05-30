class Comparator:

    matches = []
    presents = []
    chars = {}

    def test(self, s, q):
        n = len(q)

        for i in range(n):
            self.chars[i] = 0
            # print(q[i], s[i])

            if q[i] == s[i]:
                if s[i] not in self.matches: self.matches.append(q[i])
                self.chars[i] = 'correct'

            elif q[i] in s:
                self.chars[i] = 'present'

                if q[i] not in self.presents:
                    self.presents.append(q[i])
                else:
                    self.chars[i] = 'absent'

                if q[i] not in self.matches:
                    self.matches.append(q[i])
                else:
                    self.chars[i] = 'absent'

            else:
                self.chars[i] = 'absent'


if __name__ == '__main__':
    s = input()
    q = input()

    comp = Comparator()
    comp.test(s, q)
    # print(comp.matches)
    # print(comp.presents)
    # print(comp.chars)

    for c, ans in comp.chars.items():
        # print(c, s[c], q[c], ans)
        print(ans)


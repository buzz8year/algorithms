def get_prefix_hashes(word, base, mod):
    prefix_hashes = [0] * (len(word) + 1)
    for i in range(1, len(word) + 1):
        prefix_hashes[i] = (prefix_hashes[i - 1] * base % mod + ord(word[i - 1])) % mod
    return prefix_hashes


def get_powers(word, base, mod):
    powers = [0] * (len(word) + 1)
    powers[0] = 1
    for i in range(1, len(word) + 1):
        powers[i] = (powers[i - 1] * base) % mod
    return powers


def get_hash(prefix_hashes, powers, start, end, mod):
    return (prefix_hashes[-1] + mod - (prefix_hashes[start] * powers[end - start]) % mod) % mod


if __name__ == '__main__':
    base = int(input())
    mod = int(input())

    s = input()
    t = int(input())

    

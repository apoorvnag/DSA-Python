def compute_lps_array(pattern, m, lps):
    i = 0

    for q in range(1, m):
        if pattern[i] == pattern[q]:
            i = i + 1

        while i > 0 and pattern[i] != pattern[q]:
            i = lps[i - 1]

        lps[q] = i


def kmp_search(pattern, message):
    m = len(pattern)
    n = len(message)

    # Create lps[]
    lps = [0] * m

    j = 0  # Index at for pat[]

    compute_lps_array(pattern, m, lps)

    i = 0

    while i < n:
        if pattern[j] == message[i]:
            i += 1
            j += 1

        if j == m:
            print('Found the pattern at index {}'.format(i - j))
            j = lps[j - 1]
        elif i < n and pattern[j] != message[i]:
            # Do match characters
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == '__main__':
    txt = 'ABABDABACDABABCABAB'
    pat = 'ABABCABAB'

    kmp_search(pat, txt)

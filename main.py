def calculate_z(s):
    n = len(s)
    z = [0] * n
    z[0] = n  # The entire string is similar to itself
    l, r = 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            z[i] = min(z[k], r - i + 1)
            if z[i] + i > r:  # This is for a longer match
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z

def stringSimilarity(s):
    z = calculate_z(s)
    return sum(z)

# Tail starts here
num = int(input("Enter the number of test cases: ").strip())
for i in range(num):
    a = input(f"Enter string {i + 1}: ").strip()
    print(f"Similarity sum for string {i + 1}: {stringSimilarity(a)}")
    
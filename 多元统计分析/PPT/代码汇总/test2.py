def get_index(a):
    high = 0
    high_index = 0
    sec_high = 0
    sec_high_index = 0
    for i in range(0, len(a)):
        if a[i] >= high:
            sec_high = high
            sec_high_index = high_index
            high = a[i]
            high_index = i
        elif a[i] >= sec_high:
            sec_high = a[i]
            sec_high_index = i
    return [high_index, sec_high_index]


def top_adjustment(a):
    index = get_index(a)
    if a[index[0]] * 95 > a[index[1]] * 100:
        a[index[0]] = a[index[1]] * 100 / 95


t = [12, 42, 43, 121, 65, 43, 23, 76, 344]

top_adjustment(t)
print(t)

print(max(t))
print(min(t))

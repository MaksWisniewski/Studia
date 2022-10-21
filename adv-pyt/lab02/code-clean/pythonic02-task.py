data = [['bar', 'foo', 'fooba'], ['Rome', 'Madrid', 'Houston'], ['aa', 'bb', 'cc', 'dd']]

# Goal: return all strings in sub-lists which are of length at least 4

output = []
for row in data:
    for y in row:
        if len(y) >= 4:
            output.append(y)

print(output)


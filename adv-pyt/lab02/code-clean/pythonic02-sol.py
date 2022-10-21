data = [['bar', 'foo', 'fooba'], ['Rome', 'Madrid', 'Houston'], ['aa', 'bb', 'cc', 'dd']]

# Goal: return all strings in sub-lists which are of length at least 4

output = [word for line in data for word in line if len(word) >= 4]
print(output)


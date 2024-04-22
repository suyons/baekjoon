text = input().upper()
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = []
for alphabet in alphabets:
    count.append(text.count(alphabet))
if count.count(max(count)) > 1:
    print('?')
else:
    print(alphabets[count.index(max(count))])
names = ['aa','aaa','asdf','adffgeq']
for name in names:
    if name.lower() == 'asdf':
        continue
    print(name)


names.append('chika')
for name in names:
    if name == 'chika':
        break
    print(name)

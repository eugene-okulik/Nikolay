text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,'
    ' facilisis vitae semper at, dignissim vitae libero'

)
words = text.split()
for word in words:
    if ',' in word:
        print(word.replace(',', ' ing,'))
    elif '.' in word:
        print(word.replace('.', ' ing.'))
    else:
        print(word, ('ing'))


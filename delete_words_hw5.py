some_text = 'Некоторый текст абвс слоабвами содерабвщий абв'

def delete_some_words(simple):
    simple = list(filter(lambda x: 'абв' not in x, simple.split()))
    return " ".join(simple)

some_text = delete_some_words(some_text)
print(some_text)
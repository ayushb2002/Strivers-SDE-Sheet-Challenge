def reverseString(s: str) -> str:
    word = ''
    store = []
    for i in s:
        if i == ' ':
            if word!= '':
                store.append(word)
            word = ''
        else:
            word += i
    if word != '':
        store.append(word)
        
    store.reverse()
    return ' '.join(store)
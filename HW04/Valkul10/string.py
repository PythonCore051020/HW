def reverse(st):
    st = st.strip()
    word = st.split()
    word = word[::-1]
    st = ' '.join(word)
    return st


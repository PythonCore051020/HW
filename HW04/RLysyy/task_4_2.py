#Reversing Words in a String
def reverse(st):
    reverse_str = ' '.join((st.split())[::-1])
    return reverse_str

def correct_tail(body, tail):
    sub = body[::-1][0]
    if sub == tail:
        return True
    else:
        return False
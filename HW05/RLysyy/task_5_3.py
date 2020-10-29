def areYouPlayingBanjo(name):    
    result = name
    if name[0].upper() == 'R':
        result = result + ' plays banjo'
    else:
        result = result + ' does not play banjo'
    return result
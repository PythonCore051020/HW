#Jenny's secret message
def greet(name):
    greeting_name = ''
    if name == 'Johnny':
        greeting_name = 'my love'
    else:
        greeting_name = name
    return f'Hello, {greeting_name}!'

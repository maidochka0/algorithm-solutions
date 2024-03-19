def make_user(name, age):
    return {
        name: age
    }
def format_user(items):
    for i in items:
        return f'{i}, {items[i]}'
print(format_user(make_user('Bob', 42))
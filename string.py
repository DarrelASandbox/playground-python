# Strings are not mutables
# String interpolation (Use a variable in a string)
print('This is a string {}. {} {}'.format('ewww', 'Count', 'index',))
print('This is a string {2}. {0} {1}'.format('ewww', 'Count', 'index',))
print('This is a string {e}. {e} {e}'.format(e='ewww', c='Count', i='index',))

# float formatting {value:width.precision f}
result = 100/777
print('The result is {r:1.3f}'.format(r=result))

print(f'Hello, this is {str}')

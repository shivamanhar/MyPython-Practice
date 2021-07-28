#start with method is casesansitive

myString = 'Programming is cool! But some time hard'

result = myString.startswith('Pro')

print('Start string find {}'.format(result))

result = myString.endswith('time')

print('End string find {}'.format(result))
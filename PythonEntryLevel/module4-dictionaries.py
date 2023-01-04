# email_empty_dir = {}
#
# emails = {
#     'SPK': 'spk@gmail.com',
#     'PSK': 'psk@yahoo.com',
#     'ABC': 'abc@outlook.com',
#     'ABC': 'abc@live.com'       # will replace previous value
# }
#
# print(emails)
# print(emails.keys())
# print(emails.items())
# print(emails['SPK'])
# print(emails['ABC'])
#
# # key must be immutable, e.g list not allowed
# emails['PSK'] = 'psk@gmail.com'
# print(emails)
# emails.update({'ABC': 'abc@gmail.coom'})
# print(emails)
#
# print(len(emails))
#
# print('SPK' in emails)
# print('spk@gmail.com' in emails.values())
#
# del emails['ABC']
# print(len(emails))

# TRAVERSE
emails = {
    'SPK': 'spk@gmail.com',
    'PSK': 'psk@yahoo.com',
    'ABC': 'abc@outlook.com'
}

for key in emails:
    print(key)
print('---')
# same above and below
for key in emails.keys():
    print(key)
print('---')
for value in emails.values():
    print(value)
print('---')
for key, value in emails.items():
    print(key, '\'s email is', value)


# write
with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey bruce, python is awesome!')

# amend
with open('files/write.txt', 'a') as write_file:
    write_file.write('\nI love it so much! Python is awesome!')

# write lines
quotes = [
    '\nI can resist everything except templation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
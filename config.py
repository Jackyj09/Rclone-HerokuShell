import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('BOT_TOKEN')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('OWNER_ID'))
w.write('\n')
w.write('}')
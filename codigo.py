#importando bibliotecas necessárias
from googleapiclient.discovery import build
from google.oauth2 import service_account

#autenticação
credencial = service_account.Credentials.from_service_account_file('')

#cria o objeto da api do youtube
youtube = build('youtube', 'v3', credentials=credencial)

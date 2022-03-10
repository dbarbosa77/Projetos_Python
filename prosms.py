from twilio.rest import Client
import pandas as pd


# Your Account SID from twilio.com/console
account_sid = "AC5c2c0ce17b4d3dec37c9d5b53d901e97"
# Your Auth Token from twilio.com/console
auth_token  = "6695cb074c79351e76e963b959e80ff6"

client = Client(account_sid, auth_token)



lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio','junho']

for mes in lista_meses:
    tabela_vendas =pd.read_excel(f'C:\\Users\\Administrator\\Documents\\Python_Projetos\\LOCALIZARLISTA\\{mes}.xlsx')
    if (tabela_vendas['Vendas']> 55000).any():
        vendedor=tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendedor'].values[0]
        vendas=tabela_vendas.loc[tabela_vendas['Vendas']>55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+xxxxxxxxxxx", 
            from_="+16292191986",
            body=f'Em {mes}, o funcionário {vendedor} bateu a meta com total de {vendas} em vendas')
        print(message.sid)
        print(f'Em {mes}, o funcionário {vendedor} bateu a meta com total de {vendas} em vendas')
        
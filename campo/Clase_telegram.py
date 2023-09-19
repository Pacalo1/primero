# en esta biblioteca crearemos los metodos para mandar los mensages a telegram

class Telegram:
  atributo="valor"
  
  def Imprimir(self):
    print("lo imprimo")

  def Men_Telegram(self):
    print("mensage telegram")

    import requests
    token="5956058224:AAGLqlpOiBwi0RcjfkoEXlV6Z-Ce0t4-tH8"
    chat_id="5805918670"
    requests.post('https://api.telegram.org/bot'+ token +'/sendMessage',data={'chat_id': chat_id, 'text': "message"})

  def Men_entro(self,precio):
    
    import requests
    token="5956058224:AAGLqlpOiBwi0RcjfkoEXlV6Z-Ce0t4-tH8"
    chat_id="5805918670"
    mensage="entro en : " + precio
    requests.post('https://api.telegram.org/bot'+ token +'/sendMessage',data={'chat_id': chat_id, 'text': mensage})

  def Men_salio(self,precio):
    
    import requests
    token="5956058224:AAGLqlpOiBwi0RcjfkoEXlV6Z-Ce0t4-tH8"
    chat_id="5805918670"
    mensage="Salio en : " + precio
    requests.post('https://api.telegram.org/bot'+ token +'/sendMessage',data={'chat_id': chat_id, 'text': mensage})
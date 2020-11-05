import yagmail,configparser,json
config = configparser.ConfigParser()
config.read("conf")#Realizar leitura das configurações de acesso
sender=yagmail.SMTP(config['Mail']['username'],
                    config['Mail']['password'])
with open('emails.json') as json_file:
    data = json.load(json_file)#carregando json
    

assunto='Notificação Tutorial'
conteudo="""\
<html>
    <body>
        <p> Ola {nome}!</p>
        <p> Aprenda mais sobre Python em  <a href="https://www.tutorialspoint.com/python/index.htm">TutorialPythons</a></p>
    </body>
</html>

"""
for contato in data:
    sender.send(to=contato["email"],
                subject=assunto,
                contents=conteudo.format(nome = contato["name"]),
                attachments="README.md")
    print("Mensagem Enviada")


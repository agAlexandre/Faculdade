from cliente import Cliente
from servidor import Servidor
from mensagem import Mensagem
from dns import DNS
from time import sleep 
dns = DNS()
s1 = Servidor('gmail', dns)
s2 = Servidor('hotmail', dns)
s3 = Servidor('yahoo', dns)
dns.cadastrarServidor('gmail', s1)
dns.cadastrarServidor('hotmail', s2)
dns.cadastrarServidor('yahoo', s3)



gabriel = Cliente("Gozales","burrito",s1)
caio = Cliente("Caio","zica",s1)
alexandre = Cliente("Alexandre","thegreat",s2)
cachorrao = Cliente("cachorrao","lenis",s2)
marcao = Cliente("berranteiro","tbt",s3)
miguel= Cliente("Vinicius","PAIton",s3)


m1=Mensagem('gabriel','alexandre','hotmail.com',"teste","teste")
m2=Mensagem('gabriel','cachorrao','hotmail.com',"Saaalve","Saalve cachorro!")
m3=Mensagem('alexandre','marcao','yahoo.com.br',"Sdds","Liberdade vai canta")

m4=Mensagem('cachorrao','miguel','yahoo.com',"Aula LP 2","Ex dificil pra p***")
m5=Mensagem('miguel','alexandre','hotmail.com',"Aula LP 2","Ex dificil pra p***")
m6=Mensagem('miguel','gabriel','gmail.com',"Aula LP 2","Ex dificil pra p***")
m7=Mensagem('gabriel','caio','gmail.com',"Aula LP 2","Ex dificil pra p***")
m8=Mensagem('caio','miguel','yahoo.com.br',"Aula LP 2","Ex dificil pra p***")
s2.receberDeOutroServidor(m1)
s2.receberDeOutroServidor(m2)
s3.receberDeOutroServidor(m3)
s3.receberDeOutroServidor(m4)
s2.receberDeOutroServidor(m5)
s1.receberDeOutroServidor(m6)
s1.receberDeOutroServidor(m7)
s3.receberDeOutroServidor(m8)

mserver1=s1.getMensagens()
mserver2=s2.getMensagens()
mserver3=s3.getMensagens()
print('Mensagens contidas no S1:\n')
for x in mserver1:
    print(x,'\n-----------------------')
    sleep(2)
print('Mensagens contidas no S2:\n')
for y in mserver2:
    print(y,'\n-----------------------')
    sleep(2)
print('Mensagens contidas no S3:\n')
for z in mserver3:
    print(z,'\n-----------------------')
    sleep(2)

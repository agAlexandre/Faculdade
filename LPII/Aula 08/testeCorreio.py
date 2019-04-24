from cliente import Cliente
from servidor import Servidor
from mensagem import Mensagem
from dns import DNS

dns = DNS()
s1 = Servidor('gmail', dns)
s2 = Servidor('hotmail', dns)
s3 = Servidor('yahoo', dns)
dns.cadastrarServidor('gmail', s1)
dns.cadastrarServidor('hotmail', s2)
dns.cadastrarServidor('yahoo', s3)




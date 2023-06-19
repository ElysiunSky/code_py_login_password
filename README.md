# code_py_login_password
# Um breve conhecimento ao ponto de abordar o armazenamento de dados do usuário e de como devemos tratar ele, esse código permite o armazenamento desses dados e a reutilização dele no método login e senha.
Intúito geral do código:
  Um código que perminta a reacriação de um metodo de login, cadastro e senha de usuário, leitura de dados provenientes de autenticação, um código que não permite usuários com os mesmos nomes, nicka, logins iguais, isso ajudará na segurança de usuário.
  No metodo login: Você poderar realizar o login com um usuário e senha, que posteriormente você já tenha criado(esses dados são todos armazenados no local onde o arquivo do eu código se encontra)
  Cadastro: Nessa etapa, considera-se que você não tenha um usuário cadastrado no sistema, aqui será permitido que você crie um usuário, desde que o seu nick escolhido não já trnha sido escolhido por outro usuário.
  Depuração: Ao iniciar a prática do cadastro, o código irá buscar em seus arquivos se aquele usuário já existe, caso não exista, você podera partir para a próxima etapa, que seria a confirmação de login e senha, caso contrário, será retornado uma mensagem de erro informando que aquele usuário já existe e que você deverá escolher outro nome para proceguir com o processo.

Banco de dados:
  Esse código não faz uso de banco de dados para consultas internas, o seu banco de dados se dá na armazenagem de dados txt simples(bloco de notas) entretanto, é possível utilizar esse código para a armazenagens em banco de dados, basta realizar algumas mudanças simples, que você pode encontrar também nesse perfil, temos um código que mostra como é feito a administração básica de dados com python e mysql #ElysiunSky
  

Nesse código você poderá:
  Armazenar dados em um arquivo .txt
  Administrar os dados dependendo de sua necessidade
  Realizar depuração de dado, a leitura dele para poder tomar uma tomada de decisão

Todas as informações do imput serão armazenadas em arquivo bloco de notas sem perimetros de segurança, não há criptografia implementada no código, nem armazenamento seguro(binário ou codificação de input) as informaçõess serão armazenadas em arquivo de texto bruto de fácil acesso, os dados armazenados estarão vúlneráveis pois estão armazenados em texto.

##Atenção:
Realize o Download do código de forma segura, ou só abra o arquivo com o código na página web Github e copie o código. O código pode ser modificado e implementado amplamente com bibliotecas, assim tornando-o mais seguro e passivo de uso interno, evite usa-lo de forma exposta, a não ser que tenha modificado ele com perimetros essênciais de segurança(criptografia, módulos para evitar atacks simples e avançados) ressaltando que é possível implementar seguranças básicas utilizando bibliotecas de codificação e criptorafia avançadas, todas disponíveis pelo github word.

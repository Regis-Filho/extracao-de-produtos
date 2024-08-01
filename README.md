Kabum Web Scraper
Este script Python permite a extração de informações sobre produtos do site Kabum com base em uma consulta de pesquisa fornecida pelo usuário. Ele coleta o nome do produto, o preço e o link para a página do produto, salvando esses dados em um arquivo Excel.

Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Este script requer as seguintes bibliotecas Python:

pandas
BeautifulSoup (bs4)
requests
re
math
Você pode instalar essas bibliotecas usando pip:
pip install pandas beautifulsoup4 requests

Como usar
Executar o script: Execute o script em um ambiente Python.
Inserir a pesquisa: Quando solicitado, insira o termo de pesquisa para buscar produtos no site Kabum.

Aguardar a execução: O script irá percorrer as páginas de resultados, coletar os dados e salvar em um arquivo Excel nomeado com base no termo de pesquisa.

Estrutura do código
Importações: Importa as bibliotecas necessárias.
Headers: Define os cabeçalhos para a solicitação HTTP para imitar um navegador.
Pesquisa: Solicita ao usuário o termo de pesquisa.
URL de pesquisa: Formata a URL para a pesquisa no Kabum.
Requisição e parsing da página: Faz uma requisição à página de resultados e utiliza BeautifulSoup para parsear o HTML.
Quantidade de produtos: Extrai a quantidade de produtos encontrados.
Dicionário de dados: Inicializa um dicionário para armazenar os dados dos produtos.
Loop de páginas: Itera sobre as páginas de resultados, coletando nome, preço e link dos produtos.
Requisição de detalhes do produto: Faz uma requisição para cada página de produto para obter o preço.
Armazenamento dos dados: Armazena os dados coletados no dicionário.
Criação do DataFrame: Cria um DataFrame pandas com os dados coletados.
Salvamento em Excel: Salva os dados no arquivo Excel.
Mensagem final: Imprime uma mensagem indicando a conclusão.
Exemplo de saída
O arquivo Excel gerado conterá três colunas:

Nome: O nome do produto.
Preço: O preço do produto.
Links: O link para a página do produto.
Notas
Este script pode não funcionar corretamente se o layout do site Kabum mudar.
Algumas páginas de produtos podem falhar ao obter o preço devido a restrições do site ou a mudanças no layout da página do produto.

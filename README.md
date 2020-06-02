# Scrapper-Submarino

Essa aplicação tem como foco a retirada de dados do site submarino. 

### Sobre a aplicação

No momento há duas páginas de código na aplicação, uma é a parte lógica que fica na página\
scrapper.py a outra é app.py que fica responsável por rodar a aplicação. 

Esta aplicação faz o scrapper de todas as categorias contidas no arquivo categorias.txt

Basicamente ele entra em cada uma das categorias pega todos os livros e assim sucessivamente até
a lista de categorias acabar.  

### Sobre as funções

* next_page()
    * Responsável por navegar entre as páginas de livros, a medida que o a função get_all_books() solicitar.
* writing(name, data_set)
    * Responsável por escrever arquivos txt sempre que for chamada. 
* get_dirty_categories()
    * Pega todas as categorias da pagina em que se encontra o rodo. Ela retorna dados a mais, é feita uma correção desses dados
     na função get_categories()
* btn_click(xpath)
    * Clica em determinado botão de acordo com o xpath passado.
* get_categories()
    * Essa é a função principal, nela há toda a lógica que entra de página em página pegando dados de sub categoria.
* get_all_books()
    * Função pega os dados de livros de 4 páginas. Ela tem capacidade para mais, porém é colocado 4 no looping 
    para teste. 
    
### Como utilizar

Esse scrapper esta configurado para pegar apenas as duas primeiras paginas de cada categoria. Caso queira mais
será necessário alterar o for que há em get_all_books().

        for index in range(2, 3):
        books = browser.find_elements_by_xpath('//h2[@class="TitleUI-bwhjk3-15 khKJTM TitleH2-sc-1wh9e1x-1 fINzxm"]')
        prices = browser.find_elements_by_xpath('//*[@class = "PriceWrapper-bwhjk3-13 eBwWGp ViewUI-sc-1ijittn-6 '
                                                'iXIDWU"]')
                                            
Altere o range de (2, 3) para no maxímo (2, 23). Caso queira mais será necessário acessar o site e verificar\
quantas paginas cada sessão tem. 

Feito isso, rode o código e ele irá pegar os livros de cada uma das categorias, isso pode levar de uma a duas horas. 
Claro que isso é chutando alto, pode levar bem menos tempo.                                             
# Scrapper-Submarino

Essa aplicação tem como foco a retirada de dados do site submarino. 

### Sobre a aplicação

No momento há duas páginas de código na aplicação, uma é a parte lógica que fica na página\
scrapper.py a outra é app.py que fica responsável por rodar a aplicação. 

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
    
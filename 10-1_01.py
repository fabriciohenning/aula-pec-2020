codigo = 100
livros = {}

while True:
    titulo = input('Título: ').strip()

    if titulo == '':
        break

    isbn = input('ISBN: ').strip()
    autor = input('Autor: ').strip()
    preco = float(input('Preço: '))
    codigo += 1

    livro = titulo, isbn, autor, preco
    livros[codigo] = livro

for codigo in livros:
    titulo, isbn, autor, preco = livros[codigo]
    print(f'Código: {codigo}\nTítulo: {titulo}\nISBN: {isbn}\nAutor: {autor}\nPreço: {preco:.2f}')

def tag_bloco(conteudo, *args,  classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'< {tag} class = "{classe}" > {html} </{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco_inline', classe='info', inline=True))
    print(tag_bloco('bloco_inline2', inline=True))
    print(tag_bloco(tag_lista('item1', 'item2'), 'info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info',
                    inline=True))

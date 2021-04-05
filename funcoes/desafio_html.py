def tag(tag, *args, **kwargs):

    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')

    resultado1 = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    resultado2 = ''.join(args)
    return f'<{tag} {resultado1}>{resultado2}</{tag}>'


    # resultado = ''.join(f'< {tag} > )
if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Anna Januzzi', id='aj'),
            tag('span', ' e '),
            tag('strong', 'Saulo Januzzi', id='sj'),
            tag('span', '.'),
            html_class='alert'
            )
    )

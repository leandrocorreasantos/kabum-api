from api import log


config_frete = [
    {
        'codigo': 'ninja',
        'nome': 'Entrega Ninja',
        'constante': 0.3,
        'altura_minima': 10,
        'altura_maxima': 200,
        'largura_minima': 6,
        'largura_maxima': 140,
        'prazo_entrega': 6
    },
    {
        'codigo': 'kabum',
        'nome': 'Entrega KaBuM',
        'constante': 0.2,
        'altura_minima': 5,
        'altura_maxima': 140,
        'largura_minima': 13,
        'largura_maxima': 125,
        'prazo_entrega': 4
    }
]


def calcula_frete(largura, altura, peso):
    result = []
    for c in config_frete:
        frete = {}
        log.info("test {}".format(c['codigo']))
        if c['largura_minima'] <= largura <= c['largura_maxima']:
            if c['altura_minima'] <= altura <= c['altura_maxima']:
                frete['valor_frete'] = (peso * c['constante']) / 10
                frete['nome'] = c['nome']
                frete['prazo_entrega'] = c['prazo_entrega']
                log.info('frete: {}'.format(frete))
                result.append(frete)

    log.info('result: {}'.format(result))
    return result

def PegaSecuritizadora(text):
    try:
        Securitizadora = text.split(' como Securitizadora')[0].split('Emissão da ')[1]
    except:
        Securitizadora = 'Não foi possível determninar'
    return Securitizadora
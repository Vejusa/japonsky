hiragana = 0
katakana = 0

with open('pojaponsky.txt', encoding = 'utf-8') as mix:
    mixo = mix.read()
    with open('hiragana.txt', encoding = 'utf-8') as hira:
        hirao = hira.read()
        for riadok in mixo:
            for znak in riadok:
                for radek in hirao:
                    if znak in radek:
                        hiragana = hiragana + 1
        print('V texte je {} hiragana znakov.'.format(hiragana))

with open('pojaponsky.txt', encoding = 'utf-8') as mix:
    mixo = mix.read()
    with open('katakana.txt', encoding = 'utf-8') as kata:
        katao = kata.read()
        for riadok in mixo:
            for znak in riadok:
                for radek in katao:
                    if znak in radek:
                        katakana = katakana + 1
        print('V texte je {} katakana znakov.'.format(katakana))

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
if (alt<0 or larg<0):
    print('Altura ou largura inválida')
else:
    área = larg * alt
    print('Sua parede tea a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
    tinta = área / 2
    print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

from Classes.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('José',5)
restaurante_japones.receber_avaliacao('Jose',8)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
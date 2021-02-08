import pygame

pygame.init()


class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/muro - copia.jpg")
        self.rect = self.image.get_rect()

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


class Haku(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/hakuu.png")
        self.rect = self.image.get_rect()

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


class No_face(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/sincara.png")
        self.rect = self.image.get_rect()

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/coin.png")
        self.rect = self.image.get_rect()

    def dibujar_moneda(self, superficie):
        superficie.blit(self.image, self.rect)


class Chihiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/chihiro.png")
        self.rect = self.image.get_rect()

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


# mapa = [
#     [1, 0, 1, 2, 3, 1, 1, 1, 1, 1, 1],
#     [4, 0, 0, 1, 0, 0, 0, 3, 0, 0, 5],
#     [1, 1, 1, 1, 0, 1, 1, 2, 0, 1, 1],
# ]


def viajeChihiro(nodos):
    mapa = nodos[0].mapa
    iterador = iter(nodos)
    pared = Pared()
    chihiro = Chihiro()
    noFace = No_face()
    coin = Coin()
    haku = Haku()
    ANCHO = len(mapa[0]) * 80
    ALTO = len(mapa) * 80
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Viaje de Chihiro')
    reloj = pygame.time.Clock()
    game_over = False
    monedas = 0
    energia = 0

    def tiene_monedas(moneda):
        if moneda > 0:
            return True
        else:
            return False

    while not game_over:
        n = 2
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        mapa = next(iterador).mapa
                    except StopIteration:
                        print("Fin")
        # Fondo
        ventana.fill("skyblue")

        # ---------- Area de Dibujo
        coord_x = 0
        coord_y = 0

        # recorre el mapa y pinta una imagen u otra, dependiendo de que numero obtenga
        for fila in mapa:
            for columna in fila:
                if columna == 0:
                    pared.rect.x = coord_x
                    pared.rect.y = coord_y
                    pared.dibujar(ventana)
                elif columna == 4:
                    chihiro.rect.x = coord_x
                    chihiro.rect.y = coord_y
                    chihiro.dibujar(ventana)
                elif columna == 5:
                    haku.rect.x = coord_x + 10
                    haku.rect.y = coord_y
                    haku.dibujar(ventana)
                elif columna == 3:
                    noFace.rect.x = coord_x + 20
                    noFace.rect.y = coord_y + 10
                    noFace.dibujar(ventana)
                elif columna == 2:
                    coin.rect.x = coord_x + 10
                    coin.rect.y = coord_y + 10
                    coin.dibujar_moneda(ventana)

                coord_x += 80
            coord_x = 0
            coord_y += 80
        # Actualizar Pantalla
        # dibujar_mapa(ventana, listaMuro)
        pygame.display.flip()
    pygame.quit()

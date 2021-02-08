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


def viajeChihiro(nodos, nombre):
    nodo = nodos[0]
    mapa = nodo.mapa
    iterador = iter(nodos)
    pared = Pared()
    chihiro = Chihiro()
    noFace = No_face()
    coin = Coin()
    haku = Haku()
    ANCHO = len(mapa[0]) * 80 + 300
    ALTO = len(mapa) * 80
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Viaje de Chihiro: ' + nombre)
    reloj = pygame.time.Clock()
    game_over = False

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    while not game_over:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        nodo = next(iterador)
                        mapa = nodo.mapa
                    except StopIteration:
                        print("Fin")
        # Fondo
        ventana.fill("skyblue")
        # textsurface = myfont.render('Costo: '  + str(nodo.g()), False, (255, 255, 255))
        # ventana.blit(textsurface, (len(mapa[0])*80, 20))
        draw_string('Costo: ' + str(nodo.g()), len(mapa[0]) * 80, 20, ventana, myfont)
        draw_string('Monedas: ' + str(nodo.acumulated_coins), len(mapa[0]) * 80, 50, ventana, myfont)
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
        pygame.display.flip()
    pygame.quit()


def draw_string(string: str, x, y, ventana, font):
    textsurface = font.render(string, False, (255, 255, 255))
    ventana.blit(textsurface, (x, y))

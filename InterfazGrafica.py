import pygame

pygame.init()


class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\muro - copia.jpg").convert()
        self.rect = self.image.get_rect()


class Haku(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\hakuu.png").convert_alpha()
        self.rect = self.image.get_rect()


class No_face(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\sincara.png").convert_alpha()
        self.rect = self.image.get_rect()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\coin.png").convert_alpha()
        self.rect = self.image.get_rect()

    def dibujar_moneda(self, superficie):
        superficie.blit(self.image, self.rect)


class Chihiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\chihiro.png").convert_alpha()
        self.rect = self.image.get_rect()


# ----------Muros
def construir_mapa(mapa):
    listaMuros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "0":
                listaMuros.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80
    return listaMuros


def dibujar_muro(superficie, rectangulo):  # funcion para dibujar rectangulos
    pygame.draw.rect(superficie, VERDE, rectangulo)


def dibujar_mapa(superficie, listaMuro):  # Funcion que dibuja muros
    for muro in listaMuro:
        dibujar_muro(superficie, muro)


mapa = [
    "10123111111",
    "40010003005",
    "11110112011",
    "F"
]

ANCHO = len(mapa[0]) * 80
ALTO = (len(mapa)-1) * 80
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
SKYBLUE = (135, 206, 235)
movil = pygame.Rect(0, 0, 60, 60)
coord_x = 0
coord_y = 0
vel_x = 0
vel_y = 0
fondo = pygame.image.load("E:\PyCharm Projects\intentoPyGame\imagenes\968167.png")
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Muro')
reloj = pygame.time.Clock()

listaPared = pygame.sprite.Group()
pared = Pared()
listaPared.add(pared)

listaChihiro = pygame.sprite.Group()
chihiro = Chihiro()
listaChihiro.add(chihiro)

listaHaku = pygame.sprite.Group()
haku = Haku()
listaHaku.add(haku)

# listaCoin = pygame.sprite.Group()
# coin = Coin()
# listaCoin.add(coin)

listaNoFace = pygame.sprite.Group()
noFace = No_face()
listaNoFace.add(noFace)

listaMuro = construir_mapa(mapa)

game_over = False
haku_x = 0
haku_y = 0
noFace_x = 0
noFace_y = 0
coin_x = 0
coin_y = 0
monedas = 0
energia = 0
listaMonedas = []
cuenta_monedas = 0
cuenta_noface = 0

def tiene_monedas(moneda):
    if (moneda > 0):
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
            if event.key == pygame.K_UP:
                vel_y = - 5
            elif event.key == pygame.K_DOWN:
                vel_y = + 5
            elif event.key == pygame.K_LEFT:
                vel_x = - 5
            elif event.key == pygame.K_RIGHT:
                vel_x = + 5
        else:
            vel_y = 0
            vel_x = 0

    movil.x += vel_x
    movil.y += vel_y

    chihiro.rect.x = movil.x
    chihiro.rect.y = movil.y

    # verifica si hay choque con un muro
    for muro in listaMuro:
        if movil.colliderect(muro) or movil.x < 0 or movil.x >= ANCHO - 40 \
                or movil.y < 0 or movil.y >= ALTO - 40:
            movil.x -= vel_x
            movil.y -= vel_y

    # Fondo
    ventana.fill("skyblue")

    # ---------- Area de Dibujo
    coord_x = 0
    coord_y = 0


    # recorre el mapa y pinta una imagen u otra, dependiendo de que numero obtenga
    for fila in mapa:
        for columna in fila:
            if columna == "0":
                pared.rect.x = coord_x
                pared.rect.y = coord_y
                listaPared.add(pared)
                listaPared.draw(ventana)

            elif columna == "5":
                haku.rect.x = coord_x + 10
                haku.rect.y = coord_y
                haku_x = coord_x
                haku_y = coord_y

                listaHaku.add(haku)
                listaHaku.draw(ventana)
            elif columna == "3":
                noFace.rect.x = coord_x + 20
                noFace.rect.y = coord_y
                noFace_x = coord_x
                noFace_y = coord_y

                listaNoFace.add(noFace)
                listaNoFace.draw(ventana)
            elif columna == "2":
                coin = Coin()
                coin.rect.x = coord_x + 10
                coin.rect.y = coord_y
                coin_x = coord_x
                coin_y = coord_y
                listaMonedas.append(coin)
                for moneda in listaMonedas:
                    if movil.collidepoint(coin_x+20, coin_y):
                        listaMonedas.remove(moneda)
                        print("moneda")
                if len(listaMonedas)>0:
                    for monedita in listaMonedas:
                        monedita.dibujar_moneda(ventana)


            coord_x += 80
        coord_x = 0
        coord_y += 80
    listaChihiro.draw(ventana)

    # verifica si se encontró con Haku
    if movil.collidepoint(haku_x + 50, haku_y):
        print("Yupi, encontraste a tu amor")
    elif movil.collidepoint(noFace_x + 20, noFace_y):  # Verifica si se encontró con un sin cara
        energia += 1
        if tiene_monedas(monedas):
            energia -= 5
            monedas = 0
        print("Encontraste a matecho :0", energia)


    # Actualizar Pantalla
    # dibujar_mapa(ventana, listaMuro)
    pygame.display.flip()
pygame.quit()

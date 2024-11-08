import pygame
import random
import os

# Inicializando o pygame
pygame.init()

# Definindo as dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Bolinhas Aleatórias')

# Definindo as cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Função para desenhar bolinhas
def desenha_bolinhas(qtd_bolinhas):
    bolinhas = []
    tela.fill(BRANCO)  # Preenche a tela de branco
    
    # Gerando bolinhas em locais aleatórios
    for _ in range(qtd_bolinhas):
        x = random.randint(50, LARGURA_TELA - 50)
        y = random.randint(50, ALTURA_TELA - 50)
        raio = random.randint(20, 40)
        cor = random.choice([VERDE, AZUL, VERMELHO])
        pygame.draw.circle(tela, cor, (x, y), raio)
        bolinhas.append({'x': x, 'y': y, 'raio': raio, 'cor': cor})
    
    pygame.display.update()
    return bolinhas

# Função para salvar as informações das bolinhas em HTML
def salva_em_html(bolinhas):
    caminho_arquivo = "bolinhas_info.html"
    with open(caminho_arquivo, 'w') as f:
        f.write("<html>\n")
        f.write("<head><title>Informações das Bolinhas</title></head>\n")
        f.write("<body>\n")
        f.write("<h1>Bolinhas Aleatórias</h1>\n")
        f.write("<ul>\n")
        
        for i, bolinha in enumerate(bolinhas):
            f.write(f"<li><strong>Bolinhas {i+1}:</strong><br>\n")
            f.write(f"Posição: ({bolinha['x']}, {bolinha['y']})<br>\n")
            f.write(f"Raio: {bolinha['raio']} pixels<br>\n")
            f.write(f"Cor: {bolinha['cor']}<br>\n")
            f.write("</li>\n")
        
        f.write("</ul>\n")
        f.write("</body>\n")
        f.write("</html>\n")
    
    print(f"Informações salvas em {os.path.abspath(caminho_arquivo)}")

# Função principal
def main():
    clock = pygame.time.Clock()
    rodando = True
    qtd_bolinhas = 10  # Defina quantas bolinhas aparecerão

    bolinhas = []
    
    # Loop principal
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        bolinhas = desenha_bolinhas(qtd_bolinhas)  # Desenha as bolinhas aleatórias
        pygame.time.delay(1000)  # Espera 1 segundo (1000 ms) antes de gerar novamente as bolinhas

        # Após exibir as bolinhas por um tempo, salva as informações em HTML
        salva_em_html(bolinhas)
        break  # Vamos parar o programa após gerar e salvar as informações (pode remover este `break` para manter rodando)

    pygame.quit()

if __name__ == "__main__":
    main()

# projetinhos
É recomendado que você esteja utilizando a versão mais recente de Python para evitar problemas de compatibilidade.
Para saber mais sobre as versões, acesse https://www.python.org/downloads/ e baixe a versão mais recente.

***Projetinho de um aplicativo anti-inatividade que move o mouse sozinho dentro de um periodo específico de tempo.***

- Por padrão, o tempo de atuação do aplicativo é de 0.5 segundos, com duração de 0.5 segundos de animação(tempo que o mouse vai demorar pra deslocar o ponteiro).
Para alterar o tempo de duração e o tempo da animação, é necessario mudar alguns parametros dentro do codigo:

  
        pag.moveTo(x,y,.5) --> .5 é o tempo da animação. É necessário altes para um valor valido de segundos.
        time.sleep(.5) --> Tempo que o aplicativo espera até o próximo movimento. Tempo em segundos também.
        
É isso! Bom uso. O pixel-tracker é pra saber precisamente em qual área da tela o ponteiro se encontra, mas é apenas
pra uso técnico, não tem nenhuma outra funcionalidade.

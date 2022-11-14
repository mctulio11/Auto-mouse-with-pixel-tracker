# AM v1.3

***O que mudou da versão 1.0 pra versão 1.3***
1. O aplicativo não reportava a posição atual do ponteiro do mouse, mas sim a posição anterior a nova. O aplicativo agora
reporta a posição precisa do mouse e todo o trajeto de pixels que ele faz.
2. Adicionada uma nova interface pra facilidade de uso do aplicativo. Só tem um botão que ta escrito "Launch", não tem como errar.
*****************************************************************************************************************************************

É recomendado que você esteja utilizando a versão mais recente de Python para evitar problemas de compatibilidade.
Para saber mais sobre as versões, acesse https://www.python.org/downloads/ e baixe a versão mais recente.

***Projetinho de um aplicativo anti-inatividade que move o mouse sozinho dentro de um periodo específico de tempo.***

- Por padrão, o tempo de atuação do aplicativo é de 0.5 segundos, com duração de 0.5 segundos de animação(tempo que o mouse vai demorar pra deslocar o ponteiro).
Para alterar o tempo de duração e o tempo da animação, é necessario mudar alguns parametros dentro do codigo:

  
        pag.moveTo(x,y,.5) --> .5 é o tempo da animação. É necessário altes para um valor valido de segundos.
        time.sleep(.5) --> Tempo que o aplicativo espera até o próximo movimento. Tempo em segundos também.
        

O arquivo launcher.zip é a versão executável dos dois aplicativos em um só, pra economizar janela no seu pc.
A versão executável foi adicionada pra melhor compatibilidade com todos os publicos, nem todo mundo tem python instalado no PC.


É isso! Bom uso. O pixel-tracker é pra saber precisamente em qual área da tela o ponteiro se encontra, mas é apenas
pra uso técnico, não tem nenhuma outra funcionalidade.

Nota importante: Ainda não é possível alterar o tempo que o ponteiro leva pra ir de um ponto ao outro, mas eu to trabalhando numa solução e lanço 
o mais rápido possivel.

 
***mctulio11.

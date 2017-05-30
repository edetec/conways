[Conway’s	Game	of	Life](https://github.com/edetec/conways)
===========================

O	Jogo	da	vida	(Conway’s	Game	of	Life)	é	um	autômato	simples	que	se
comporta	de	acordo	com	as	seguintes	regras:
1.	 Cada	célula	está	morta	ou	viva;
2.	 As	células	estão	dispostas	em	um	tabuleiro	retangular;
3.	 Considere	os	extremos	direito	e	esquerdo	do	tabuleiro	como	se
estivessem	juntos,	assim	como	o	topo	e	a	parte	de	baixo;
4.	 Todas	as	células	tem	8	vizinhos	(incluindo	as	células	da
“borda”).	Por	exemplo:	A	célula	(2,2)	tem	os	vizinhos:	(1,1)
(1,2)	(1,3)	(2,1)	(2,3)	(3,1)	(3,2)	(3,3);
5.	 Não	se	esqueça	da	regra	3	(as	“bordas”	estão	conectadas).	Por
exemplo,	a	célula	(0,4)	tem	os	vizinhos:	(0,3)	(1,3)	(1,4)	(1,5)
(0,5)	(tamanho_x	-	1,	3)	(tamanho_x	-1,	4)	(tamanho_x-1,	5);
6.	 Qualquer	célula	viva	com	menos	de	dois	vizinhos	vivos	morre
de	solidão;
7.	 Qualquer	célula	viva	com	mais	de	três	vizinhos	vivos	morre	de
superpopulação;
8.	 Qualquer	célula	morta	com	exatamente	três	vizinhos	vivos	se
torna	uma	célula	viva;

Classe Game
--------
~~~python
    def	__init__(self,	x,	y,	setup=[]):
~~~
  * X:	número	de	linhas;
  * Y:	número	de	colunas;
  * setup:	Array	de	tuplas	(x,y)	indicando	quais	células	estão	vivas na	geração	0.	Ex:	 [(1,3),	(1,5),	(2,2)]    
~~~python    
    def	__str__(self):
~~~
Retorna	uma	representação	em	texto	do	estado	atual	do autômato utilizando os caracteres:
  * **X** : para celulas vivas
  * **-** : para celulas mortas    
~~~python    
    def	next_generation(self):
~~~
Avança	uma	geração.

Executar
--------
Para executar os testes

    $ python -m unittest test_game

Para executar um amostra

    $ python sample.py

### Docker ###
Para executar os testes

    $ docker-compose run game python -m unittest test_game

Para executar um amostra

    $ docker-compose run game

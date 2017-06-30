## P6 @ Faça visualização de dados eficazes

##### por José Ferraz Neto

### 1. RESUMO

O projeto apresentará informações relativas ao mercado de óleos lubrificantes no Brasil. O conjunto de dados é disponibilizado pela Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) órgão regulador setorial.

### 2. DESIGN

O conjunto de dados utilizado no projeto possui dimensão espacial. Dessa forma, os registros de volumes produzidos de óleo lubrificante possuem uma localidade atribuída, isto é, a unidade federativa o qual o óleo foi produzido. Assim, optou-se por criar um mapa temático para representar os volumes de produção associados a um determinado estado brasileiro.  

Dentro dos possíveis mapas a ser produzido, optou-se pelo [coroplético](https://pt.wikipedia.org/wiki/Mapa_coropl%C3%A9tico), que pode se utilizar de cores para codificar diferentes grandezas associadas a uma determinada região do mapa.

Em decorrência ao feedback recebido do Thiago Karashima optou-se por alterar a unidade dos dados volumétricos apresentados. Pela ordem de grandeza destes, a unidade metros cúbicos torna-se mais conveniente para apresentação dos mesmos.

Além disso, para uma melhor navegação na página os links que direcionam para outros sites, foram setados para abrirem em aba adicional do navegador. Por conseguinte, adicionou-se um pequeno texto apresentando detalhes sobre o período o qual os dados dizem respeito, além de um um link para os leitores que desejam ter informações mais detalhadas sobre óleos lubrificantes.

Apesar da sugestão recebida no feedback de Cristiane Costa sobre a inserção de uma legenda no gráfico, optou-se por não inserir uma paleta de cores na forma de legenda. A escala utilizada no gráfico se dá por quantis, portanto, a seleção de diferentes categorias de óleos lubrificantes acarreta em domínios distintos que por sua vez produzem intervalos de quantis diversos, produzindo mais um elemento dinâmico na visualização, podendo assim gerar um elemento de confusão no gráfico. Dessa forma, um texto explicando o conceito de mapas coropléticos é suficiente para o leitor ter consciência que cores mais escuras estão associados a maiores volumes de OLAC e vice-versa.  Além disso, ao posicionar o mouse sobre uma unidade da federação, aparecerá uma legenda flutuante com o volume produzido naquele dado estado.

### 3. FEEDBACK

#### 3.1 THIAGO KARASHIMA

- **O que você percebeu na visualização?**
  1. Ao clicar nos links (SIMP e Boletim), eu saio da visualização. Para manter o foco no seu conteúdo, seria melhor que abrisse uma nova aba no navegador. 
  2. Os volumes estão em L. Pela magnitude dos valores, seria melhor se estivessem em m³.
  3. A caixa que informa o volume de cada estado está muito distante do cursor. Dependendo da posição vertical do mapa na tela, a caixa fica oculta.


- **Que perguntas você tem sobre os dados?**

  1. Os dados se referem a qual período? Um ano, trimestre? Qual ano?
  2. Qual a diferença entre Isolante Tipo A e Isolante Tipo B?
  3. O que significa "OLAC"?

- **Que relacionamentos você percebeu?**

  1. A produção está concentrada nos estados RJ, SP e MG.
  2. Óleos lubrificantes para aviação são produzidos apenas em GO.

- **O que você acha que é o principal destaque dessa visualização?**

  Constatar que alguns estados não produzem óleos lubrificantes e que a produção está concentrada nos estados de RJ, SP e MG.

- **Existe algo que você não entende no gráfico?**

  Não.


#### **3.2 CRISTIANE COSTA**

- **O que você percebeu na visualização?**

  Uma explicação rápida da produção de óleos lubrificantes acabados no país.

- **Que perguntas você tem sobre os dados?**

  O que são os vários tons de azul no mapa?

- **Que relacionamentos você percebeu?**

  A medida que se escolhe os tipos de óleos, podemos perceber em quais estados são produzidos.

- **O que você acha que é o principal destaque dessa visualização?**

  A localização de produção dos diversos tipos de óleos registrados na ANP.

- **Existe algo que você não entende no gráfico?**

  Os tons de azul no gráfico. Acredito que tenha faltado uma legenda.

#### 3.3 SILVIO FRANK

- **O que você percebeu na visualização?**

  Os textos destacados, apresentam fontes diferentes o que causa desconforto na leitura:


- **Que relacionamentos você percebeu?**

  Poderia alocar também as informações por região?

- **O que você acha que é o principal destaque dessa visualização?**

  A estratificação de dados por região com a possibilidade de escolha dos dados a serem mostrados.

- **Existe algo que você não entende no gráfico?**

  Não.

- **Comentário adicional**

  Eu fiz o teste e identifiquei que a aplicação não abre corretamente nos browsers  Mozila e Internet Explorer.

  ​
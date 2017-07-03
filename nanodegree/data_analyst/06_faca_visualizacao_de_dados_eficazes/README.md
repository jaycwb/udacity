## P6 @ Faça visualização de dados eficazes

##### por José Ferraz Neto

### 1. RESUMO

O projeto apresentará informações relativas ao mercado de óleos lubrificantes no Brasil. O conjunto de dados é disponibilizado pela [Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)](http://www.anp.gov.br/wwwanp/), órgão regulador setorial.

### 2. DESIGN

A ANP por meio da da Superintendência de Abastecimento (SAB) publica o Boletim de Lubrificantes fornecendo informações atualizadas sobre o mercado brasileiro de lubrificantes com dados retirados do sistema [SIMP - Sistema de Informações de Movimentação de Produtos](http://www.anp.gov.br/SITE/EXTRAS/SITE_SIMP/INDEX.asp). Em conjunto com o Boletim, é fornecido uma série de Anexos, que são os dados brutos utilizados na produção do Boletim.

O conjunto de dados utilizado no projeto possui dimensão espacial. Dessa forma, os registros de volumes produzidos de óleo lubrificante possuem uma localidade atribuída, isto é, a unidade federativa o qual o óleo foi produzido. Assim, optou-se por criar um mapa temático para representar os volumes de produção associados a um determinado estado brasileiro.  

Dentro dos possíveis mapas a ser produzido, optou-se pelo [coroplético](https://pt.wikipedia.org/wiki/Mapa_coropl%C3%A9tico), que pode se utilizar de cores para codificar diferentes grandezas associadas a uma determinada região do mapa.

A primeira versão do projeto o qual foi submetido a Feedback do voluntário Thiago Karashima foi está contido no arquivo **index.html**.

Em decorrência ao feedback recebido do Thiago Karashima optou-se por alterar a unidade dos dados volumétricos apresentados. Pela ordem de grandeza destes, a unidade metros cúbicos torna-se mais conveniente para apresentação dos mesmos.

Além disso, para uma melhor navegação na página os links que direcionam para outros sites, foram setados para abrirem em aba adicional do navegador. Por conseguinte, adicionou-se um pequeno texto apresentando detalhes sobre o período o qual os dados dizem respeito, além de um um link para os leitores que desejam ter informações mais detalhadas sobre óleos lubrificantes.

A consolidação das alterações recebidas pelo feedback acima estão contidas no arquivo **index_1.html** .

Apesar da sugestão recebida no feedback de Cristiane Costa sobre a inserção de uma legenda no gráfico, optou-se por não inserir uma paleta de cores na forma de legenda. A escala utilizada no gráfico se dá por quantis, portanto, a seleção de diferentes categorias de óleos lubrificantes acarreta em domínios distintos que por sua vez produzem intervalos de quantis diversos, produzindo mais um elemento dinâmico na visualização, podendo assim gerar um elemento de confusão no gráfico. Dessa forma, um texto explicando o conceito de mapas coropléticos é suficiente para o leitor ter consciência que cores mais escuras estão associados a maiores volumes de OLAC e vice-versa.  Além disso, ao posicionar o mouse sobre uma unidade da federação, aparecerá uma legenda flutuante com o volume produzido naquele dado estado.

As alterações realizadas em decorrência do feedback de Cristiane Costa estão contidas no arquivo **index_2.html**.

Apenas um feedback (Silvio Frank) relatou incômodo com a adoção de cores destacadas e fontes diferentes para realçar certos aspectos do texto, portanto, decidiu-se manter esses elmentos para chamar a atenção a conceitos chaves na apresentação da visualização.

As alterações realizadas em decorrência do feedback de Silvio Frank estão representadas no arquivo **index_3.html**.

Com o consolidado de 3 feedbacks foram levantadas algumas perguntas e ideias sugeridas a serem respondidas pelo conjunto de dados escolhido para o projeto. Desse modo, optou-se por criar um diagrama de Sankey para representar o fluxo de comercialização de óleo lubrificante no Brasil.

Essa nova visualização foi agregada ao projeto e o resultado está consolidado no arquivo **index_4.html**.

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

  Os textos destacados, apresentam fontes diferentes o que causa desconforto na leitura.


**Que relacionamentos você percebeu?**

Poderia alocar também as informações por região?

**O que você acha que é o principal destaque dessa visualização?**

A estratificação de dados por região com a possibilidade de escolha dos dados a serem mostrados.

**Existe algo que você não entende no gráfico?**

Não.

**Comentário adicional**

Eu fiz o teste e identifiquei que a aplicação não abre corretamente nos browsers  Mozila e Internet Explorer.

### 4. RECURSOS

1. [http://bl.ocks.org/enjoylife/4e435d329c2c743da33e](http://bl.ocks.org/enjoylife/4e435d329c2c743da33e)
2. [https://stackoverflow.com/questions/13632169/using-viewbox-to-resize-svg-depending-on-the-window-size](https://stackoverflow.com/questions/13632169/using-viewbox-to-resize-svg-depending-on-the-window-size)
3. [https://stackoverflow.com/questions/9400615/whats-the-best-way-to-make-a-d3-js-visualisation-layout-responsive](https://stackoverflow.com/questions/9400615/whats-the-best-way-to-make-a-d3-js-visualisation-layout-responsive)
4. [http://www.cartographicperspectives.org/index.php/journal/article/view/cp78-sack-et-al/1359](http://www.cartographicperspectives.org/index.php/journal/article/view/cp78-sack-et-al/1359)
5. [https://github.com/topojson/topojson](https://github.com/topojson/topojson)
6. [http://www.jeromecukier.net/blog/2011/08/11/d3-scales-and-color/](http://www.jeromecukier.net/blog/2011/08/11/d3-scales-and-color/)
7. [http://maptimesea.github.io/2015/01/07/d3-mapping.html](http://maptimesea.github.io/2015/01/07/d3-mapping.html)
8. [http://synthesis.sbecker.net/articles/2012/07/18/learning-d3-part-7-choropleth-maps](http://synthesis.sbecker.net/articles/2012/07/18/learning-d3-part-7-choropleth-maps)
9. [https://d3-geomap.github.io/map/choropleth/us-states/](https://d3-geomap.github.io/map/choropleth/us-states/)
10. [http://www.stator-afm.com/tutorial/d3-js-mouse-events/](http://www.stator-afm.com/tutorial/d3-js-mouse-events/)
11. [http://learnjsdata.com/](http://learnjsdata.com/)
12. [https://bost.ocks.org/mike/join/](https://bost.ocks.org/mike/join/)
13. https://www.packtpub.com/web-development/learning-d3js-mapping
14. https://www.packtpub.com/web-development/d3js-cutting-edge-data-visualization
15. [https://github.com/d3/d3-queue](https://github.com/d3/d3-queue)
16. http://christophergandrud.github.io/d3Network/


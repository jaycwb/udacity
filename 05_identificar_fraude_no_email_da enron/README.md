## P5 @ Identificar Fraude no Email da Enron

##### por José Ferraz Neto

#### 1. Introdução

Fundada em 1985 a Enron se dedicava a exploração de gás natural e produção de energia de diversos tipos, mas ao longo dos anos também começou a diversificar a sua carteira de investimentos, incluindo áreas como freqüência de internet, gerenciamento de risco e derivativo climático (um tipo de seguro climático para negócios sazonais). Seu crescimento chegou a ser tão assombroso que se converteram na sétima maior companhia norte-americana<sup>[1](http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron)</sup>. 

Mas foi no ano de 2001 que foi revelado ao mundo uma enorme fraude corporativa o qual revelou uma série de lucros não existentes que estavam sendo lançados nos registros contábeis da empresa.

Tecnicamente, a Enron utilizou empresas coligadas e controladas para inflar seu resultado, uma prática comum nas empresas. Através de SPE´s (Special Purpose Entities), a empresa transferia passivos, camuflava despesas, alavancava empréstimos, leasings, securitizações e montava arriscadas operações com derivativos<sup>[2](http://www.provedor.nuca.ie.ufrj.br/eletrobras/artigos/schmitt1.htm)</sup>. 

Dessa forma, o objetivo desse projeto é analisar um conjunto de dados que reúnem diversas informações sobre os funcionários que trabalhavam na Enron à época do escândalo e predizer quais desses funcionários são *person of interest* ("POI"). Para isso serão utilizados algoritmos de *machine learning* implementados por meio da biblioteca *[scikit-learn](http://scikit-learn.org/stable/)* uma biblioteca de *python*.

#### 2. Perguntas

> Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?  

O objetivo do projeto é o desenvolvimento de um modelo preditivo, a partir de dados financeiros e de atributos de emails dos funcionários da Enron, que objetiva determinar se uma pessoa é uma *person of interest* (`POI`), isto é, se essa estava envolvida no escândalo deflagrado em 2001.

O *dataset* possui o atributo `POI` que é a indicação se uma determinada pessoa esteve envolvida na fraude ou não, portanto, como existe uma pré-classificação definida dos dados a melhor abordagem de *machine learning* se dá por algoritmos de classificação supervisionada.

O *dataset* é composto por 146 registros cada um deles contendo 20 *features*, das quais 14 são características financeiras e as demais são derivadas de atributos dos emails, além do *label* `POI`.

A partir da análise dos dados disponibilizados foi possível constatar a existência de três registros que podem ser considerados como *outliers* dentro do contexto desse *dataset*.

- `LOCKHART EUGENE E` : Não há dados associados a essa pessoa, portanto, não há sentido de manter o registro para construção do modelo.
- `THE TRAVEL AGENCY IN THE PARK` : Definitivamente esse não é um nome associado a uma pessoa, logo, não irá colaborar com informação útil ao desenvolvimento do modelo.
- `TOTAL ` : Esse registro ao que indica contem os valores agregados de todas as pessoas do *dataset*.

Após a retirada dos 3 registros acima, o dataset resultou em 143 registros dos quais 13 são assinalados como sendo *<u>person of interest</u>*, desse modo o trabalho de modelagem apresenta-se como uma classificação supervisionada com classes desbalanceadas.

> What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.
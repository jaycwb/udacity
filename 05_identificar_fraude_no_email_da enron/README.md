## P5 @ Identificar Fraude no Email da Enron

##### por José Ferraz Neto

#### 1. Introdução

Fundada em 1985 a Enron se dedicava a exploração de gás natural e produção de energia de diversos tipos, mas ao longo dos anos também começou a diversificar a sua carteira de investimentos, incluindo áreas como freqüência de internet, gerenciamento de risco e derivativo climático (um tipo de seguro climático para negócios sazonais). Seu crescimento chegou a ser tão assombroso que se converteram na sétima maior companhia norte-americana. <sup>[1](http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron)</sup>

Mas foi no ano de 2001 que foi revelado ao mundo uma enorme fraude corporativa o qual revelou uma série de lucros não existentes que estavam sendo lançados nos registros contábeis da empresa.

Tecnicamente, a Enron utilizou empresas coligadas e controladas para inflar seu resultado, uma prática comum nas empresas. Através de SPE´s (Special Purpose Entities), a empresa transferia passivos, camuflava despesas, alavancava empréstimos, leasings, securitizações e montava arriscadas operações com derivativos. <sup>[2](http://www.provedor.nuca.ie.ufrj.br/eletrobras/artigos/schmitt1.htm)</sup>

Dessa forma, o objetivo desse projeto é analisar um conjunto de dados que reúnem diversas informações sobre os funcionários que trabalhavam na Enron à época do escândalo e predizer quais desses funcionários são *person of interest* ("POI"). Para isso serão utilizados algoritmos de *machine learning* implementados por meio da biblioteca *scikit-learn* uma biblioteca de *python*.
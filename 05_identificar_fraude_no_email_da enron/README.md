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

O *dataset* é composto por 146 registros cada um deles contendo 20 *features*, das quais 14 são características financeiras e as demais são derivadas de atributos dos emails, além do *label* `POI`. A seguir a listagem de todas as *features* originais do *dataset*.

```
atributos financeiros: ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (todos em dólares americanos (USD))
```

```
atributos de email: ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages',
'from_this_person_to_poi', 'shared_receipt_with_poi'] (as unidades aqui são geralmente em número de emails; a exceção notável aqui é o atributo ‘email_address’, que é uma string)
```

A partir da análise dos dados disponibilizados foi possível constatar a existência de três registros que podem ser considerados como *outliers* dentro do contexto desse *dataset*.

- `LOCKHART EUGENE E` : Não há dados associados a essa pessoa, portanto, não há sentido de manter o registro para construção do modelo.
- `THE TRAVEL AGENCY IN THE PARK` : Definitivamente esse não é um nome associado a uma pessoa, logo, não irá colaborar com informação útil ao desenvolvimento do modelo.
- `TOTAL ` : Esse registro ao que indica contem os valores agregados de todas as pessoas do *dataset*.

Após a retirada dos 3 registros acima, o dataset resultou em 143 registros dos quais 13 são assinalados como sendo *<u>person of interest</u>*, desse modo o trabalho de modelagem apresenta-se como uma classificação supervisionada com classes desbalanceadas.

> What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.



> What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?





> What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier)



> What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?



> Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance.



|       ALGORITMO        | PRECISÃO | RECALL  |
| :--------------------: | :------: | :-----: |
| DecisionTreeClassifier | 0.30005  | 0.96750 |
|   LogisticRegression   | 0.25924  | 0.59650 |
| Support Vector Machine | 0.16689  | 0.06250 |

Os autores Jake Lever, Martin Krzywinski e Naomi Altman publicaram no período científico **[nature methods](http://www.nature.com/nmeth/journal/v13/n8/full/nmeth.3945.html)** um excelente artigo denominado *Points of Significance: Classification evaluation* o qual discorrem sobre a avaliação de algortimos de classificação. Os autores de forma didática apresentam no referido artigo a figura abaixo que, de forma muito didática, apresentam a matriz de confusão e as diversas métricas possíveis de obter a partir dela.

<p align="center"> <img src="https://github.com/netoferraz/udacity/blob/master/05_identificar_fraude_no_email_da%20enron/pics/confusion_matrix_paper.png">  </p>




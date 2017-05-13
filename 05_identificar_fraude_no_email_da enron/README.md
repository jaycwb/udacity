## P5 @ Identificar Fraude no Email da Enron

##### por José Ferraz Neto

#### 1. Introdução

Fundada em 1985 a Enron se dedicava a exploração de gás natural e produção de energia de diversos tipos, mas ao longo dos anos também começou a diversificar a sua carteira de investimentos, incluindo áreas como freqüência de internet, gerenciamento de risco, entre outros. Seu crescimento chegou a ser tão assombroso que se converteram na sétima maior companhia norte-americana<sup>[1](http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron)</sup>. 

Mas foi no ano de 2001 que foi revelado ao mundo uma enorme fraude corporativa o qual revelou uma série de lucros não existentes que estavam sendo lançados nos registros contábeis da empresa. Tecnicamente, a Enron utilizou empresas coligadas e controladas para inflar seu resultado, uma prática comum nas empresas. Através de SPE´s (*Special Purpose Entities*), a empresa transferia passivos, camuflava despesas, alavancava empréstimos, leasings, securitizações e montava arriscadas operações com derivativos<sup>[2](http://www.provedor.nuca.ie.ufrj.br/eletrobras/artigos/schmitt1.htm)</sup>. 

Dessa forma, o objetivo desse projeto é analisar um conjunto de dados que reúnem diversas informações sobre os funcionários que trabalhavam na Enron à época do escândalo e predizer quais desses funcionários são *person of interest* ("POI"). Para isso serão utilizados algoritmos de *machine learning* implementados por meio da biblioteca *[scikit-learn](http://scikit-learn.org/stable/)* implementada em *python*.

#### 2. Perguntas

> Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?  

O objetivo do projeto é o desenvolvimento de um modelo preditivo, a partir de dados financeiros e de atributos de emails dos funcionários da Enron, para determinar se uma pessoa é uma *person of interest* (`POI`), isto é, se essa estava envolvida no escândalo deflagrado em 2001.

O *dataset* possui o *label* `POI` que é a indicação se uma pessoa esteve envolvida na fraude ou não, portanto, como existe uma pré-classificação definida dos dados a melhor abordagem se dará por algoritmos de classificação supervisionada.

O *dataset* é composto por 146 registros cada um deles contendo 20 *features*, das quais 14 são características financeiras e as demais são derivadas de atributos dos emails, além do *label* `POI`. A seguir a listagem de todas as *features* originais do *dataset*.

```
atributos financeiros: ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (todos em dólares americanos (USD))
```

```
atributos de email: ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages',
'from_this_person_to_poi', 'shared_receipt_with_poi'] 
```

A partir da análise dos dados disponibilizados foi possível constatar a existência de três registros que podem ser considerados como *outliers* dentro do contexto desse *dataset*.

- `LOCKHART EUGENE E` : Não há dados associados a essa pessoa, portanto, não há sentido de manter o registro para construção do modelo.
- `THE TRAVEL AGENCY IN THE PARK` : Definitivamente esse não é um nome associado a uma pessoa, logo, não irá colaborar com informação útil ao desenvolvimento do modelo.
- `TOTAL ` : Esse registro ao que indica contem os valores agregados de todas as pessoas do *dataset*.

Após a retirada dos 3 registros acima, o dataset resultou em 143 registros dos quais 18 são assinalados como sendo *<u>person of interest</u>*, desse modo o trabalho de modelagem apresenta-se como uma classificação supervisionada com classes desbalanceadas.

> What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.

A partir dos dados originais foram criadas mais duas features:

- from_this_person_to_poi_ratio
- from_poi_to_this_person_ratio

A primeira é a proporção dos emails enviados por uma dada pessoa com destino a algum `POI`em relação ao total de emails enviados pela pessoa, enquanto a segunda *feature* é a proporção dos emails recebidos de uma dada pessoa enviados por algum `POI`em relação ao total de emails recebidos pela dada pessoa.

No processo de pré-processamento dos dados optou-se por realizar uma redução de dimensionalidade dos dados por meio do uso de PCA, portanto, para que não fosse perdido informação alguma e capturar a maior variância possível dos dados não foi realizado nenhum processo de *feature selection*, portanto, o PCA foi realizado no dataset com todas as features disponíveis, além das recém criadas. 

Além disso, como as *features* possuem diferentes ordens de grandeza foi realizada uma padronização por meio do *StandardScaler()* de modo a evitar que uma *feature* que possua uma ordem de grandeza muito superior as demais seja a responsável por grande parte da variância dos dados.

Para o modelo otimizado de acordo com *Pipeline* abaixo:

```
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
 svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini',...plit=4, min_weight_fraction_leaf=0.0,presort=False, random_state=42, splitter='best'))])
```

O *GridSearchCV* otimizou o Pipeline de maneira que se utiliza apenas 1 componente principal da PCA e a `feature_importances_`do algoritmo *DecisionTreeClassifier* resultou que essa única dimensão representa 100% de importância.

> What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?

- DecisionTreeClassifier()
- LogisticRegression()
- SVC()

Pela tabela abaixo é possível constatar que o classificador DecisionTreeClassifier possui o melhor *Recall*, enquanto que o SVC registra a melhor métrica para *Precision*.

|       ALGORITMO        | PRECISION | RECALL  |
| :--------------------: | :-------: | :-----: |
| DecisionTreeClassifier |  0.32358  | 0.41450 |
|   LogisticRegression   |  0.48028  | 0.10350 |
|          SVC           |  0.46881  | 0.11650 |

> What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier)



> What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?



> Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance.

A partir da construção do *Pipeline* com 3 algoritmos - *DecisionTree, LogisticRegression e Support Vector Machine* - bem como a otimização de alguns de seus parâmetros por meio do *GridSearchCV*, foi possível otimizar os algoritmos que tem seus respectivos desempenhos ilustrados pelas métricas *accuracy*, *precision* e *recall*. 

##### ALGORITMO 1:



|       ALGORITMO        | ACCURACY | RECALL  | PRECISION |
| :--------------------: | :------: | :-----: | :-------: |
| DecisionTreeClassifier | 0.69473  | 0.96750 |  0.30005  |
|   LogisticRegression   | 0.71893  | 0.59650 |  0.25924  |
| Support Vector Machine | 0.83340  | 0.06250 |  0.16689  |

No que concerne a avaliação de algoritmos de classificação, os autores Jake Lever, Martin Krzywinski e Naomi Altman publicaram no período científico **[nature methods](http://www.nature.com/nmeth/journal/v13/n8/full/nmeth.3945.html)** um excelente artigo denominado *Points of Significance: Classification evaluation* o qual discorrem sobre diversas métricas utilizadas na avaliação de algortimos de classificação. O referido artigo apresenta a figura abaixo que, de forma muito didática, explica a matriz de confusão e as diversas métricas possíveis de obter a partir dela.

<p align="center"> <img src="https://github.com/netoferraz/udacity/blob/master/05_identificar_fraude_no_email_da%20enron/pics/confusion_matrix_paper.png">  </p>

A métrica *accuracy* corresponde a fração das predições que foram realizadas corretamente. Dos três algoritmos otimizados o *Support Vector Machine* foi aquele que obteve um maior valor, apesar da fácil interpretação dessa métrica, um maior *accuracy* não significa necessariamente um bom estimador. Essa métrica só é adequada quando o número de instâncias de cada classe no *dataset* é balanceada, caso exista uma assimetria na distribuição das classes esse estimador poderá predizer a classe majoritária com maior frequência resultando em uma excelente performance em termos de *accuracy*, todavia, deixa a desejar como classificador. 

Para o caso particular da nossa análise menos de 15% do *dataset* corresponde a `POI's`, portanto, trata-se de uma distribuição bastante assimétrica. Nesse contexto, a ocorrência de **Falsos Positivos** (FP) e/ou **Falsos Negativos** torna-se ainda mais relevante e a métrica *accuracy* não informa nada a respeito da ocorrência dessas circunstâncias. 

Desse modo, para o problema dos funcionários da Enron um **FP** significa que o classificador estará apontando uma pessoa como `POI`quando na realidade ela não é, enquanto que o **FN** é classificar um `POI`como inocente.

O *Recall* ou sensibilidade representa a proporção dos `POIs` preditos corretamente em relação a todos aqueles que de fato são `POI`, essa métrica também é conhecida como *True Positive Rate* (TPR).

Por último e não menos importante, temos a *Precision* que corresponde a proporção dos `POIs`preditos corretamente em relação a todos aqueles que são preditos como `POI`.

Com os scores apresentados, podemos interpretar os classificadores de forma mais adequada. Vamos considerar que o objetivo é apresentar um modelo preditivo para a equipe encarregada da investigação do escândalo da Enron, portanto, o classificador deve indicar os nomes dos funcionários que devem ser investigados ao longo da operação.

Dessa modo, investigar um inocente por considerá-lo um `POI` é mais tolerável do que deixar de investigar um criminoso por não considerá-lo um `POI`. O primeiro caso é o típico **FP** ou **Erro do Tipo I**, em contrapartida o segundo caso é um exemplo de **FN** ou **Erro do Tipo II**.

A seguir encontra-se os dados  do *Pipeline* que foi otimizado com o algoritmo (*DecisionTreeClassifier*) que gerou o melhor resultado.

```
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini', max_dept...plit=3, min_weight_fraction_leaf=0.0, presort=False, random_state=42, splitter='best'))])
```

O resultado da matriz de confusão desse estimador no arquivo de validação/avaliação `tester.py` está apresentado abaixo:

|  **True positives**   |   1935    |
| :-------------------: | :-------: |
|  **False positives**  | **4514**  |
|  **False negatives**  |  **65**   |
|  **True negatives**   | **8486**  |
| **Total predictions** | **15000** |

O referido algortimo possui um Recall de 0,9675, isto é, em 96,75% das vezes aquelas pessoas que de fato são `POI` são preditas como `POI`. Portanto, uma incidência de **Falso Negativo** muito baixa. 

Na simulação realizada pelo `tester.py` das 15000 predições realizadas, apenas 65 (0,43%) são **FN**. Desse modo, o classificador comete um **Erro do Tipo 2** em 3,25% das vezes que realiza uma predição, ou seja, aproximadamente, a cada 100 pessoas que de fato são `POI`apenas 3 delas não são preditas como `POI`.

Em contrapartida, o mesmo classificador possui uma *Precision* de 0.3000, isto significa que em 30% das vezes aqueles que são preditos como `POI` são de fato `POI`. Portanto, o nosso estimador possui um calcanhar de Aquiles que chama-se **Falsos Positivos**. No contexto dos dados da Enron, significa dizer que o classificador estará cometendo um **Erro do Tipo I** 
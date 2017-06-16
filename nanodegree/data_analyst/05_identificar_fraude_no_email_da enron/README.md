## P5 @ Identificar Fraude no Email da Enron

##### por José Ferraz Neto

#### 1. Introdução

Fundada em 1985 a Enron se dedicava a exploração de gás natural e produção de energia de diversos tipos, mas ao longo dos anos também começou a diversificar a sua carteira de investimentos, incluindo áreas como freqüência de internet, gerenciamento de risco, entre outros. Seu crescimento chegou a ser tão assombroso que se converteram na sétima maior companhia norte-americana<sup>[1](http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron)</sup>. 

Mas foi no ano de 2001 que foi revelado ao mundo uma enorme fraude corporativa o qual revelou uma série de lucros não existentes que estavam sendo lançados nos registros contábeis da empresa. Tecnicamente, a Enron utilizou empresas coligadas e controladas para inflar seu resultado, uma prática comum nas empresas. Através de SPE´s (*Special Purpose Entities*), a empresa transferia passivos, camuflava despesas, alavancava empréstimos, leasings, securitizações e montava arriscadas operações com derivativos<sup>[2](http://www.provedor.nuca.ie.ufrj.br/eletrobras/artigos/schmitt1.htm)</sup>. 

Dessa forma, o objetivo desse projeto é analisar um conjunto de dados que reúnem diversas informações sobre os funcionários que trabalhavam na Enron à época do escândalo e predizer quais desses funcionários são *person of interest* ("POI"). Para isso serão utilizados algoritmos de *machine learning* implementados por meio da biblioteca *[scikit-learn](http://scikit-learn.org/stable/)* implementada em *python*.

O código implementando toda a análise encontra-se no arquivo `/projeto/poi_id.py`.

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

Pela análise do *dataset* foi constatado que muitas instâncias possuíam *features* sem valores atribuídos. A tabela abaixo sumariza o quantitativo de valores ausentes por *feature*.

|          FEATURE          | TOTAL DE VALORES AUSENTES |
| :-----------------------: | :-----------------------: |
|          salary           |            49             |
|        to_messages        |            57             |
|     deferral_payments     |            105            |
|      total_payments       |            20             |
|  exercised_stock_options  |            42             |
|           bonus           |            62             |
|       director_fees       |            127            |
| restricted_stock_deferred |            126            |
|     total_stock_value     |            18             |
|         expenses          |            49             |
|  from_poi_to_this_person  |            57             |
|       loan_advances       |            140            |
|       from_messages       |            57             |
|           other           |            52             |
|  from_this_person_to_poi  |            57             |
|            poi            |             0             |
|      deferred_income      |            95             |
|  shared_receipt_with_poi  |            57             |
|     restricted_stock      |            34             |
|    long_term_incentive    |            78             |

A partir da análise dos dados disponibilizados foi possível constatar a existência de três registros que podem ser considerados como *outliers* dentro do contexto desse *dataset*.

- `LOCKHART EUGENE E` : Não há dados associados a essa pessoa, portanto, não há sentido de manter o registro para construção do modelo.
- `THE TRAVEL AGENCY IN THE PARK` : Definitivamente esse não é um nome associado a uma pessoa, logo, não irá colaborar com informação útil ao desenvolvimento do modelo.
- `TOTAL ` : Esse registro ao que indica contem os valores agregados de todas as pessoas do *dataset*.

Após a retirada dos 3 registros acima, o dataset resultou em 143 registros dos quais 18 são assinalados como sendo *<u>person of interest</u>*, desse modo o trabalho de modelagem apresenta-se como uma classificação supervisionada com classes desbalanceadas.

> What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.

A partir dos dados originais foram criadas mais duas features:

<<<<<<< HEAD
- from_this_person_to_poi_ratio
- from_poi_to_this_person_ratio

A primeira é a proporção dos emails enviados por uma dada pessoa com destino a algum `POI`em relação ao total de emails enviados pela pessoa, enquanto a segunda *feature* é a proporção dos emails recebidos de uma dada pessoa enviados por algum `POI`em relação ao total de emails recebidos pela dada pessoa.

No processo de pré-processamento dos dados optou-se por realizar uma redução de dimensionalidade dos dados por meio do uso de PCA, portanto, para que não fosse perdido informação alguma e capturar a maior variância possível dos dados não foi realizado nenhum processo de *feature selection*, portanto, foi o PCA foi realizado no dataset com todas as features disponíveis, além das recém criadas. 

Além disso, como as *features* possuem diferentes ordens de grandeza foi realizada uma padronização por meio do *StandardScaler()* de modo a evitar que uma *feature* que possua uma ordem de grandeza muito superior as demais seja a responsável por grande parte da variância dos dados
||||||| merged common ancestors
=======
- from_this_person_to_poi_ratio
- from_poi_to_this_person_ratio
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7

A primeira é a proporção dos emails enviados por uma dada pessoa com destino a algum `POI`em relação ao total de emails enviados pela pessoa, enquanto a segunda *feature* é a proporção dos emails recebidos de uma dada pessoa enviados por algum `POI`em relação ao total de emails recebidos pela dada pessoa.

Um das evidências coletadas pelas autoridades para a investigação são os emails de diversos funcionários da Enron, dessa forma existe a possibilidade de haver uma maior incidência de emails entre duas pessoas que estejam envolvidas no esquema de corrupção, dessa forma as duas features criadas acima se apresentam como uma métrica adicional para tentar estabelecer *links* entre pessoas que estejam envolvidas no crime.

No processo de pré-processamento dos dados optou-se por realizar uma redução de dimensionalidade dos dados por meio do uso de PCA, portanto, para que não fosse perdido informação alguma e capturar a maior variância possível dos dados não foi realizado nenhum processo de *feature selection*, portanto, o PCA foi realizado no dataset com todas as features disponíveis, além das recém criadas. 

Além disso, como as *features* possuem diferentes ordens de grandeza foi realizada uma padronização por meio do *StandardScaler()* de modo a evitar que uma *feature* que possua uma ordem de grandeza muito superior as demais seja a responsável por grande parte da variância dos dados.

Para o modelo otimizado de acordo com *Pipeline* abaixo:

```
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
 svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini',...plit=4, min_weight_fraction_leaf=0.0,presort=False, random_state=42, splitter='best'))])
```

O *GridSearchCV* otimizou o Pipeline entre os parâmetros ajustados avaliou-se `n_components` entre 1 a 10 componentes e o melhor resultado foi com o uso de apeans 1 componente principal da PCA e a `feature_importances_`do algoritmo *DecisionTreeClassifier* resultou que essa única dimensão representa 100% de importância.

Além disso,  testou-se a otimização via *GridSearchCV* apenas com as features originais, bem como utilizando as criadas durante a análise e não ouve ganho de desempenho, as métricas de avaliação *Accuracy*, *Precision* e *Recall* foram exatamente idênticas em ambas as abordagens.

```
Features originais: Accuracy: 0.80640       Precision: 0.32358      Recall: 0.41450
Features originais + criadas: Accuracy: 0.80640       Precision: 0.32358      Recall: 0.41450
```

> What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?

- DecisionTreeClassifier
- LogisticRegression
- SVC

Pela tabela abaixo é possível constatar que o classificador DecisionTreeClassifier possui o melhor *Recall*, enquanto que o SVC registra a melhor métrica para *Precision*.

|       ALGORITMO        | PRECISION | RECALL  |
| :--------------------: | :-------: | :-----: |
| DecisionTreeClassifier |  0.32358  | 0.41450 |
|   LogisticRegression   |  0.48028  | 0.10350 |
|          SVC           |  0.46881  | 0.11650 |

> What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier)

O processo de *tunning* é importante porque ele otimiza a perfomance dos algoritmos. Para que seja possível mensurar a performance de um dado algoritmo é necessário testar a combinação de múltiplos parâmetros e avaliar/validar o resultado no conjunto de dados que esteja trabalhando. Desse modo, modificamos os algoritmos em sua natureza *default* onde se encontram em sua forma "genérica" e vamos testando os seus parâmetros para que possam se ajustar da melhor forma ao conjunto de dados de interesse.

No processo de *tunning* para os algoritmos abaixo buscou-se otimizar os seguintes parâmetros:

 **LogisticRegression**

```
"clf__C": [0.05, 0.5, 1, 10, 10**2, 10**3, 10**5, 10**10, 10**15],
"clf__tol":[10**-1, 10**-2, 10**-4, 10**-5, 10**-6, 10**-10, 10**-15],
"clf__class_weight":[None,'balanced']
```

**DecisionTreeClassifier**

```
"clf__criterion": ["gini", "entropy"],
"clf__max_depth":[None, 1, 2, 3, 4],
"clf__min_samples_split":[3, 4, 5],
"clf__class_weight":[None, 'balanced'],
"clf__random_state":[42]
```

**SVC**

```
"clf__C": 10. ** np.arange(-3,3),
"clf__gamma": 10. ** np.arange(-3,3)
```

> What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?

O processo de validação é importante porque nos permite avaliar o tradeoff  *bias-variance* de modo a buscar um equilíbrio, já que um alto viés significa que o modelo apresenta um *underfitting* em relação aos dados e uma alta variância é indicativo de *overfitting*. O melhor dos mundos é que um modelo tenha um excelente desempenho quando exposto a dados novos, ou seja, dados que não foram utilizados em seu treinamento. Para tanto, foi utilizado a função `train_test_split` o qual dividiu o dataset em: 70% para treinamento e os demais 30% para avaliação.

Além disso, no processo de tunning (*GridSearchCV*) realizado foi incluído uma etapa de validação cruzada do tipo *StratifiedShuffleSplit*, que garante que os *tests sets* tenham um percentual de `POI`muito próximos ao conjunto original de dados, além disso foram realizados 20 *splits* os quais seus respectivos *test set* representem 50% dos dados. 

Ao final do processo iterativo de tunning e validação cruzada o melhor estimador obtido pelo método `.best_estimator_` foi submetido ao script avaliador `tester.py` que também realiza uma validação cruzada por meio de StratifiedShuffleSplit com 1000 Folds e retorna diversas métricas para avaliação do desempenho do classificador.

> Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance.

A partir da construção doS *Pipeline*s com 3 algoritmos - *DecisionTree, LogisticRegression e Support Vector Machine* - bem como a otimização de alguns de seus parâmetros por meio do *GridSearchCV*, foi possível otimizar os algoritmos que tem seus respectivos desempenhos ilustrados pelas métricas *accuracy*, *precision* e *recall*. 

##### PIPELINE 1:  Uso da função PCA() + scoring = "f1" no tunning

> Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
>   svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini', max_dept...plit=3, min_weight_fraction_leaf=0.0,presort=False, random_state=42, splitter='best'))])

##### PIPELINE 2 Uso da função PCA() + scoring ="precision" no tunning

> Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
>   svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini', ...plit=4, min_weight_fraction_leaf=0.0, presort=False, random_state=42, splitter='best'))])

##### PIPELINE 3 Uso da função KernelPCA() + scoring='f1' no tunning

> Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', KernelPCA(alpha=1.0, coef0=1, copy_X=True, degree=3, eigen_solver='auto', fit_inverse_transform=False, gamma=None, kernel='poly', kernel_params=None, max_iter=None, n_components=3, n_jobs=1, ...plit=3, min_weight_fraction_leaf=0.0, presort=False, random_state=42, splitter='best'))])

##### PIPELINE 4 Uso da função KernelPCA() + scoring="precision" no tunning

> Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', KernelPCA(alpha=1.0, coef0=1, copy_X=True, degree=3, eigen_solver='auto',  fit_inverse_transform=False, gamma=None, kernel='linear', kernel_params=None, max_iter=None, n_components=10, n_jobs=...,  max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False))])



| PIPELINES | ACCURACY | PRECISION | RECALL  |
| :-------: | :------: | :-------: | :-----: |
|     1     | 0.67800  |  0.28509  | 0.93850 |
|     2     | 0.80640  |  0.32358  | 0.41450 |
|     3     | 0.66013  |  0.27407  | 0.93950 |
|     4     | 0.86460  |  0.46881  | 0.11650 |

No que concerne a avaliação de algoritmos de classificação, os autores Jake Lever, Martin Krzywinski e Naomi Altman publicaram no período científico **[nature methods](http://www.nature.com/nmeth/journal/v13/n8/full/nmeth.3945.html)** um excelente artigo denominado *Points of Significance: Classification evaluation* o qual discorrem sobre diversas métricas utilizadas na avaliação de algortimos de classificação. O referido artigo apresenta a figura abaixo que, de forma muito didática, explica a matriz de confusão e as diversas métricas possíveis de obter a partir dela.

<p align="center"> <img src="https://github.com/netoferraz/udacity/blob/master/05_identificar_fraude_no_email_da%20enron/pics/confusion_matrix_paper.png">  </p>

A métrica *accuracy* corresponde a fração das predições que foram realizadas corretamente. Das quatro *Pipelines* otimizados o de número 4 foi aquele que obteve um maior valor, apesar da fácil interpretação dessa métrica, um maior *accuracy* não significa necessariamente um bom estimador. Essa métrica só é adequada quando o número de instâncias de cada classe no *dataset* é balanceada, caso exista uma assimetria na distribuição das classes esse estimador poderá predizer a classe majoritária com maior frequência resultando em uma excelente performance em termos de *accuracy*, todavia, deixa a desejar como classificador. 

Para o caso particular da nossa análise menos de 15% do *dataset* corresponde a `POI's`, portanto, trata-se de uma distribuição bastante assimétrica. Nesse contexto, a ocorrência de **Falsos Positivos** (FP) e/ou **Falsos Negativos** torna-se ainda mais relevante e a métrica *accuracy* não informa nada a respeito da ocorrência dessas circunstâncias. 

Desse modo, para o problema dos funcionários da Enron um **FP** significa que o classificador estará apontando uma pessoa como `POI`quando na realidade ela não é, enquanto que o **FN** é classificar um `POI`como inocente.

O *Recall* ou sensibilidade representa a proporção dos `POIs` preditos corretamente em relação a todos aqueles que de fato são `POI`, essa métrica também é conhecida como *True Positive Rate* (TPR).

Por último e não menos importante, temos a *Precision* que corresponde a proporção dos `POIs`preditos corretamente em relação a todos aqueles que são preditos como `POI`.

Com os scores apresentados, podemos interpretar os classificadores de forma mais adequada. Vamos considerar que o objetivo é apresentar um modelo preditivo para a equipe encarregada da investigação do escândalo da Enron, portanto, o classificador deve indicar os nomes dos funcionários que devem ser investigados ao longo da operação.

Dessa modo, investigar um inocente por considerá-lo um `POI` é mais tolerável do que deixar de investigar um criminoso por não considerá-lo um `POI`. O primeiro caso é o típico **FP** ou **Erro do Tipo I**, em contrapartida o segundo caso é um exemplo de **FN** ou **Erro do Tipo II**.

A seguir encontra-se os dados  do *Pipeline* 3 que gerou o melhor resultado em termos de *Recall*. O resultado da matriz de confusão desse estimador no arquivo de validação/avaliação `tester.py` está apresentado abaixo:

|  **True positives**   |   1879    |
| :-------------------: | :-------: |
|  **False positives**  | **4977**  |
|  **False negatives**  |  **121**  |
|  **True negatives**   | **8023**  |
| **Total predictions** | **15000** |

O referido algortimo possui um Recall de 0,9395, isto é, em 93,95% das vezes aquelas pessoas que de fato são `POI` são preditas como `POI`. Portanto, uma incidência de **Falso Negativo** muito baixa. 

Na simulação realizada pelo `tester.py` das 15000 predições realizadas, apenas 121 (0,81%) são **FN**. Desse modo, o classificador comete um **Erro do Tipo 2** em 6,05% das vezes que realiza uma predição, ou seja, aproximadamente, a cada 100 pessoas que de fato são `POI`apenas 6 delas não são preditas como `POI`.

Em contrapartida, o mesmo classificador possui uma *Precision* de 0,2741, isto significa que em 27% das vezes aqueles que são preditos como `POI` são de fato `POI`. Portanto, o nosso estimador possui um calcanhar de Aquiles que chama-se **Falsos Positivos**. No contexto dos dados da Enron, significa dizer que o classificador estará cometendo um **Erro do Tipo I** 

Todavia, a rúbrica do projeto exige a entrega de um classificador que tenha *Recall* e *Precision* de ao menos 0,3. Desse modo, o Pipeline 2 atende as exigências do projeto com uma *Precision* de 0.32358 e um *Recall* de 0.41450.

<<<<<<< HEAD
Na simulação realizada pelo `tester.py` das 15000 predições realizadas, apenas 65 (0,43%) são **FN**. Desse modo, o classificador comete um **Erro do Tipo 2** em 3,25% das vezes que realiza uma predição, ou seja, aproximadamente, a cada 100 pessoas que de fato são `POI`apenas 3 delas não são preditas como `POI`.
||||||| merged common ancestors
Na simulação realizada pelo `tester.py` das 15000 predições realizadas, apenas 65 (0,43%) são **FN**. Desse modo, o classificador comete um **Erro do Tipo 2** em 3,25% das vezes que realiza uma predição, ou seja, aproximadamente a cada 100 pessoas que de fato são `POI`apenas 3 delas não são preditas como `POI`.
=======
#### 3. Referências Bibliográficas
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7

- [http://scikit-learn.org/stable/modules/pipeline.html#](http://scikit-learn.org/stable/modules/pipeline.html#)
- [http://stackoverflow.com/questions/31572487/fitting-data-vs-transforming-data-in-scikit-learn](http://stackoverflow.com/questions/31572487/fitting-data-vs-transforming-data-in-scikit-learn)
- [http://stackoverflow.com/questions/21338090/how-can-i-store-and-print-the-top-20-feature-names-and-scores](http://stackoverflow.com/questions/21338090/how-can-i-store-and-print-the-top-20-feature-names-and-scores)
- [http://sebastianraschka.com/Articles/2014_about_feature_scaling.html](http://sebastianraschka.com/Articles/2014_about_feature_scaling.html)
- [https://stats.stackexchange.com/questions/69157/why-do-we-need-to-normalize-data-before-analysis](https://stats.stackexchange.com/questions/69157/why-do-we-need-to-normalize-data-before-analysis)
- [http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron](http://www.marcosassi.com.br/grandes-fraudes-da-historia-o-caso-enron)
- [http://www.nature.com/nmeth/journal/v13/n8/full/nmeth.3945.html](http://www.nature.com/nmeth/journal/v13/n8/full/nmeth.3945.html)
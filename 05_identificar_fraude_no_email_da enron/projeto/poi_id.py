from __future__ import division
import sys
import pickle
import numpy as np
import pandas as pd
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, main
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline 
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler
from aux_functions import *
sys.path.append("..//tools//")

###lista de features
features_list = [
                 'poi',
                 'salary',
                 'deferral_payments',
                 'total_payments',
                 'loan_advances',
                 'bonus',
                 'restricted_stock_deferred',
                 'deferred_income',
                 'total_stock_value',
                 'expenses',
                 'exercised_stock_options',
                 'other',
                 'long_term_incentive',
                 'restricted_stock',
                 'director_fees',
                 'to_messages',
                 'from_poi_to_this_person',
                 'from_messages',
                 'from_this_person_to_poi',
                 'shared_receipt_with_poi'
                 ]

### carregar o dicionário contendo o dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### REMOÇÃO DOS OUTILERS
data_dict.pop("TOTAL") #AGREGADO DE TODAS AS INSTÂNCIAS
data_dict.pop("THE TRAVEL AGENCY IN THE PARK") #NÃO TENHO CERTEZA DO QUE PODE SER, TALVEZ UM ERRO DE DIGITAÇÃO
data_dict.pop("LOCKHART EUGENE E") #NÃO HÁ NENHUMA ENTRADA DE DADOS PARA ESSA PESSOA

#CARREGA OS DADOS EM UM DATAFRAME
df = data_to_df(data_dict, features_list)

#SUBSTITUI NAN POR 0
df = nan_handler(df)

### CRIA NOVAS FEATURES A PARTIR DAS EXISTENTES
df['from_this_person_to_poi_ratio'] = df['from_this_person_to_poi'] / df['from_messages']
df['from_this_person_to_poi_ratio'] = df['from_this_person_to_poi_ratio'].replace('NaN', 0)

df['from_poi_to_this_person'] = df['from_this_person_to_poi'] / df['to_messages']
df['from_poi_to_this_person'] = df['from_poi_to_this_person'].replace('NaN', 0)

#INPUTAR A MEDIANA AS INSTÂNCIAS QUE POSSUEM FEATURES SEM VALOR ATRIBUÍDO 

#EMAIL FEATURES
email_features = ['to_messages',
               'from_messages',
               'from_poi_to_this_person',
               'from_this_person_to_poi',
               'shared_receipt_with_poi',
               'from_this_person_to_poi_ratio',
               'from_poi_to_this_person']

#INPUTAR A MEDIANA
for feature in email_features:
    df[feature] = df[feature].apply(lambda x: df[feature].median() if x == 0 else x)


#ATUALIZA O DICIONÁRIO COM AS NOVAS FEATURES CRIADAS
my_dataset = pd.DataFrame.to_dict(df, orient="index")

# EXTRAÇÃO DAS FEATURES E LABELS PARA TESTE LOCAL
data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)

##DIVIDE O DATASET EM DADOS DE TREINAMENTO E AVALIAÇÃO
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

#padronizacao dos dados
scaler_std = StandardScaler()

#SELEAÇÃO DE FEATURE E/OU REDUÇÃO DE DIMENSIONILIDADE
feature_selection_pca = PCA()

#DICIONÁRIO CONTENDO OS ESTIMADORES QUE SERÃO UTILIZADOS E O CONJUNTO DE POSSÍVES
#VALORES PARA UMA SÉRIE DE PARÂMETROS QUE SERÃO OTIMIZADOS.
estimators = [{'estimator': LogisticRegression(),
                'params': {  "clf__C": [0.05, 0.5, 1, 10, 10**2, 10**3, 10**5, 10**10, 10**15],
                             "clf__tol":[10**-1, 10**-2, 10**-4, 10**-5, 10**-6, 10**-10, 10**-15],
                             "clf__class_weight":[None,'balanced']
                    }},
               {'estimator': DecisionTreeClassifier(),
                'params':
                    {
                        "clf__criterion": ["gini", "entropy"],
                        "clf__max_depth":[None, 1, 2, 3, 4],
                        "clf__min_samples_split":[3, 4, 5],
                        "clf__class_weight":[None, 'balanced'],
                        "clf__random_state":[42]
                        
                    }},
              {'estimator': SVC(),
                'params':
                    {
                        "clf__C": 10. ** np.arange(-3,3),
                        "clf__gamma": 10. ** np.arange(-3,3)
                    }      
                    
            }]

#ETAPA DE VALIDAÇÃO CRUZADA A SER INSERIADA NO PIPELINE
scv = StratifiedShuffleSplit(n_splits = 20, test_size = .5, random_state = 0) 
    
#LISTA QUE RECEBERÁ DICIONÁRIOS QUE IRÃO SER UTILIZADOS PARA DETERMINAR 
#O MELHOR ESTIMADOR
best_clf = []

#LISTA CONTENDO AS KEYS DO DICIONÁRIOS contidos na lista best_clf
clf_names = []

#CRIAR AS KEYS DOS DICIONÁRIOS CONTIDOS EM best_clf
for i in range(0,len(estimators)):
    estimator_n = "estimator"+"_"+str(i+1)
    clf_names.append(estimator_n)
    best_clf.append({estimator_n : "",
                     "f1_score" : ""
                     })

#PREENCHER OS DICIONÁRIOS CONTENDO AS INFORMAÇÕES RELATIVAS AO ESTIMADORES E
#O SEU RESPECTIVO DESEMPENHO  
for i in range(0,len(estimators)):
    ##DEFINIR O ESTIMADOR
    clf = estimators[i]['estimator']
    parameters = {'feature_selection__n_components':range(1,11)}
    ##INTRODUZIR O ESTIMADOR NO STEP
    steps = [('scaler',scaler_std),
             ('feature_selection',feature_selection_pca),
             ('clf', clf)]
    #DEFINIR A QUANTIDADE DE PARÂMETROS DO ESTIMADOR E ADICIONAR AO DICIONÁRIO
    param_size = int(len(estimators[i].items()[1][1]))
    for j in range(0,param_size):
        parameters[estimators[i]['params'].items()[j][0]] = estimators[i]['params'].items()[j][1] 
        
    #CRIAR OBJETO PIPELINE COM AS ETAPAS DE ANALISE
    pipe = Pipeline(steps)
    gsearch = GridSearchCV(pipe,param_grid = parameters, cv=scv, scoring="f1", error_score=0)
    gsearch.fit(X_train, y_train)
    #OBTER O ESTIMADOR COM OS MELHORES PARÂMETROS
    clf = gsearch.best_estimator_
    #ADICIONAR O ESTIMADOR NO DICIONÁRIO DE AVALIAÇÃO
    best_clf[i][best_clf[i].keys()[1]] = clf
    #AJUSTAR O ESTIMADOR AOS DADOS E OBTER MÉTRICAS DE AVALIAÇÃO
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    f1_metric = f1_score(y_test,y_pred)
    #ADICIONAR A MÉTRICA DE AVALIAÇÃO NO DICIONÁRIO DE AVALIAÇÃO
    best_clf[i][best_clf[i].keys()[0]] = f1_metric


#SELECIONAR O MODELO COM O MELHOR DESEMPENHO
clf = get_best_estimator(best_clf, clf_names)

#SALVAR OS ARQUIVOS
dump_classifier_and_data(clf, my_dataset, features_list)

#TESTAR O DESEMPENHO DO MELHOR ESTIMADOR
main()


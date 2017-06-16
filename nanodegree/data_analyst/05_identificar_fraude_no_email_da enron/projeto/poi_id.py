from __future__ import division
import sys  
sys.path.append("..//tools//")
import pickle
import numpy as np
import pandas as pd
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, main
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
<<<<<<< HEAD
from sklearn.decomposition import KernelPCA,PCA
from sklearn.feature_selection import SelectKBest
||||||| merged common ancestors
from sklearn.decomposition import PCA
=======
from sklearn.decomposition import KernelPCA, PCA
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7
from sklearn.pipeline import Pipeline 
from sklearn.metrics import f1_score
<<<<<<< HEAD
from sklearn.preprocessing import StandardScaler, MinMaxScaler

||||||| merged common ancestors
from sklearn.preprocessing import StandardScaler
=======
from sklearn.preprocessing import StandardScaler, MinMaxScaler
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7
from aux_functions import *


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

### CARREGAR O DATASET
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### REMOÇÃO DOS OUTILERS
data_dict.pop("TOTAL") #AGREGADO DE TODAS AS INSTÂNCIAS
data_dict.pop("THE TRAVEL AGENCY IN THE PARK") #NÃO TENHO CERTEZA DO QUE PODE SER, TALVEZ UM ERRO DE DIGITAÇÃO
data_dict.pop("LOCKHART EUGENE E") #NÃO HÁ NENHUMA ENTRADA DE DADOS PARA ESSA PESSOA

#CARREGA OS DADOS EM UM DATAFRAME
df = data_to_df(data_dict, features_list)

#CRIA UMA LISTA EXCLUINDO O LABEL PARA CONTABILIZAR O NÚMERO DE NAN POR FEATURE                
features_nan_count = df.columns.tolist()
#EXCLUI POI
del features_nan_count[-5]

#TRANSFORMA O DATATYPE DAS FEATURES EM FLOAT
for feature in features_nan_count:
    df[feature] = df[feature].astype(float)

#CONTABILIZA OS NAN DE CADA FEATURE E ARMAZENA EM UM DATAFRAME
count_nan_df = pd.DataFrame(df.isnull().sum(), columns=['number_of_nan'])


#SUBSTITUI NAN POR 0
df = nan_handler(df)

### CRIA NOVAS FEATURES A PARTIR DAS EXISTENTES
df['from_this_person_to_poi_ratio'] = df['from_this_person_to_poi'] / df['from_messages']
df['from_this_person_to_poi_ratio'] = df['from_this_person_to_poi_ratio'].replace('NaN', 0)

df['from_poi_to_this_person_ratio'] = df['from_poi_to_this_person'] / df['to_messages']
df['from_poi_to_this_person_ratio'] = df['from_poi_to_this_person_ratio'].replace('NaN', 0)

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

#EXTRAÇÃO DAS FEATURES E LABELS PARA TESTE LOCAL
data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)

##DIVIDE O DATASET EM DADOS DE TREINAMENTO E AVALIAÇÃO
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=40)

#PADRONIZACAO DOS DADOS
scaler_std = StandardScaler()
#minmax = MinMaxScaler()

"""
# Print features selected and their importances
features_selected=[features_list[i+1] for i in clf.named_steps['feature_selection'].get_support(indices=True)]
scores = clf.named_steps['feature_selection'].scores_
importances = clf.named_steps['clf'].feature_importances_

indices = np.argsort(importances)[::-1]
print 'The ', len(features_selected), " features selected and their importances:"
for i in range(len(features_selected)):
    print "feature no. {}: {} ({}) ({})".format(i+1,features_selected[indices[i]],importances[indices[i]], scores[indices[i]])
"""


#SELEAÇÃO DE FEATURE E/OU REDUÇÃO DE DIMENSIONILIDADE
<<<<<<< HEAD
feature_selection_pca = KernelPCA()
||||||| merged common ancestors
feature_selection_pca = PCA()
=======
#COMENTAR A FUNÇÃO QUE NÃO DESEJA UTILIZAR
dimen_reduction = PCA()
#feature_selection_pca = KernelPCA()
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7

#DICIONÁRIO CONTENDO OS ESTIMADORES QUE SERÃO UTILIZADOS E O CONJUNTO DE POSSÍVES
#VALORES PARA UMA SÉRIE DE PARÂMETROS QUE SERÃO OTIMIZADOS.
#CASO DESEJE TESTAR UM ESTIMADOR POR VEZ, COMENTAR OS DEMAIS DE FORMA A SETAR
#O DICIONÁRIO COM APENAS O ALGORITMO DESEJADO.
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
#DICIONÁRIO ESTIMATORS COM APENAS LogisticRegression()
#Accuracy: 0.86553       Precision: 0.48028      Recall: 0.10350 F1: 0.17030     F2: 0.12276

#DICIONÁRIO ESTIMATORS COM APENAS SVC()
#Accuracy: 0.86460       Precision: 0.46881      Recall: 0.11650 F1: 0.18662     F2: 0.13711

#DICIONÁRIO ESTIMATORS COM APENAS DecisionTreeClassifier()
#Accuracy: 0.80640       Precision: 0.32358      Recall: 0.41450 F1: 0.36344     F2: 0.39244

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
<<<<<<< HEAD
    parameters = {'feature_selection__n_components':range(1,11),
                  "feature_selection__kernel": ["linear","poly", "rbf", "sigmoid"]
    }
||||||| merged common ancestors
    parameters = {'feature_selection__n_components':range(1,11)}
=======
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7
    ##INTRODUZIR O ESTIMADOR NO STEP
    steps = [('scaler',scaler_std),
             ('dimen_reduc',dimen_reduction),
             ('clf', clf)]
    #DCIONÁRIO DE PARÂMETROS
    parameters = {'dimen_reduc__n_components':range(1,11)
    #CASO UTILIZE A FUNÇÃO KernelPCA() RETIRAR O COMENTÁRIO DA LINHA ABAIXO
            #"feature_selection__kernel": ["linear","poly","rbf","sigmoid"]
    }
    #DEFINIR A QUANTIDADE DE PARÂMETROS DO ESTIMADOR E ADICIONAR AO DICIONÁRIO
    param_size = int(len(estimators[i].items()[1][1]))
    for j in range(0,param_size):
        parameters[estimators[i]['params'].items()[j][0]] = estimators[i]['params'].items()[j][1] 
        
    #CRIAR OBJETO PIPELINE COM AS ETAPAS DE ANALISE
    pipe = Pipeline(steps)
<<<<<<< HEAD
    gsearch = GridSearchCV(pipe,param_grid = parameters, cv=scv, scoring="precision", error_score=0)
||||||| merged common ancestors
    gsearch = GridSearchCV(pipe,param_grid = parameters, cv=scv, scoring="f1", error_score=0)
=======
    #O PARÂMETRO SCORING PODE SER ALTERADO
    gsearch = GridSearchCV(pipe,param_grid = parameters, cv=scv, scoring="precision", error_score=0)
>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7
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

<<<<<<< HEAD



||||||| merged common ancestors
=======
## PCA + SCORING="precision"
## Precision: 0.32358      Recall: 0.41450

#PARA O MODELO QUE FOI UTILIZADO PCA() + scoring="precision"
#NÚMERO DE COMPONENTES DA PCA UTILIZADOS NO MODELO
#clf.named_steps['dimen_reduc'].n_components_ = 1

#VARIÂNCIA EXPLICADA PELO COMPONENTE UTILIZADO NA PCA

#clf.named_steps['dimen_reduc'].explained_variance_ratio_ = 0.36736728

>>>>>>> 650ab05847aa1b1932b86d09b7211e121618edf7
#SALVAR OS ARQUIVOS
dump_classifier_and_data(clf, my_dataset, features_list)

#TESTAR O DESEMPENHO DO MELHOR ESTIMADOR
main()

#TESTE 1:
##1.1 USO DE PCA() + SCORING = "f1" NO GRIDSEARCH

"""
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini', max_dept...plit=3, min_weight_fraction_leaf=0.0,
            presort=False, random_state=42, splitter='best'))])
        Accuracy: 0.67800       Precision: 0.28509      Recall: 0.93850 F1: 0.43733     F2: 0.64351
        Total predictions: 15000        True positives: 1877    False positives: 4707   False negatives:  123   True negatives: 8293
"""

#TESTE 2:
##2.1 USO DE PCA() + SCORING = "precision" NO GRIDSEARCH

"""
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', PCA(copy=True, iterated_power='auto', n_components=1, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)), ('clf', DecisionTreeClassifier(class_weight='balanced', criterion='gini',
        ...plit=4, min_weight_fraction_leaf=0.0,
            presort=False, random_state=42, splitter='best'))])
        Accuracy: 0.80640       Precision: 0.32358      Recall: 0.41450 F1: 0.36344     F2: 0.39244
        Total predictions: 15000        True positives:  829    False positives: 1733   False negatives: 1171   True negatives: 11267
"""

#TESTE 3:
##3.1 USO DE KernelPCA() + SCORING = "f1" NO GRIDSEARCH

"""
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', KernelPCA(alpha=1.0, coef0=1, copy_X=True, degree=3, eigen_solver='auto',
     fit_inverse_transform=False, gamma=None, kernel='poly',
     kernel_params=None, max_iter=None, n_components=3, n_jobs=1,
...plit=3, min_weight_fraction_leaf=0.0,
            presort=False, random_state=42, splitter='best'))])
        Accuracy: 0.66013       Precision: 0.27407      Recall: 0.93950 F1: 0.42435     F2: 0.63240
        Total predictions: 15000        True positives: 1879    False positives: 4977   False negatives:  121   True negatives: 8023
"""
#TESTE 4:
##4.1 USO DE KernelPCA() + SCORING = "precision" NO GRIDSEARCH

"""
Pipeline(steps=[('scaler', StandardScaler(copy=True, with_mean=True, with_std=True)), ('feature_selection', KernelPCA(alpha=1.0, coef0=1, copy_X=True, degree=3, eigen_solver='auto',
     fit_inverse_transform=False, gamma=None, kernel='linear',
     kernel_params=None, max_iter=None, n_components=10, n_jobs=...,
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False))])
        Accuracy: 0.86460       Precision: 0.46881      Recall: 0.11650 F1: 0.18662     F2: 0.13711
        Total predictions: 15000        True positives:  233    False positives:  264   False negatives: 1767   True negatives: 12736
"""

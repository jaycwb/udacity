# -*- coding: utf-8 -*-
"""
Created on Wed May 03 14:45:59 2017

@author: jferraz
"""
import pandas as pd

def data_to_df(data,features):
    """
    # data é o dicionário contendo os dados da enron
    # features é uma lista contendo as features de interesse
    
    """
    data_on_dict = {}
    for i,key in enumerate(data.keys()): 
        if key not in data_on_dict:
            data_on_dict[key] = {}
        for feature in features:
            data_on_dict[key][feature] = data[key][feature]
    df = pd.DataFrame.from_dict(data_on_dict, orient='index', dtype=None)  
    return df

def nan_handler(df):
    "Substitui NaN por 0 ou por vazio no caso da coluna email"
    columns = df.columns
    for col in columns:
        if col == 'email_address':
            df[col] = df[col].replace('NaN', "")
        else:
            df[col] = df[col].replace('NaN', 0)
    return df

def get_best_estimator(clf_dict, clf_names):
    """Recebe o dicionário de estimadores e retorna o melhor de acordo com f1_score
    
    # clf_dict é o dicionário contendo todos os estimadores avaliados
    # clf_names é a lista com as keys dos estimadores contindos no clf_dict
    """
    f1_scores = []
    for i in clf_dict:
        for k,v in i.items():
            if k == "f1_score":
                f1_scores.append(v)
    best_score = max(f1_scores)
    
    for i in clf_dict:
        if i['f1_score'] == best_score:
            for name in clf_names:
                if name in i:
                    clf = i[name]
    return clf



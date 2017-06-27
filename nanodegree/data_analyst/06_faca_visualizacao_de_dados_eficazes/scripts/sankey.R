library(networkD3)
library(jsonlite)

Energy <- jsonlite::fromJSON("C:\\Users\\ferraz\\Documents\\Nanodegree\\Projetos\\nanodegree\\data_analyst\\06_faca_visualizacao_de_dados_eficazes\\data\\vendas_olac_agg.json")

sankeyNetwork(Links = Energy$links, Nodes = Energy$nodes, Source = "source",
              Target = "target", Value = "value", NodeID = "name",
              units = "TWh", fontSize = 12, nodeWidth = 30, iframe=TRUE)

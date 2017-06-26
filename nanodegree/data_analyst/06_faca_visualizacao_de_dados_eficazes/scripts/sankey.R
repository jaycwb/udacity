library(networkD3)

Energy <- jsonlite::fromJSON("C:\\Users\\jferraz\\Desktop\\vendas_olac_agg.json")
# Plot
sankeyNetwork(Links = Energy$links, Nodes = Energy$nodes, Source = "source",
              Target = "target", Value = "value", NodeID = "name",
              units = "TWh", fontSize = 12, nodeWidth = 30)


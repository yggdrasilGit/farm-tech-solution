# Carregar as bibliotecas necessárias
library('tidygeocoder')
library('tibble')

source("/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-R/R/funcoes.R")

cidade <- get_geocode("Parauna, Brasil")
print(cidade)

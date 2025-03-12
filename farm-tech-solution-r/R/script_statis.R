library(jsonlite)

source("/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-R/R/funcoes.R")

arquivo_json <- "/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-r/data/test.json"
df_resultado <- ler_json_para_dataframe(arquivo_json)

df_processado <- processar_dataframe(df_resultado)

colunas_para_analisar <- c("rocas.area_plantio", 
                           "semente_quantidade_kg", 
                           "fertilizante_quantidade_kg", 
                           "veneno_quantidade_litros", 
                           "adubo_quantidade_kg")

estatisticas <- calcular_estatisticas(df_processado, colunas_para_analisar)

# Convertendo a lista para JSON
estatisticas_json <- toJSON(estatisticas, pretty = TRUE)

# Caminho onde o arquivo JSON será salvo
caminho_arquivo_json <- "/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-r/data/estatisticas.json"

# Salvando o arquivo JSON
write(estatisticas_json, file = caminho_arquivo_json)


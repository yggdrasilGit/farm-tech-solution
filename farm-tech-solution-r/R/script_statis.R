library("jsonlite")
library("fs")

caminho_funcoes <- path("R", "funcoes.R")
source(caminho_funcoes)

arquivo_json <- path("data", "test.json")
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
caminho_arquivo_json <- path("data", "estatistica.json")

# Salvando o arquivo JSON
write(estatisticas_json, file = caminho_arquivo_json)


# Carregar pacotes necessários
library(jsonlite)
library(fs)
library(here)

# Função para encontrar o arquivo recursivamente
encontrar_arquivo <- function(nome_arquivo, raiz_busca=".") {
  raiz_busca <- path_abs(raiz_busca)  # Obtém o caminho absoluto da raiz de busca
  
  # Buscar recursivamente pelo arquivo
  arquivos_encontrados <- dir_ls(raiz_busca, recurse = TRUE, glob = nome_arquivo)
  
  if (length(arquivos_encontrados) > 0) {
    paste(arquivos_encontrados[1])
    return(arquivos_encontrados[1])
  } else {
    print(paste("❌ Erro: Arquivo", nome_arquivo, "não encontrado dentro de", raiz_busca))
    return(NULL)
  }
}

# Definir o caminho do arquivo de funções (utilizando 'here' para resolução do caminho)
caminho_funcoes_relativo <- here("farm-tech-solution-R/R", "funcoes.R")  # Caminho relativo do arquivo

# Exibir o caminho absoluto antes de carregar o script
caminho_funcoes_absoluto <- path_abs(caminho_funcoes_relativo)  # Obtém o caminho absoluto
paste(caminho_funcoes_absoluto)

# Verifica se o arquivo existe e carrega a função
if (file.exists(caminho_funcoes_absoluto)) {
  source(caminho_funcoes_absoluto)  # Carregar o script de funções
} else {
  stop("❌ Funções não encontradas! Verifique o caminho do arquivo 'funcoes.R'.")
}

# Definir o caminho do arquivo JSON de entrada
arquivo_json_relativo <- here("farm-tech-solution-R/data", "test.json")  # Caminho relativo do arquivo

# Exibir o caminho absoluto do arquivo JSON
arquivo_json_absoluto <- path_abs(arquivo_json_relativo)  # Obtém o caminho absoluto
paste("📂 Caminho absoluto do arquivo JSON:", arquivo_json_absoluto)

# Ler o arquivo JSON e converter em um dataframe
df_resultado <- ler_json_para_dataframe(arquivo_json_absoluto)

# Processar o dataframe
df_processado <- processar_dataframe(df_resultado)

# Definir as colunas a serem analisadas
colunas_para_analisar <- c("rocas.area_plantio", 
                           "semente_quantidade_kg", 
                           "fertilizante_quantidade_kg", 
                           "veneno_quantidade_litros", 
                           "adubo_quantidade_kg")

# Calcular as estatísticas
estatisticas <- calcular_estatisticas(df_processado, colunas_para_analisar)

# Converter as estatísticas para JSON
estatisticas_json <- toJSON(estatisticas, pretty = TRUE)

# Definir o caminho do arquivo JSON de saída
caminho_arquivo_json_relativo <- here("farm-tech-solution-R/data", "estatistica.json")  # Caminho relativo do arquivo

# Exibir o caminho absoluto do arquivo de saída
caminho_arquivo_json_absoluto <- path_abs(caminho_arquivo_json_relativo)  # Obtém o caminho absoluto
paste(caminho_arquivo_json_absoluto)

# Salvar o arquivo JSON com as estatísticas
write(estatisticas_json, file = caminho_arquivo_json_absoluto)
paste(caminho_arquivo_json_absoluto)


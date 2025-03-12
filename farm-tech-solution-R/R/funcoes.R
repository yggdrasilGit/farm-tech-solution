# Definir a função para ler JSON e converter para data.frame
ler_json_para_dataframe <- function(caminho_arquivo) {
  # Verifica se o arquivo existe
  if (!file.exists(caminho_arquivo)) {
    stop("O arquivo JSON não foi encontrado.")
  }
  
  # Lendo o arquivo JSON
  dados <- fromJSON(caminho_arquivo)
  
  # Converter para data.frame
  df <- as.data.frame(dados)
  
  return(df)
}

# Exemplo de uso:

# arquivo_json <- "/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-r/data/test.json"
# df_resultado <- ler_json_para_dataframe(arquivo_json)


# Função para processar o data.frame
processar_dataframe <- function(df) {
  # Verifica se a coluna 'rocas.insumos' existe
  if (!"rocas.insumos" %in% names(df)) {
    stop("A coluna 'rocas.insumos' não foi encontrada no data.frame.")
  }
  
  # Criando novas colunas baseadas nos insumos
  for (i in 1:nrow(df)) {
    df$semente_quantidade_kg[i] <- df$rocas.insumos[[i]][1, 'quantidade']
    df$fertilizante_quantidade_kg[i] <- df$rocas.insumos[[i]][2, 'quantidade']
    df$fertilizante_variedade[i] <- df$rocas.insumos[[i]][2, 'variedade']
    df$veneno_quantidade_litros[i] <- df$rocas.insumos[[i]][3, 'quantidade']
    df$veneno_variedade[i] <- df$rocas.insumos[[i]][3, 'variedade']
    df$adubo_quantidade_kg[i] <- df$rocas.insumos[[i]][4, 'quantidade']
    df$adubo_variedade[i] <- df$rocas.insumos[[i]][4, 'variedade']
  }
  
  # Excluindo a coluna 'rocas.insumos'
  df <- subset(df, select = -rocas.insumos)
  
  # Convertendo colunas para valores numéricos, removendo unidades de medida
  df$semente_quantidade_kg <- as.numeric(gsub(" kg", "", df$semente_quantidade_kg))
  df$fertilizante_quantidade_kg <- as.numeric(gsub(" kg", "", df$fertilizante_quantidade_kg))
  df$veneno_quantidade_litros <- as.numeric(gsub(" litros", "", df$veneno_quantidade_litros))
  df$adubo_quantidade_kg <- as.numeric(gsub(" kg", "", df$adubo_quantidade_kg))
  df$rocas.area_plantio <- as.numeric(gsub(" hectares", "", df$rocas.area_plantio))
  
  # Retorna o dataframe processado
  return(df)
}

# Exemplo de uso:
# df_processado <- processar_dataframe(df)
# print(df_processado)

# Função para calcular média e desvio padrão de colunas específicas
calcular_estatisticas <- function(df, colunas) {
  # Criar uma lista para armazenar os resultados
  resultados <- list()
  
  # Iterar sobre as colunas fornecidas
  for (coluna in colunas) {
    if (coluna %in% names(df)) {
      media <- mean(df[[coluna]], na.rm = TRUE)
      desvio_padrao <- sd(df[[coluna]], na.rm = TRUE)
      
      # Armazenar os resultados em uma lista
      resultados[[coluna]] <- list(
        media = media,
        desvio_padrao = desvio_padrao
      )
    } else {
      print(paste("A coluna", coluna, "não foi encontrada no dataframe."))
    }
  }
  
  return(resultados)
}

# Exemplo de uso:
# colunas_para_analisar <- c("rocas.area_plantio", 
#                           "semente_quantidade_kg", 
#                           "fertilizante_quantidade_kg", 
#                           "veneno_quantidade_litros", 
#                           "adubo_quantidade_kg")

# Chamar a função
# estatisticas <- calcular_estatisticas(df, colunas_para_analisar)













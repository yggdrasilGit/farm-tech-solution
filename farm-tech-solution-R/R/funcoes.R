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


# Definir a função para obter coordenadas de um local
# Definir a função para obter coordenadas de um local
get_geocode <- function(location_name) {
  # Verifica se a função geocode existe
  if (!exists("geocode")) {
    stop("A função geocode não está disponível. Verifique se o pacote 'tidygeocoder' foi instalado corretamente.")
  }
  
  # Tenta geocodificar a cidade usando OpenStreetMap (OSM)
  resultado <- tibble(location = location_name) %>%
    geocode(location, method = "osm")
  
  return(resultado)
}


# **Exemplo de uso da função**
# resultado <- get_geocode("Parauna, Brasil")
# print(resultado)


#buscasr o diretorio data 
get_data_directory <- function() {
  # Defina o caminho base para salvar os arquivos JSON
  base_dir <- file.path("~", "Documents", "GitHub", "farm-tech-solution", "farm-tech-solution-R", "data")
  
  # Normalizar o caminho para garantir compatibilidade com qualquer SO
  normalized_dir <- normalizePath(base_dir, mustWork = FALSE)
  
  # Criar o diretório, se não existir
  dir.create(normalized_dir, showWarnings = FALSE, recursive = TRUE)
  
  return(normalized_dir)
}

save_json <- function(data, file_name) {
  directory <- get_data_directory()  # Obtém o diretório correto
  
  # Criar diretório se não existir
  if (!dir.exists(directory)) {
    dir.create(directory, recursive = TRUE)
  }
  
  # Caminho completo do arquivo JSON
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  # Salvar os dados em JSON
  write_json(data, file_path, pretty = TRUE, auto_unbox = TRUE)
  
  cat("Dados salvos em:", file_path, "\n")
}

# Função para carregar dados JSON do diretório específico
load_json <- function(file_name) {
  directory <- get_data_directory()  # Obtém o diretório correto
  
  # Caminho completo do arquivo JSON
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  # Verificar se o arquivo existe
  if (file.exists(file_path)) {
    data <- fromJSON(file_path)
    return(data)
  } else {
    cat("Arquivo não encontrado:", file_path, "\n")
    return(NULL)
  }
}


# Função para obter dados meteorológicos

# Função para obter dados meteorológicos (API gratuita)


# Função para obter dados meteorológicos
# Função para obter dados meteorológicos
obter_previsao <- function(lat, lon, api_key) {
  # Construir a URL da API
  url <- paste0("https://api.openweathermap.org/data/2.5/weather?",
                "lat=", lat,
                "&lon=", lon,
                "&appid=", api_key,
                "&lang=pt_br",
                "&units=metric")
  
  # Fazer a requisição GET
  resposta <- GET(url)
  
  # Verificar se a requisição foi bem-sucedida
  if (status_code(resposta) == 200) {
    # Obter o conteúdo da resposta
    dados <- content(resposta, as = "text", encoding = "UTF-8")
    
    # Converter o JSON para uma lista R
    dados_json <- save_json(dados, "dados_climaticos")
    
 
      return()
    
  }
}

# processamento climaticp
processar_dados_clima <- function(json_dados) {
  # Converter JSON para lista
  dados_lista <- fromJSON(json_dados, simplifyVector = FALSE)  # Desativa conversão automática para data.frame
  
  # Verificar estrutura dos dados (para diagnóstico)
  str(dados_lista)
  
  # Acessar os dados do clima de forma segura
  if (!is.null(dados_lista$weather) && length(dados_lista$weather) > 0) {
    weather_list <- dados_lista$weather[[1]]  # Pegar o primeiro item da lista
    clima_descricao <- weather_list$description
    clima_tipo <- weather_list$main
  } else {
    clima_descricao <- NA
    clima_tipo <- NA
  }
  
  # Criar data frame com os dados extraídos
  dados_clima <- data.frame(
    Cidade = dados_lista$name,
    Pais = dados_lista$sys$country,
    Latitude = dados_lista$coord$lat,
    Longitude = dados_lista$coord$lon,
    Temperatura = dados_lista$main$temp,
    Sensacao_Termica = dados_lista$main$feels_like,
    Temp_Minima = dados_lista$main$temp_min,
    Temp_Maxima = dados_lista$main$temp_max,
    Pressao_Atmosferica = dados_lista$main$pressure,
    Umidade = dados_lista$main$humidity,
    Visibilidade = dados_lista$visibility,
    Velocidade_do_Vento = dados_lista$wind$speed,
    Direcao_do_Vento = dados_lista$wind$deg,
    Cobertura_de_Nuvens = dados_lista$clouds$all,
    Descricao_do_Clima = clima_descricao,
    Tipo_de_Clima = clima_tipo,
    Nascer_do_Sol = as.POSIXct(dados_lista$sys$sunrise, origin = "1970-01-01", tz = "GMT"),
    Por_do_Sol = as.POSIXct(dados_lista$sys$sunset, origin = "1970-01-01", tz = "GMT"),
    Fuso_Horario = dados_lista$timezone
  )
  
  return(dados_clima)
}









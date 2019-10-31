
# BASE SQL com Cartas de Interesse. 
# AGORA, PRECISAMOS PEGAR TODOS OS RESULTADOS E ACHAR OS VALORES COM A OCR, LEMBRANDO QUE ISTO É UMA LISTA

# 1) IDENTIFICAR OS DADOS NECESSÁRIOS NO NOSSO SCRAPING:                                           ###################################### CHECK
"""
DADOS IDENTIFICADOS: 
-- e-col1 <img title=""       ==> NOME DA LOJA
-- e-col3     								==> Coluna dos Preços, precisa ser decodificada.
-- e-col2                     ==> SIMBOLO DA EDIÇÃO COM NOME ABREV.
-- e-col4 (font class="azul") ==> QUALIDADE DA CARTA 
-- e-col5                     ==> Quantidade de Unidades, precisa ser decodificada.
"""

# 2) ARMAZENAR AS VARIAVEIS INTERESSANTES EM LISTAS/DICIONARIOS                                 ######################################### CHECK


#	3) IDENTIFICAR MANEIRA PARA PROCESSAR OS DADOS ENCRIPTADOS (PROVAVELMENTE ENVOLVE PYTESSERACT) ######################################## CHECK
 ## -- PEGAR ELEMENTOS CSS PARA O CRAWLING                                                       ######################################## CHECK
 ## -- DE=>PARA  CLASS CSS => POSIÇÃO                                                            ######################################## CHECK
 ## -- CRIAR METODO QUE FAZ A PROCURA NO SITE DA LIGAMAGIC PARA MAIS DE UMA CARTA                ??????????????

#4)	TRANSFERIR ESTAS LISTAS/DICIONARIOS PARA O SQL/SQLITE/ETC                                    <========  FOCO ATUAL                                

#5) REALIZAR O LEVANTE DE DADOS ATRAVÉS DO EEL (GUI CSS/HTML/JS)

#6)	DEFINIR MANEIRA DE COMPARAR COM OS PREÇOS DA STARCITYGAMES

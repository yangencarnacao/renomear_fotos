import os
import re
import unicodedata
import pandas as pd

# ==================== CONFIGURAÇÕES DO USUÁRIO ====================
# Defina o caminho para o seu arquivo Excel
caminho_planilha = "lista_alunos.xlsx"

# Defina o caminho para a pasta onde estão as fotos
diretorio_fotos = "./fotos_alunos"

# Defina o nome exato das colunas na sua planilha Excel
coluna_nome = "NomeAluno"
coluna_codigo = "CodAluno"
# ==================================================================


def normalizar_texto(texto):
    """Remove acentos, caracteres especiais e converte para minúsculas para facilitar a comparação."""
    if not isinstance(texto, str):
        texto = str(texto)

    # Remove acentos (Ex: "João" vira "Joao")
    texto_sem_acentos = (
        unicodedata.normalize("NFKD", texto)
        .encode("ascii", "ignore")
        .decode("utf-8")
    )

    # Mantém apenas letras, números e espaços, removendo caracteres especiais
    texto_limpo = re.sub(r"[^a-zA-Z0-9\s]", "", texto_sem_acentos)

    # Remove espaços extras nas pontas e padroniza em minúsculas
    return texto_limpo.strip().lower()


def limpar_codigo(codigo):
    """Remove qualquer letra ou caractere especial do CodAluno, mantendo apenas números."""
    if not isinstance(codigo, str):
        codigo = str(codigo)

    # Remove tudo o que NÃO for número
    codigo_numerico = re.sub(r"\D", "", codigo)
    return codigo_numerico


def renomear_fotos():
    # 1. Carregar a planilha Excel
    try:
        df = pd.read_excel(caminho_planilha)
        print("Planilha carregada com sucesso!")
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")
        return

    # Verificar se as colunas configuradas existem na planilha
    if coluna_nome not in df.columns or coluna_codigo not in df.columns:
        print(
            f"Erro: As colunas '{coluna_nome}' ou '{coluna_codigo}' nao foram encontradas."
        )
        print(f"Colunas disponíveis na planilha: {list(df.columns)}")
        return

    # Criar o dicionário de mapeamento aplicando o tratamento de texto e código
    mapeamento = {}
    for _, linha in df.iterrows():
        nome_original = linha[coluna_nome]
        codigo_original = linha[coluna_codigo]

        # Trata o nome (sem acentos/especiais) e limpa o código (apenas números)
        nome_tratado = normalizar_texto(nome_original)
        codigo_limpo = limpar_codigo(codigo_original)

        if nome_tratado and codigo_limpo:
            mapeamento[nome_tratado] = codigo_limpo

    # 2. Verificar se o diretório das fotos existe
    if not os.path.exists(diretorio_fotos):
        print(f"Erro: O diretório '{diretorio_fotos}' não foi encontrado.")
        return

    # Listar todos os arquivos na pasta de fotos
    arquivos = os.listdir(diretorio_fotos)

    sucesso = 0
    nao_encontrados = 0

    print("\nIniciando o processo de renomeação...")

    # 3. Iterar sobre os arquivos e renomeá-los
    for arquivo in arquivos:
        # Ignorar pastas, focar apenas em arquivos
        caminho_antigo = os.path.join(diretorio_fotos, arquivo)
        if os.path.isdir(caminho_antigo):
            continue

        # Separar o nome do arquivo da sua extensão
        nome_base, extensao = os.path.splitext(arquivo)

        # Trata o nome do arquivo da foto da mesma forma que tratou a planilha
        nome_base_tratado = normalizar_texto(nome_base)

        # Verificar se o nome tratado da foto existe no mapeamento da planilha
        if nome_base_tratado in mapeamento:
            novo_nome_base = mapeamento[nome_base_tratado]
            # Garante que a extensão fique em minúscula (.jpg, .png)
            novo_nome_arquivo = f"{novo_nome_base}{extensao.lower()}"
            caminho_novo = os.path.join(diretorio_fotos, novo_nome_arquivo)

            try:
                # Renomeia o arquivo fisicamente
                os.rename(caminho_antigo, caminho_novo)
                print(f"Renomeado: '{arquivo}' -> '{novo_nome_arquivo}'")
                sucesso += 1
            except Exception as e:
                print(f"Erro ao renomear o arquivo '{arquivo}': {e}")
        else:
            # Caso a foto tenha o nome de alguém que não está na planilha
            nao_encontrados += 1

    # Resumo final
    print("\n=== PROCESSO CONCLUÍDO ===")
    print(f"Fotos renomeadas com sucesso: {sucesso}")
    print(
        f"Arquivos ignorados ou não encontrados na planilha: {nao_encontrados}"
    )


if __name__ == "__main__":
    renomear_fotos()
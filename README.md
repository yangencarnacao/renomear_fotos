```markdown
# Renomeador de Fotos de Alunos por Código

Este script em Python automatiza o processo de renomear arquivos de fotos de alunos (geralmente nomeados com o nome completo do aluno) para o seu respectivo código de matrícula, utilizando uma planilha Excel como banco de dados para o mapeamento.

O script é inteligente: ele limpa acentos, espaços extras e caracteres especiais tanto da planilha quanto dos arquivos de imagem para garantir que o cruzamento de dados funcione mesmo se houver pequenas diferenças de digitação.

## 🚀 Como Funciona?

1. O script lê uma planilha Excel (`.xlsx`) contendo os nomes e códigos dos alunos.
2. Ele limpa e padroniza os nomes (removendo acentos, caracteres especiais e convertendo para minúsculas).
3. Ele limpa os códigos dos alunos, mantendo **apenas números**.
4. Ele varre a pasta de fotos e, ao encontrar uma foto com o nome correspondente ao de um aluno da planilha, renomeia o arquivo para `[CodigoDoAluno].[extensão]`.

---

## 📋 Pré-requisitos

Antes de executar o script, você precisa ter o Python instalado na sua máquina e a biblioteca `pandas` (junto com o motor para ler arquivos Excel).

Você pode instalar as dependências necessárias executando o seguinte comando no terminal:

```bash
pip install pandas openpyxl

```

---

## ⚙️ Configuração

Abra o arquivo do script e edite a seção **CONFIGURAÇÕES DO USUÁRIO** com as informações do seu projeto:

```python
# ==================== CONFIGURAÇÕES DO USUÁRIO ====================
caminho_planilha = "lista_alunos.xlsx"  # Nome ou caminho do seu arquivo Excel
diretorio_fotos = "./fotos_alunos"  # Pasta onde estão armazenadas as fotos
coluna_nome = "NomeAluno"  # Nome exato da coluna de nomes na planilha
coluna_codigo = "CodAluno"  # Nome exato da coluna de códigos na planilha
# ==================================================================

```

### Estrutura de Pastas Recomendada:

```text
meu_projeto/
│
├── renomear_fotos.py       # Este script
├── lista_alunos.xlsx       # Sua planilha Excel
└── fotos_alunos/           # Pasta com as fotos (Ex: "João Silva.jpg")

```

---

## 🛠️ Exemplo Prático

### 1. Dados da Planilha (`lista_alunos.xlsx`):

| NomeAluno | CodAluno |
| --- | --- |
| João Alcantara Silva | A-12345 |
| Maria Andréa da Costa | 67890 / SP |

### 2. Antes de Rodar o Script (Pasta `./fotos_alunos`):

* `João Alcântara silva.JPG`
* `maria andrea da costa.png`

### 3. Depois de Rodar o Script (Pasta `./fotos_alunos`):

* `12345.jpg`
* `67890.png`

> 💡 **Nota:** Perceba que o script removeu os traços e letras dos códigos, converteu as extensões para minúsculas e ignorou as diferenças de acentuação e maiúsculas/minúsculas nos nomes!

---

## 🏃 Como Executar

Com as configurações feitas e as fotos na pasta correta, execute o script pelo terminal:

```bash
python renomear_fotos.py

```

O terminal exibirá o progresso em tempo real e mostrará um resumo ao final:

```text
Planilha carregada com sucesso!

Iniciando o processo de renomeação...
Renomeado: 'João Alcântara silva.JPG' -> '12345.jpg'
Renomeado: 'maria andrea da costa.png' -> '67890.png'

=== PROCESSO CONCLUÍDO ===
Fotos renomeadas com sucesso: 2
Arquivos ignorados ou não encontrados na planilha: 0

```

---

## ⚠️ Avisos Importantes

* **Faça um backup:** É altamente recomendável fazer uma cópia da sua pasta de fotos antes de rodar o script, já que o processo de renomeação altera os arquivos originais.
* **Extensões mantidas:** O script mantém o formato original da foto (PNG, JPG, JPEG, etc.), apenas padronizando a extensão para letras minúsculas.

```

```

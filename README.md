# Faustão no Chat 🎙️

## Descrição

Este projeto utiliza a API do Google Generative AI para criar um chatbot que simula Faustão, o famoso apresentador de televisão brasileiro. A aplicação permite que o usuário interaja com Faustão de maneira divertida, analisando texto, imagens e vídeos. 

- **A**: Converse com o Faustão! (Geração de Texto)
- **B**: Chamar os reclames do plim plim! (Análise de Imagens)
- **C**: Vídeo cassetadas! (Análise de Vídeos)

---

## Dependências

Para rodar esta aplicação, são necessárias as seguintes dependências:

- **Python**
- **Bibliotecas**:
  - `google.generativeai`: Para interagir com a API do Google Generative AI.
  - `IPython.display`: Utilizado para renderizar Markdown e para fazer uploads de arquivos.
  - `time`: Utilizado para atrasos no código, especialmente ao aguardar o processamento dos vídeos.
  - `google.colab`: Para interagir com o ambiente do Google Colab, como o upload de arquivos e o armazenamento seguro de credenciais.

## Configuração da API

Esta aplicação utiliza a API do Google Generative AI. Para usar essa API, é necessário ter uma chave de API válida. Aqui estão os passos para configurar a integração:

1. **Obtenha a chave da API**:
   - Cadastre-se no [Google Cloud Platform](https://cloud.google.com/) e crie um projeto.
   - Ative o serviço de **Google Generative AI** no projeto.
   - Vá até a seção "Credenciais" e gere uma **API Key**.

2. **Defina a chave da API no Colab**:
   - Armazene a chave da API no Colab utilizando `userdata.get('GOOGLE_API_KEY')`. A aplicação usará esta chave para autenticar as requisições.

---

## Como Rodar a Aplicação

1. **Instale as Dependências**:

   Execute o comando abaixo para instalar as dependências do Google Generative AI:

   ```python
   !pip install google-generativeai
   ```

2. **Configure o Ambiente**:

   No Google Colab, execute as instruções para garantir que a chave da API do Google seja configurada corretamente:

   ```python
   from google.colab import userdata
   GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
   ```

3. **Clone e Execute o Código**:

   - Copie o código principal e cole em uma célula do Colab.
   - Execute o código para iniciar o menu principal do programa.
   - Escolha entre as opções disponíveis para interagir com Faustão, seja por texto, imagens ou vídeos.

---

## Instruções de Uso

- **A - Converse com o Faustão! (Geração de Texto)**

  Esta funcionalidade cria uma sessão de conversa onde o usuário interage com o Faustão. Utilize frases como se estivesse em um bate-papo, e o modelo irá responder com o jeito característico do Faustão.

- **B - Chamar os reclames do plim plim! (Análise de Imagens)**

  Nesta opção, você poderá fazer o upload de uma imagem. Faustão irá analisá-la e destacar os pontos principais. A análise de imagem utiliza a API do Google Generative AI para gerar descrições da imagem.

  - **Upload de Arquivo**: O arquivo de imagem deve ser carregado através da função `files.upload()` e, em seguida, o modelo `gemini-1.5-pro-latest` faz a análise.

- **C - Vídeo cassetadas! (Análise de Vídeos)**

  Você poderá fazer o upload de um vídeo. O Faustão fará uma análise do conteúdo do vídeo e destacará os pontos importantes. A análise do vídeo também utiliza a API do Google Generative AI.

  - **Processamento de Arquivo**: O vídeo é carregado e processado antes de ser enviado para análise. O programa aguarda a finalização do processamento para garantir que o vídeo está pronto para ser analisado.

---

## API e Modelos utilizados

A aplicação utiliza a biblioteca `google.generativeai` para se conectar ao Google Generative AI, usando o modelo `gemini-1.5-pro`.

- **API Key**: A API Key é necessária para autenticação e é armazenada no `userdata` para segurança.
- **Configuração do Modelo**: O modelo é configurado com parâmetros específicos como `temperature`, `top_p`, e `top_k` para controlar a criatividade e variedade das respostas geradas.
  
### Funções

- **converse_com_o_fausto(model, history)**: Utiliza a função `model.start_chat()` para iniciar uma conversa com o Faustão. As respostas são geradas com base no histórico da conversa.
  
- **reclames_do_plim_plim(generation_config)**: Esta função faz upload de uma imagem e a envia para o Google Generative AI, que retorna uma análise descritiva do conteúdo.

- **video_cassetadas(generation_config)**: Semelhante à análise de imagens, esta função faz o upload de um vídeo, espera o processamento e depois gera uma análise dos pontos importantes do vídeo.

### Referência de Documentação

- Documentação da [API Google Generative AI](https://cloud.google.com/generative-ai)
- Documentação da biblioteca [google-generativeai Python SDK](https://github.com/google/generative-ai-python)

---

## Observações

- Para garantir o bom funcionamento da aplicação, o vídeo enviado deve ser curto, pois vídeos longos podem levar muito tempo para serem processados.
- O ambiente do Google Colab facilita o upload de arquivos e a integração com a API, tornando a execução deste projeto mais simples.

## Problemas Conhecidos

- **Falha no Processamento de Vídeo**: Caso o vídeo não possa ser processado, a função retorna um erro. Isso pode acontecer devido ao formato ou ao tamanho do vídeo.

## Autor

Projeto criado por Andrey Ricardo Lucca Peil e Otávio Ferreira Dahlke! 😊

---

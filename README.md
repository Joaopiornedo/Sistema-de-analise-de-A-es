# Sistema de Fechamento de Ações
Este projeto em Python utiliza yfinance e tkinter para criar um sistema de análise de ações com uma interface gráfica simples e intuitiva. O sistema permite aos usuários inserirem o código de uma ação e um período de tempo específico para obter informações detalhadas sobre os preços de abertura, máxima, mínima, fechamento e volume de negociação.

## Funcionalidades
Interface gráfica para inserção de dados.
Consulta de dados históricos de ações usando yfinance.
Exibição de valores mínimos, médios e máximos de Open, High, Low, Close e Volume.

## Como Usar
### Instale as dependências:
Certifique-se de ter as bibliotecas: yfinance e tkinter instaladas.<br>
Você pode instalar yfinance usando o seguinte comando:<br>

pip install yfinance

## Execute o script:
Execute o arquivo Python para abrir a interface gráfica:

## Insira os dados:

Digite o código da ação (ex.: PETR4.SA).
Digite a data de início (formato: YYYY-MM-DD).
Digite a data final (formato: YYYY-MM-DD).
Inicie a análise:
Clique no botão "Iniciar" para obter os resultados. <br>
Uma caixa de mensagem exibirá os valores mínimos, médios e máximos dos preços de abertura,<br>
máxima, mínima, fechamento e volume de negociação para o período especificado.

## Exemplo de Uso
Código da ação: PETR4.SA
Data de início: 2023-01-01
Data final: 2023-12-31
Ao clicar em "Iniciar", o sistema buscará os dados históricos da ação e exibirá os resultados em uma caixa de mensagem.

### Capturas de Tela

Descrição: Tela inicial do sistema onde o usuário insere o código da ação e as datas.<br>
Descrição: Caixa de mensagem exibindo os resultados da análise.

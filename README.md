# Jogo da Forca

Este é um jogo da forca em Python que permite aos usuários jogarem uma versão clássica do jogo com uma interface de texto simples. O jogo oferece diferentes níveis de dificuldade, escolha aleatória de palavras e limites de tentativas personalizados para uma experiência personalizada e desafiadora.

## Requisitos

Antes de começar a jogar, certifique-se de ter os seguintes requisitos:

- Python 3.6 ou versão superior instalado no seu sistema.

## Instruções de Uso

1. Clone o repositório para o seu ambiente local ou faça o download dos arquivos.

```shell
git clone https://github.com/dgeison/jogo_da_forca.git
```

2. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.

```shell
cd jogo-da-forca
```

3. Execute o arquivo principal `hangman.py` usando o Python.

```shell
python hangman.py
```

4. Siga as instruções na tela para jogar o jogo da forca.

- Escolha o nível de dificuldade:
  - Digite "1" para fácil (palavras de 3 a 5 letras).
  - Digite "2" para médio (palavras de 6 a 10 letras).
  - Digite "3" para difícil (palavras com 10 ou mais letras).

- O programa selecionará uma palavra aleatória para você.

- Você terá um número limitado de tentativas para adivinhar a palavra correta.

- Digite uma letra para adivinhar. O programa irá informar se a letra está correta ou não.

- Se a letra estiver correta, ela será exibida na posição correta da palavra.

- Se a letra estiver incorreta, você perderá uma tentativa.

- Continue adivinhando letras até descobrir a palavra correta ou até esgotar suas tentativas.

- Após o término do jogo, você terá a opção de jogar novamente ou sair.

## Customização

Você pode personalizar o jogo da forca ajustando os seguintes parâmetros no arquivo `hangman.py`:

- `QUANTIDADE_BASICA`: O fator multiplicador para determinar o número básico de tentativas com base no tamanho da palavra.

- `NIVEIS_DE_DIFICULDADE`: Um dicionário que define os limites de tamanho da palavra para cada nível de dificuldade.

## Contribuindo

Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.

2. Crie uma nova branch para as suas alterações.

```shell
git checkout -b minha-nova-feature
```

3. Faça as alterações desejadas e adicione-as ao commit.

```shell
git add .
```

4. Faça o commit das suas alterações.

```shell
git commit -m "Descrição das suas alterações"
```

5. Envie as alterações para o seu repositório remoto.

```shell
git push origin minha-nova-feature
```

6. Abra uma pull request no repositório original.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://github.com/seu-usuario/jogo-da-forca/blob/main/LICENSE).

## Contato

Se você tiver alguma dúvida

, sugestão ou feedback, não hesite em entrar em contato.

- Autor: Dgeison S. Peixoto
- E-mail: dgeison.peixoto@gmail.com

Aproveite o jogo da forca! Divirta-se e desafie seus amigos!
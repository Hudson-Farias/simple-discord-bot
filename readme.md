# Bot para Discord - Open Source

Este é um bot para Discord desenvolvido em Python utilizando a biblioteca [py-cord](https://docs.pycord.dev/en/v2.6.1/) para interação com a API do Discord. O projeto é open-source e pode ser facilmente configurado para diferentes propósitos.

## Tecnologias Utilizadas
- Python 3.x
- [py-cord](https://docs.pycord.dev/en/v2.6.1/) - Biblioteca para interação com o Discord
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Gerenciamento de variáveis de ambiente

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux 
   venv\Scripts\activate # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Copie o arquivo `.env.example` para `.env` e configure sua chave de API do Discord:
   ```sh
   cp .env.example .env
   ```

5. Edite o arquivo `.env` e adicione suas credenciais:
   ```env
   BOT_TOKEN = seu_token_aqui
   ```

## Uso
Para iniciar o bot, execute:
```sh
python main.py
```

Certifique-se de que o token do bot está corretamente configurado no arquivo `.env`.

## Comandos Disponíveis
- `avatar` - Obtém o avatar de um usuário
- `clear` - Limpa mensagens do chat
- `ping` - Testa a latência do bot
- `rename` - Altera o nome de um usuário
- `roll` - Rola um dado aleatório

## Contribuição
Ficamos felizes com contribuições! Para contribuir:
1. Fork este repositório
2. Crie um branch: `git checkout -b minha-nova-feature`
3. Faça commit das suas mudanças: `git commit -m 'Adicionando nova funcionalidade'`
4. Envie seu branch: `git push origin minha-nova-feature`
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

---

Se precisar de ajuda, sinta-se à vontade para abrir uma issue ou entrar em contato!


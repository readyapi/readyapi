# Generate Clients

Como o **readyapi** é baseado na especificação **OpenAPI**, você obtém compatibilidade automática com muitas ferramentas, incluindo a documentação automática da API (fornecida pelo Swagger UI).

Uma vantagem particular que nem sempre é óbvia é que você pode **gerar clientes** (às vezes chamados de <abbr title="Software Development Kits">**SDKs**</abbr>) para a sua API, para muitas **linguagens de programação** diferentes.

## Geradores de Clientes OpenAPI

Existem muitas ferramentas para gerar clientes a partir do **OpenAPI**.

Uma ferramenta comum é o <a href="https://openapi-generator.tech/" class="external-link" target="_blank">OpenAPI Generator</a>.

Se voce está construindo um **frontend**, uma alternativa muito interessante é o <a href="https://github.com/hey-api/openapi-ts" class="external-link" target="_blank">openapi-ts</a>.

## Geradores de Clientes e SDKs - Patrocinadores

Existem também alguns geradores de clientes e SDKs baseados na OpenAPI (readyapi) **patrocinados por empresas**, em alguns casos eles podem oferecer **recursos adicionais** além de SDKs/clientes gerados de alta qualidade.

Alguns deles também ✨ [**patrocinam o readyapi**](../help-readyapi.md#sponsor-the-author){.internal-link target=_blank} ✨, isso garante o **desenvolvimento** contínuo e saudável do readyapi e seu **ecossistema**.

E isso mostra o verdadeiro compromisso deles com o readyapi e sua **comunidade** (você), pois eles não apenas querem fornecer um **bom serviço**, mas também querem garantir que você tenha um **framework bom e saudável**, o readyapi. 🙇

Por exemplo, você pode querer experimentar:

* <a href="https://speakeasy.com/?utm_source=readyapi+repo&utm_medium=github+sponsorship" class="external-link" target="_blank">Speakeasy</a>
* <a href="https://www.stainlessapi.com/?utm_source=readyapi&utm_medium=referral" class="external-link" target="_blank">Stainless</a>
* <a href="https://developers.liblab.com/tutorials/sdk-for-readyapi/?utm_source=readyapi" class="external-link" target="_blank">liblab</a>

Existem também várias outras empresas que oferecem serviços semelhantes que você pode pesquisar e encontrar online. 🤓

## Gerar um Cliente Frontend TypeScript

Vamos começar com um aplicativo **readyapi** simples:

{* ../../docs_src/generate_clients/tutorial001_py39.py hl[7:9,12:13,16:17,21] *}

Note que as *operações de rota* definem os modelos que usam para o corpo da requisição e o corpo da resposta, usando os modelos `Item` e `ResponseMessage`.

### Documentação da API

Se você acessar a documentação da API, verá que ela tem os **schemas** para os dados a serem enviados nas requisições e recebidos nas respostas:

<img src="/img/tutorial/generate-clients/image01.png">

Você pode ver esses schemas porque eles foram declarados com os modelos no app.

Essas informações estão disponíveis no **OpenAPI schema** do app e são mostradas na documentação da API (pelo Swagger UI).

E essas mesmas informações dos modelos que estão incluídas no OpenAPI são o que pode ser usado para **gerar o código do cliente**.

### Gerar um Cliente TypeScript

Agora que temos o app com os modelos, podemos gerar o código do cliente para o frontend.

#### Instalar o `openapi-ts`

Você pode instalar o `openapi-ts` no seu código frontend com:

<div class="termy">

```console
$ npm install @hey-api/openapi-ts --save-dev

---> 100%
```

</div>

#### Gerar o Código do Cliente

Para gerar o código do cliente, você pode usar a aplicação de linha de comando `openapi-ts` que agora está instalada.

Como ela está instalada no projeto local, você provavelmente não conseguiria chamar esse comando diretamente, mas você o colocaria no seu arquivo `package.json`.

Poderia ser assim:

```JSON  hl_lines="7"
{
  "name": "frontend-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "generate-client": "openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axios"
  },
  "author": "",
  "license": "",
  "devDependencies": {
    "@hey-api/openapi-ts": "^0.27.38",
    "typescript": "^4.6.2"
  }
}
```

Depois de ter esse script NPM `generate-client` lá, você pode executá-lo com:

<div class="termy">

```console
$ npm run generate-client

frontend-app@1.0.0 generate-client /home/user/code/frontend-app
> openapi-ts --input http://localhost:8000/openapi.json --output ./src/client --client axios
```

</div>

Esse comando gerará o código em `./src/client` e usará o `axios` (a biblioteca HTTP frontend) internamente.

### Experimente o Código do Cliente

Agora você pode importar e usar o código do cliente, ele poderia ser assim, observe que você obtém preenchimento automático para os métodos:

<img src="/img/tutorial/generate-clients/image02.png">

Você também obterá preenchimento automático para o corpo a ser enviado:

<img src="/img/tutorial/generate-clients/image03.png">

/// tip | Dica

Observe o preenchimento automático para `name` e `price`, que foi definido no aplicativo readyapi, no modelo `Item`.

///

Você terá erros em linha para os dados que você envia:

<img src="/img/tutorial/generate-clients/image04.png">

O objeto de resposta também terá preenchimento automático:

<img src="/img/tutorial/generate-clients/image05.png">

## App readyapi com Tags

Em muitos casos seu app readyapi será maior, e você provavelmente usará tags para separar diferentes grupos de *operações de rota*.

Por exemplo, você poderia ter uma seção para **items** e outra seção para **users**, e elas poderiam ser separadas por tags:

{* ../../docs_src/generate_clients/tutorial002_py39.py hl[21,26,34] *}

### Gerar um Cliente TypeScript com Tags

Se você gerar um cliente para um app readyapi usando tags, normalmente também separará o código do cliente com base nas tags.

Dessa forma, você poderá ter as coisas ordenadas e agrupadas corretamente para o código do cliente:

<img src="/img/tutorial/generate-clients/image06.png">

Nesse caso você tem:

* `ItemsService`
* `UsersService`

### Nomes dos Métodos do Cliente

Agora os nomes dos métodos gerados como `createItemItemsPost` não parecem muito "limpos":

```TypeScript
ItemsService.createItemItemsPost({name: "Plumbus", price: 5})
```

...isto ocorre porque o gerador de clientes usa o **operation ID** interno do OpenAPI para cada *operação de rota*.

O OpenAPI exige que cada operation ID seja único em todas as *operações de rota*, então o readyapi usa o **nome da função**, o **caminho** e o **método/operacao HTTP** para gerar esse operation ID, porque dessa forma ele pode garantir que os operation IDs sejam únicos.

Mas eu vou te mostrar como melhorar isso a seguir. 🤓

### IDs de Operação Personalizados e Melhores Nomes de Método

Você pode **modificar** a maneira como esses IDs de operação são **gerados** para torná-los mais simples e ter **nomes de método mais simples** nos clientes.

Neste caso, você terá que garantir que cada ID de operação seja **único** de alguma outra maneira.

Por exemplo, você poderia garantir que cada *operação de rota* tenha uma tag, e então gerar o ID da operação com base na **tag** e no **nome** da *operação de rota* (o nome da função).

### Função Personalizada para Gerar IDs de Operação Únicos

O readyapi usa um **ID único** para cada *operação de rota*, ele é usado para o **ID da operação** e também para os nomes de quaisquer modelos personalizados necessários, para requisições ou respostas.

Você pode personalizar essa função. Ela recebe uma `APIRoute` e gera uma string.

Por exemplo, aqui está usando a primeira tag (você provavelmente terá apenas uma tag) e o nome da *operação de rota* (o nome da função).

Você pode então passar essa função personalizada para o **readyapi** como o parâmetro `generate_unique_id_function`:

{* ../../docs_src/generate_clients/tutorial003_py39.py hl[6:7,10] *}

### Gerar um Cliente TypeScript com IDs de Operação Personalizados

Agora, se você gerar o cliente novamente, verá que ele tem os nomes dos métodos melhorados:

<img src="/img/tutorial/generate-clients/image07.png">

Como você pode ver, os nomes dos métodos agora têm a tag e, em seguida, o nome da função. Agora eles não incluem informações do caminho da URL e da operação HTTP.

### Pré-processar a Especificação OpenAPI para o Gerador de Clientes

O código gerado ainda tem algumas **informações duplicadas**.

Nós já sabemos que esse método está relacionado aos **items** porque essa palavra está no `ItemsService` (retirada da tag), mas ainda temos o nome da tag prefixado no nome do método também. 😕

Provavelmente ainda queremos mantê-lo para o OpenAPI em geral, pois isso garantirá que os IDs de operação sejam **únicos**.

Mas para o cliente gerado, poderíamos **modificar** os IDs de operação do OpenAPI logo antes de gerar os clientes, apenas para tornar esses nomes de método mais **simples**.

Poderíamos baixar o JSON do OpenAPI para um arquivo `openapi.json` e então poderíamos **remover essa tag prefixada** com um script como este:

{* ../../docs_src/generate_clients/tutorial004.py *}

//// tab | Node.js

```Javascript
{!> ../../docs_src/generate_clients/tutorial004.js!}
```

////

Com isso, os IDs de operação seriam renomeados de coisas como `items-get_items` para apenas `get_items`, dessa forma o gerador de clientes pode gerar nomes de métodos mais simples.

### Gerar um Cliente TypeScript com o OpenAPI Pré-processado

Agora, como o resultado final está em um arquivo `openapi.json`, você modificaria o `package.json` para usar esse arquivo local, por exemplo:

```JSON  hl_lines="7"
{
  "name": "frontend-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "generate-client": "openapi-ts --input ./openapi.json --output ./src/client --client axios"
  },
  "author": "",
  "license": "",
  "devDependencies": {
    "@hey-api/openapi-ts": "^0.27.38",
    "typescript": "^4.6.2"
  }
}
```

Depois de gerar o novo cliente, você teria agora **nomes de métodos "limpos"**, com todo o **preenchimento automático**, **erros em linha**, etc:

<img src="/img/tutorial/generate-clients/image08.png">

## Benefícios

Ao usar os clientes gerados automaticamente, você teria **preenchimento automático** para:

* Métodos.
* Corpo de requisições, parâmetros da query, etc.
* Corpo de respostas.

Você também teria **erros em linha** para tudo.

E sempre que você atualizar o código do backend, e **regenerar** o frontend, ele teria quaisquer novas *operações de rota* disponíveis como métodos, as antigas removidas, e qualquer outra alteração seria refletida no código gerado. 🤓

Isso também significa que se algo mudar, será **refletido** no código do cliente automaticamente. E se você **construir** o cliente, ele dará erro se houver alguma **incompatibilidade** nos dados usados.

Então, você **detectaria vários erros** muito cedo no ciclo de desenvolvimento, em vez de ter que esperar que os erros apareçam para seus usuários finais em produção e então tentar depurar onde está o problema. ✨

# Códigos de status adicionais

Por padrão, o **ReadyAPI** retornará as respostas utilizando o `JSONResponse`, adicionando o conteúdo do retorno da sua *operação de caminho* dentro do `JSONResponse`.

Ele usará o código de status padrão ou o que você definir na sua *operação de caminho*.

## Códigos de status adicionais

Caso você queira retornar códigos de status adicionais além do código principal, você pode fazer isso retornando um `Response` diretamente, como por exemplo um `JSONResponse`, e definir os códigos de status adicionais diretamente.

Por exemplo, vamos dizer que você deseja ter uma *operação de caminho* que permita atualizar itens, e retornar um código de status HTTP 200 "OK" quando for bem sucedido.

Mas você também deseja aceitar novos itens. E quando os itens não existiam, ele os cria, e retorna o código de status HTTP 201 "Created.

Para conseguir isso, importe `JSONResponse` e retorne o seu conteúdo diretamente, definindo o `status_code` que você deseja:

{* ../../examples/additional_status_codes/tutorial001_an_py310.py hl[4,25] *}

/// warning | Aviso

Quando você retorna um `Response` diretamente, como no exemplo acima, ele será retornado diretamente.

Ele não será serializado com um modelo, etc.

Garanta que ele tenha toda informação que você deseja, e que os valores sejam um JSON válido (caso você esteja usando `JSONResponse`).

///

/// note | Detalhes técnicos

Você também pode utilizar `from starlette.responses import JSONResponse`.

O **ReadyAPI** disponibiliza o `starlette.responses` como `readyapi.responses` apenas por conveniência para você, o programador. Porém a maioria dos retornos disponíveis vem diretamente do Starlette. O mesmo com `status`.

///

## OpenAPI e documentação da API

Se você retorna códigos de status adicionais e retornos diretamente, eles não serão incluídos no esquema do OpenAPI (a documentação da API), porque o ReadyAPI não tem como saber de antemão o que será retornado.

Mas você pode documentar isso no seu código, utilizando: [Retornos Adicionais](additional-responses.md){.internal-link target=_blank}.

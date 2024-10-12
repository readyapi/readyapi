# Configuração da Operação de Rota

Existem vários parâmetros que você pode passar para o seu _decorador de operação de rota_ para configurá-lo.

/// warning | "Aviso"

Observe que esses parâmetros são passados diretamente para o _decorador de operação de rota_, não para a sua _função de operação de rota_.

///

## Código de Status da Resposta

Você pode definir o `status_code` (HTTP) para ser usado na resposta da sua _operação de rota_.

Você pode passar diretamente o código `int`, como `404`.

Mas se você não se lembrar o que cada código numérico significa, pode usar as constantes de atalho em `status`:

//// tab | Python 3.8 and above

```Python hl_lines="3  17"
{!> ../../docs_src/path_operation_configuration/tutorial001.py!}
```

////

//// tab | Python 3.9 and above

```Python hl_lines="3  17"
{!> ../../docs_src/path_operation_configuration/tutorial001_py39.py!}
```

////

//// tab | Python 3.10 and above

```Python hl_lines="1  15"
{!> ../../docs_src/path_operation_configuration/tutorial001_py310.py!}
```

////

Esse código de status será usado na resposta e será adicionado ao esquema OpenAPI.

/// note | "Detalhes Técnicos"

Você também poderia usar `from starlette import status`.

**ReadyAPI** fornece o mesmo `starlette.status` como `readyapi.status` apenas como uma conveniência para você, o desenvolvedor. Mas vem diretamente do Starlette.

///

## Tags

Você pode adicionar tags para sua _operação de rota_, passe o parâmetro `tags` com uma `list` de `str` (comumente apenas um `str`):

//// tab | Python 3.8 and above

```Python hl_lines="17  22  27"
{!> ../../docs_src/path_operation_configuration/tutorial002.py!}
```

////

//// tab | Python 3.9 and above

```Python hl_lines="17  22  27"
{!> ../../docs_src/path_operation_configuration/tutorial002_py39.py!}
```

////

//// tab | Python 3.10 and above

```Python hl_lines="15  20  25"
{!> ../../docs_src/path_operation_configuration/tutorial002_py310.py!}
```

////

Eles serão adicionados ao esquema OpenAPI e usados pelas interfaces de documentação automática:

<img src="/img/tutorial/path-operation-configuration/image01.png">

### Tags com Enums

Se você tem uma grande aplicação, você pode acabar acumulando **várias tags**, e você gostaria de ter certeza de que você sempre usa a **mesma tag** para _operações de rota_ relacionadas.

Nestes casos, pode fazer sentido armazenar as tags em um `Enum`.

**ReadyAPI** suporta isso da mesma maneira que com strings simples:

```Python hl_lines="1  8-10  13  18"
{!../../docs_src/path_operation_configuration/tutorial002b.py!}
```

## Resumo e descrição

Você pode adicionar um `summary` e uma `description`:

//// tab | Python 3.8 and above

```Python hl_lines="20-21"
{!> ../../docs_src/path_operation_configuration/tutorial003.py!}
```

////

//// tab | Python 3.9 and above

```Python hl_lines="20-21"
{!> ../../docs_src/path_operation_configuration/tutorial003_py39.py!}
```

////

//// tab | Python 3.10 and above

```Python hl_lines="18-19"
{!> ../../docs_src/path_operation_configuration/tutorial003_py310.py!}
```

////

## Descrição do docstring

Como as descrições tendem a ser longas e cobrir várias linhas, você pode declarar a descrição da _operação de rota_ na <abbr title="uma string de várias linhas como a primeira expressão dentro de uma função (não atribuída a nenhuma variável) usada para documentação">docstring</abbr> da função e o **ReadyAPI** irá lê-la de lá.

Você pode escrever <a href="https://en.wikipedia.org/wiki/Markdown" class="external-link" target="_blank">Markdown</a> na docstring, ele será interpretado e exibido corretamente (levando em conta a indentação da docstring).

//// tab | Python 3.8 and above

```Python hl_lines="19-27"
{!> ../../docs_src/path_operation_configuration/tutorial004.py!}
```

////

//// tab | Python 3.9 and above

```Python hl_lines="19-27"
{!> ../../docs_src/path_operation_configuration/tutorial004_py39.py!}
```

////

//// tab | Python 3.10 and above

```Python hl_lines="17-25"
{!> ../../docs_src/path_operation_configuration/tutorial004_py310.py!}
```

////

Ela será usada nas documentações interativas:

<img src="/img/tutorial/path-operation-configuration/image02.png">

## Descrição da resposta

Você pode especificar a descrição da resposta com o parâmetro `response_description`:

//// tab | Python 3.8 and above

```Python hl_lines="21"
{!> ../../docs_src/path_operation_configuration/tutorial005.py!}
```

////

//// tab | Python 3.9 and above

```Python hl_lines="21"
{!> ../../docs_src/path_operation_configuration/tutorial005_py39.py!}
```

////

//// tab | Python 3.10 and above

```Python hl_lines="19"
{!> ../../docs_src/path_operation_configuration/tutorial005_py310.py!}
```

////

/// info | "Informação"

Note que `response_description` se refere especificamente à resposta, a `description` se refere à _operação de rota_ em geral.

///

/// check

OpenAPI especifica que cada _operação de rota_ requer uma descrição de resposta.

Então, se você não fornecer uma, o **ReadyAPI** irá gerar automaticamente uma de "Resposta bem-sucedida".

///

<img src="/img/tutorial/path-operation-configuration/image03.png">

## Depreciar uma _operação de rota_

Se você precisar marcar uma _operação de rota_ como <abbr title="obsoleta, recomendada não usá-la">descontinuada</abbr>, mas sem removê-la, passe o parâmetro `deprecated`:

```Python hl_lines="16"
{!../../docs_src/path_operation_configuration/tutorial006.py!}
```

Ela será claramente marcada como descontinuada nas documentações interativas:

<img src="/img/tutorial/path-operation-configuration/image04.png">

Verifique como _operações de rota_ descontinuadas e não descontinuadas se parecem:

<img src="/img/tutorial/path-operation-configuration/image05.png">

## Resumindo

Você pode configurar e adicionar metadados para suas _operações de rota_ facilmente passando parâmetros para os _decoradores de operação de rota_.

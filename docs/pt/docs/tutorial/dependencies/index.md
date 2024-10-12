# Dependências

O **ReadyAPI** possui um poderoso, mas intuitivo sistema de **<abbr title="também conhecidos como, recursos, provedores, serviços, injetáveis">Injeção de Dependência</abbr>**.

Esse sistema foi pensado para ser fácil de usar, e permitir que qualquer desenvolvedor possa integrar facilmente outros componentes ao **ReadyAPI**.

## O que é "Injeção de Dependência"

**"Injeção de Dependência"** no mundo da programação significa, que existe uma maneira de declarar no seu código (nesse caso, suas _funções de operação de rota_) para declarar as coisas que ele precisa para funcionar e que serão utilizadas: "dependências".

Então, esse sistema (nesse caso o **ReadyAPI**) se encarrega de fazer o que for preciso para fornecer essas dependências para o código ("injetando" as dependências).

Isso é bastante útil quando você precisa:

- Definir uma lógica compartilhada (mesmo formato de código repetidamente).
- Compartilhar conexões com banco de dados.
- Aplicar regras de segurança, autenticação, papéis de usuários, etc.
- E muitas outras coisas...

Tudo isso, enquanto minimizamos a repetição de código.

## Primeiros passos

Vamos ver um exemplo simples. Tão simples que não será muito útil, por enquanto.

Mas dessa forma podemos focar em como o sistema de **Injeção de Dependência** funciona.

### Criando uma dependência, ou "injetável"

Primeiro vamos focar na dependência.

Ela é apenas uma função que pode receber os mesmos parâmetros de uma _função de operação de rota_:

//// tab | Python 3.10+

```Python hl_lines="8-9"
{!> ../../docs_src/dependencies/tutorial001_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="8-11"
{!> ../../docs_src/dependencies/tutorial001_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="9-12"
{!> ../../docs_src/dependencies/tutorial001_an.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="6-7"
{!> ../../docs_src/dependencies/tutorial001_py310.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="8-11"
{!> ../../docs_src/dependencies/tutorial001.py!}
```

////

E pronto.

**2 linhas**.

E com a mesma forma e estrutura de todas as suas _funções de operação de rota_.

Você pode pensar nela como uma _função de operação de rota_ sem o "decorador" (sem a linha `@app.get("/some-path")`).

E com qualquer retorno que você desejar.

Neste caso, a dependência espera por:

- Um parâmetro de consulta opcional `q` do tipo `str`.
- Um parâmetro de consulta opcional `skip` do tipo `int`, e igual a `0` por padrão.
- Um parâmetro de consulta opcional `limit` do tipo `int`, e igual a `100` por padrão.

E então retorna um `dict` contendo esses valores.

/// info | "Informação"

ReadyAPI passou a suportar a notação `Annotated` (e começou a recomendá-la) na versão 0.95.0.

Se você utiliza uma versão anterior, ocorrerão erros ao tentar utilizar `Annotated`.

Certifique-se de [Atualizar a versão do ReadyAPI](../../deployment/versions.md#atualizando-as-versoes-do-readyapi){.internal-link target=\_blank} para pelo menos 0.95.1 antes de usar `Annotated`.

///

### Importando `Depends`

//// tab | Python 3.10+

```Python hl_lines="3"
{!> ../../docs_src/dependencies/tutorial001_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="3"
{!> ../../docs_src/dependencies/tutorial001_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="3"
{!> ../../docs_src/dependencies/tutorial001_an.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="1"
{!> ../../docs_src/dependencies/tutorial001_py310.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="3"
{!> ../../docs_src/dependencies/tutorial001.py!}
```

////

### Declarando a dependência, no "dependente"

Da mesma forma que você utiliza `Body`, `Query`, etc. Como parâmetros de sua _função de operação de rota_, utilize `Depends` com um novo parâmetro:

//// tab | Python 3.10+

```Python hl_lines="13  18"
{!> ../../docs_src/dependencies/tutorial001_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="15  20"
{!> ../../docs_src/dependencies/tutorial001_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="16  21"
{!> ../../docs_src/dependencies/tutorial001_an.py!}
```

////

//// tab | Python 3.10+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="11  16"
{!> ../../docs_src/dependencies/tutorial001_py310.py!}
```

////

//// tab | Python 3.8+ non-Annotated

/// tip | "Dica"

Utilize a versão com `Annotated` se possível.

///

```Python hl_lines="15  20"
{!> ../../docs_src/dependencies/tutorial001.py!}
```

////

Ainda que `Depends` seja utilizado nos parâmetros da função da mesma forma que `Body`, `Query`, etc, `Depends` funciona de uma forma um pouco diferente.

Você fornece um único parâmetro para `Depends`.

Esse parâmetro deve ser algo como uma função.

Você **não chama a função** diretamente (não adicione os parênteses no final), apenas a passe como parâmetro de `Depends()`.

E essa função vai receber os parâmetros da mesma forma que uma _função de operação de rota_.

/// tip | "Dica"

Você verá quais outras "coisas", além de funções, podem ser usadas como dependências no próximo capítulo.

///

Sempre que uma nova requisição for realizada, o **ReadyAPI** se encarrega de:

- Chamar sua dependência ("injetável") com os parâmetros corretos.
- Obter o resultado da função.
- Atribuir esse resultado para o parâmetro em sua _função de operação de rota_.

```mermaid
graph TB

common_parameters(["common_parameters"])
read_items["/items/"]
read_users["/users/"]

common_parameters --> read_items
common_parameters --> read_users
```

Assim, você escreve um código compartilhado apenas uma vez e o **ReadyAPI** se encarrega de chamá-lo em suas _operações de rota_.

/// check | "Checando"

Perceba que você não precisa criar uma classe especial e enviar a dependência para algum outro lugar em que o **ReadyAPI** a "registre" ou realize qualquer operação similar.

Você apenas envia para `Depends` e o **ReadyAPI** sabe como fazer o resto.

///

## Compartilhando dependências `Annotated`

Nos exemplos acima, você pode ver que existe uma pequena **duplicação de código**.

Quando você precisa utilizar a dependência `common_parameters()`, você precisa escrever o parâmetro inteiro com uma anotação de tipo e `Depends()`:

```Python
commons: Annotated[dict, Depends(common_parameters)]
```

Mas como estamos utilizando `Annotated`, podemos guardar esse valor `Annotated` em uma variável e utilizá-la em múltiplos locais:

//// tab | Python 3.10+

```Python hl_lines="12  16  21"
{!> ../../docs_src/dependencies/tutorial001_02_an_py310.py!}
```

////

//// tab | Python 3.9+

```Python hl_lines="14  18  23"
{!> ../../docs_src/dependencies/tutorial001_02_an_py39.py!}
```

////

//// tab | Python 3.8+

```Python hl_lines="15  19  24"
{!> ../../docs_src/dependencies/tutorial001_02_an.py!}
```

////

/// tip | "Dica"

Isso é apenas Python padrão, essa funcionalidade é chamada de "type alias", e na verdade não é específica ao **ReadyAPI**.

Mas como o **ReadyAPI** se baseia em convenções do Python, incluindo `Annotated`, você pode incluir esse truque no seu código. 😎

///

As dependências continuarão funcionando como esperado, e a **melhor parte** é que a **informação sobre o tipo é preservada**, o que signfica que seu editor de texto ainda irá incluir **preenchimento automático**, **visualização de erros**, etc. O mesmo vale para ferramentas como `mypy`.

Isso é especialmente útil para uma **base de código grande** onde **as mesmas dependências** são utilizadas repetidamente em **muitas _operações de rota_**.

## `Async` ou não, eis a questão

Como as dependências também serão chamadas pelo **ReadyAPI** (da mesma forma que _funções de operação de rota_), as mesmas regras se aplicam ao definir suas funções.

Você pode utilizar `async def` ou apenas `def`.

E você pode declarar dependências utilizando `async def` dentro de _funções de operação de rota_ definidas com `def`, ou declarar dependências com `def` e utilizar dentro de _funções de operação de rota_ definidas com `async def`, etc.

Não faz diferença. O **ReadyAPI** sabe o que fazer.

/// note | "Nota"

Caso você não conheça, veja em [Async: _"Com Pressa?"_](../../async.md#com-pressa){.internal-link target=\_blank} a sessão acerca de `async` e `await` na documentação.

///

## Integrando com OpenAPI

Todas as declarações de requisições, validações e requisitos para suas dependências (e sub-dependências) serão integradas em um mesmo esquema OpenAPI.

Então, a documentação interativa também terá toda a informação sobre essas dependências:

<img src="/img/tutorial/dependencies/image01.png">

## Caso de Uso Simples

Se você parar para ver, _funções de operação de rota_ são declaradas para serem usadas sempre que uma _rota_ e uma _operação_ se encaixam, e então o **ReadyAPI** se encarrega de chamar a função correspondente com os argumentos corretos, extraindo os dados da requisição.

Na verdade, todos (ou a maioria) dos frameworks web funcionam da mesma forma.

Você nunca chama essas funções diretamente. Elas são chamadas pelo framework utilizado (nesse caso, **ReadyAPI**).

Com o Sistema de Injeção de Dependência, você também pode informar ao **ReadyAPI** que sua _função de operação de rota_ também "depende" em algo a mais que deve ser executado antes de sua _função de operação de rota_, e o **ReadyAPI** se encarrega de executar e "injetar" os resultados.

Outros termos comuns para essa mesma ideia de "injeção de dependência" são:

- recursos
- provedores
- serviços
- injetáveis
- componentes

## Plug-ins em **ReadyAPI**

Integrações e "plug-ins" podem ser construídos com o sistema de **Injeção de Dependência**. Mas na verdade, **não há necessidade de criar "plug-ins"**, já que utilizando dependências é possível declarar um número infinito de integrações e interações que se tornam disponíveis para as suas _funções de operação de rota_.

E as dependências pode ser criadas de uma forma bastante simples e intuitiva que permite que você importe apenas os pacotes Python que forem necessários, e integrá-los com as funções de sua API em algumas linhas de código, _literalmente_.

Você verá exemplos disso nos próximos capítulos, acerca de bancos de dados relacionais e NoSQL, segurança, etc.

## Compatibilidade do **ReadyAPI**

A simplicidade do sistema de injeção de dependência do **ReadyAPI** faz ele compatível com:

- todos os bancos de dados relacionais
- bancos de dados NoSQL
- pacotes externos
- APIs externas
- sistemas de autenticação e autorização
- istemas de monitoramento de uso para APIs
- sistemas de injeção de dados de resposta
- etc.

## Simples e Poderoso

Mesmo que o sistema hierárquico de injeção de dependência seja simples de definir e utilizar, ele ainda é bastante poderoso.

Você pode definir dependências que por sua vez definem suas próprias dependências.

No fim, uma árvore hierárquica de dependências é criadas, e o sistema de **Injeção de Dependência** toma conta de resolver todas essas dependências (e as sub-dependências delas) para você, e provê (injeta) os resultados em cada passo.

Por exemplo, vamos supor que você possua 4 endpoints na sua API (_operações de rota_):

- `/items/public/`
- `/items/private/`
- `/users/{user_id}/activate`
- `/items/pro/`

Você poderia adicionar diferentes requisitos de permissão para cada um deles utilizando apenas dependências e sub-dependências:

```mermaid
graph TB

current_user(["current_user"])
active_user(["active_user"])
admin_user(["admin_user"])
paying_user(["paying_user"])

public["/items/public/"]
private["/items/private/"]
activate_user["/users/{user_id}/activate"]
pro_items["/items/pro/"]

current_user --> active_user
active_user --> admin_user
active_user --> paying_user

current_user --> public
active_user --> private
admin_user --> activate_user
paying_user --> pro_items
```

## Integração com **OpenAPI**

Todas essas dependências, ao declarar os requisitos para suas _operações de rota_, também adicionam parâmetros, validações, etc.

O **ReadyAPI** se encarrega de adicionar tudo isso ao esquema OpenAPI, para que seja mostrado nos sistemas de documentação interativa.

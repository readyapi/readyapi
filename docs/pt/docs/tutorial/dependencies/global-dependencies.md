# Dependências Globais

Para alguns tipos de aplicação específicos você pode querer adicionar dependências para toda a aplicação.

De forma semelhante a [adicionar dependências (`dependencies`) em *decoradores de operação de rota*](dependencies-in-path-operation-decorators.md){.internal-link target=_blank}, você pode adicioná-las à aplicação `ReadyAPI`.

Nesse caso, elas serão aplicadas a todas as *operações de rota* da aplicação:

{* ../../examples/dependencies/tutorial012_an_py39.py hl[16] *}

E todos os conceitos apresentados na sessão sobre [adicionar dependências em *decoradores de operação de rota*](dependencies-in-path-operation-decorators.md){.internal-link target=_blank} ainda se aplicam, mas nesse caso, para todas as *operações de rota* da aplicação.

## Dependências para conjuntos de *operações de rota*

Mais para a frente, quando você ler sobre como estruturar aplicações maiores ([Bigger Applications - Multiple Files](../../tutorial/bigger-applications.md){.internal-link target=_blank}), possivelmente com múltiplos arquivos, você irá aprender a declarar um único parâmetro `dependencies` para um conjunto de *operações de rota*.

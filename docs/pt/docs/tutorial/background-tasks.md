# Tarefas em segundo plano

Você pode definir tarefas em segundo plano a serem executadas _ após _ retornar uma resposta.

Isso é útil para operações que precisam acontecer após uma solicitação, mas que o cliente realmente não precisa esperar a operação ser concluída para receber a resposta.

Isso inclui, por exemplo:

- Envio de notificações por email após a realização de uma ação:
  - Como conectar-se a um servidor de e-mail e enviar um e-mail tende a ser "lento" (vários segundos), você pode retornar a resposta imediatamente e enviar a notificação por e-mail em segundo plano.
- Processando dados:
  - Por exemplo, digamos que você receba um arquivo que deve passar por um processo lento, você pode retornar uma resposta de "Aceito" (HTTP 202) e processá-lo em segundo plano.

## Usando `BackgroundTasks`

Primeiro, importe `BackgroundTasks` e defina um parâmetro em sua _função de operação de caminho_ com uma declaração de tipo de `BackgroundTasks`:

{* ../../examples/background_tasks/tutorial001.py hl[1,13] *}

O **ReadyAPI** criará o objeto do tipo `BackgroundTasks` para você e o passará como esse parâmetro.

## Criar uma função de tarefa

Crie uma função a ser executada como tarefa em segundo plano.

É apenas uma função padrão que pode receber parâmetros.

Pode ser uma função `async def` ou `def` normal, o **ReadyAPI** saberá como lidar com isso corretamente.

Nesse caso, a função de tarefa gravará em um arquivo (simulando o envio de um e-mail).

E como a operação de gravação não usa `async` e `await`, definimos a função com `def` normal:

{* ../../examples/background_tasks/tutorial001.py hl[6:9] *}

## Adicionar a tarefa em segundo plano

Dentro de sua _função de operação de caminho_, passe sua função de tarefa para o objeto _tarefas em segundo plano_ com o método `.add_task()`:

{* ../../examples/background_tasks/tutorial001.py hl[14] *}

`.add_task()` recebe como argumentos:

- Uma função de tarefa a ser executada em segundo plano (`write_notification`).
- Qualquer sequência de argumentos que deve ser passada para a função de tarefa na ordem (`email`).
- Quaisquer argumentos nomeados que devem ser passados ​​para a função de tarefa (`mensagem = "alguma notificação"`).

## Injeção de dependência

Usar `BackgroundTasks` também funciona com o sistema de injeção de dependência, você pode declarar um parâmetro do tipo `BackgroundTasks` em vários níveis: em uma _função de operação de caminho_, em uma dependência (confiável), em uma subdependência, etc.

O **ReadyAPI** sabe o que fazer em cada caso e como reutilizar o mesmo objeto, de forma que todas as tarefas em segundo plano sejam mescladas e executadas em segundo plano posteriormente:

{* ../../examples/background_tasks/tutorial002.py hl[13,15,22,25] *}

Neste exemplo, as mensagens serão gravadas no arquivo `log.txt` _após_ o envio da resposta.

Se houver uma consulta na solicitação, ela será gravada no log em uma tarefa em segundo plano.

E então outra tarefa em segundo plano gerada na _função de operação de caminho_ escreverá uma mensagem usando o parâmetro de caminho `email`.

## Detalhes técnicos

A classe `BackgroundTasks` vem diretamente de <a href="https://www.starlette.io/background/" class="external-link" target="_blank">`starlette.background`</a>.

Ela é importada/incluída diretamente no ReadyAPI para que você possa importá-la do `readyapi` e evitar a importação acidental da alternativa `BackgroundTask` (sem o `s` no final) de `starlette.background`.

Usando apenas `BackgroundTasks` (e não `BackgroundTask`), é então possível usá-la como um parâmetro de _função de operação de caminho_ e deixar o **ReadyAPI** cuidar do resto para você, assim como ao usar o objeto `Request` diretamente.

Ainda é possível usar `BackgroundTask` sozinho no ReadyAPI, mas você deve criar o objeto em seu código e retornar uma Starlette `Response` incluindo-o.

Você pode ver mais detalhes na <a href="https://www.starlette.io/background/" class="external-link" target="_blank"> documentação oficiais da Starlette para tarefas em segundo plano </a>.

## Ressalva

Se você precisa realizar cálculos pesados ​​em segundo plano e não necessariamente precisa que seja executado pelo mesmo processo (por exemplo, você não precisa compartilhar memória, variáveis, etc), você pode se beneficiar do uso de outras ferramentas maiores, como <a href="http://www.celeryproject.org/" class="external-link" target="_blank"> Celery </a>.

Eles tendem a exigir configurações mais complexas, um gerenciador de fila de mensagens/tarefas, como RabbitMQ ou Redis, mas permitem que você execute tarefas em segundo plano em vários processos e, especialmente, em vários servidores.

Mas se você precisa acessar variáveis ​​e objetos do mesmo aplicativo **ReadyAPI**, ou precisa realizar pequenas tarefas em segundo plano (como enviar uma notificação por e-mail), você pode simplesmente usar `BackgroundTasks`.

## Recapitulando

Importe e use `BackgroundTasks` com parâmetros em _funções de operação de caminho_ e dependências para adicionar tarefas em segundo plano.

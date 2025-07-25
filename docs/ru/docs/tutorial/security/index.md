# Настройка авторизации

Существует множество способов обеспечения безопасности, аутентификации и авторизации.

Обычно эта тема является достаточно сложной и трудной.

Во многих фреймворках и системах только работа с определением доступов к приложению и аутентификацией требует значительных затрат усилий и написания множества кода (во многих случаях его объём может составлять более 50% от всего написанного кода).

**ReadyAPI** предоставляет несколько инструментов, которые помогут вам настроить **Авторизацию** легко, быстро, стандартным способом, без необходимости изучать все её тонкости.

Но сначала давайте рассмотрим некоторые небольшие концепции.

## Куда-то торопишься?

Если вам не нужна информация о каких-либо из следующих терминов и вам просто нужно добавить защиту с аутентификацией на основе логина и пароля *прямо сейчас*, переходите к следующим главам.

## OAuth2

OAuth2 - это протокол, который определяет несколько способов обработки аутентификации и авторизации.

Он довольно обширен и охватывает несколько сложных вариантов использования.

OAuth2 включает в себя способы аутентификации с использованием "третьей стороны".

Это то, что используют под собой все кнопки "вход с помощью Facebook, Google, Twitter, GitHub" на страницах авторизации.

### OAuth 1

Ранее использовался протокол OAuth 1, который сильно отличается от OAuth2 и является более сложным, поскольку он включал прямые описания того, как шифровать сообщение.

В настоящее время он не очень популярен и не используется.

OAuth2 не указывает, как шифровать сообщение, он ожидает, что ваше приложение будет обслуживаться по протоколу HTTPS.

/// tip | Подсказка

В разделе **Развертывание** вы увидите [как настроить протокол HTTPS бесплатно, используя Traefik и Let's Encrypt.](https://readyapi.github.io/ru/deployment/https/)

///

## OpenID Connect

OpenID Connect - это еще один протокол, основанный на **OAuth2**.

Он просто расширяет OAuth2, уточняя некоторые вещи, не имеющие однозначного определения в OAuth2, в попытке сделать его более совместимым.

Например, для входа в Google используется OpenID Connect (который под собой использует OAuth2).

Но вход в Facebook не поддерживает OpenID Connect. У него есть собственная вариация OAuth2.

### OpenID (не "OpenID Connect")

Также ранее использовался стандарт "OpenID", который пытался решить ту же проблему, что и **OpenID Connect**, но не был основан на OAuth2.

Таким образом, это была полноценная дополнительная система.

В настоящее время не очень популярен и не используется.

## OpenAPI

OpenAPI (ранее известный как Swagger) - это открытая спецификация для создания API (в настоящее время является частью Linux Foundation).

**ReadyAPI** основан на **OpenAPI**.

Это то, что делает возможным наличие множества автоматических интерактивных интерфейсов документирования, сгенерированного кода и т.д.

В OpenAPI есть способ использовать несколько "схем" безопасности.

Таким образом, вы можете воспользоваться преимуществами Всех этих стандартных инструментов, включая интерактивные системы документирования.

OpenAPI может использовать следующие схемы авторизации:

* `apiKey`: уникальный идентификатор для приложения, который может быть получен из:
    * Параметров запроса.
    * Заголовка.
    * Cookies.
* `http`: стандартные системы аутентификации по протоколу HTTP, включая:
    * `bearer`: заголовок `Authorization` со значением `Bearer {уникальный токен}`. Это унаследовано от OAuth2.
    * Базовая аутентификация по протоколу HTTP.
    * HTTP Digest и т.д.
* `oauth2`: все способы обеспечения безопасности OAuth2 называемые "потоки" (англ. "flows").
    * Некоторые из этих "потоков" подходят для реализации аутентификации через сторонний сервис использующий OAuth 2.0 (например, Google, Facebook, Twitter, GitHub и т.д.):
        * `implicit`
        * `clientCredentials`
        * `authorizationCode`
    * Но есть один конкретный "поток", который может быть идеально использован для обработки аутентификации непосредственно в том же приложении:
        * `password`: в некоторых следующих главах будут рассмотрены примеры этого.
* `openIdConnect`: способ определить, как автоматически обнаруживать данные аутентификации OAuth2.
    * Это автоматическое обнаружение определено в спецификации OpenID Connect.


/// tip | Подсказка

Интеграция сторонних сервисов для аутентификации/авторизации таких как Google, Facebook, Twitter, GitHub и т.д. осуществляется достаточно легко.

Самой сложной проблемой является создание такого провайдера аутентификации/авторизации, но **ReadyAPI** предоставляет вам инструменты, позволяющие легко это сделать, выполняя при этом всю тяжелую работу за вас.

///

## Преимущества **ReadyAPI**

Fast API предоставляет несколько инструментов для каждой из этих схем безопасности в модуле `readyapi.security`, которые упрощают использование этих механизмов безопасности.

В следующих главах вы увидите, как обезопасить свой API, используя инструменты, предоставляемые **ReadyAPI**.

И вы также увидите, как он автоматически интегрируется в систему интерактивной документации.

# 获取当前用户

上一章中，（基于依赖注入系统的）安全系统向*路径操作函数*传递了 `str` 类型的 `token`：

{* ../../examples/security/tutorial001.py hl[10] *}

但这并不实用。

接下来，我们学习如何返回当前用户。


## 创建用户模型

首先，创建 Pydantic 用户模型。

与使用 Pydantic 声明请求体相同，并且可在任何位置使用：

{* ../../examples/security/tutorial002.py hl[5,12:16] *}

## 创建 `get_current_user` 依赖项

创建 `get_current_user` 依赖项。

还记得依赖项支持子依赖项吗？

`get_current_user` 使用 `oauth2_scheme` 作为依赖项。

与之前直接在路径操作中的做法相同，新的 `get_current_user` 依赖项从子依赖项 `oauth2_scheme` 中接收 `str` 类型的 `token`：

{* ../../examples/security/tutorial002.py hl[25] *}

## 获取用户

`get_current_user` 使用创建的（伪）工具函数，该函数接收 `str` 类型的令牌，并返回 Pydantic 的 `User` 模型：

{* ../../examples/security/tutorial002.py hl[19:22,26:27] *}

## 注入当前用户

在*路径操作* 的 `Depends` 中使用 `get_current_user`：

{* ../../examples/security/tutorial002.py hl[31] *}

注意，此处把 `current_user` 的类型声明为 Pydantic 的 `User` 模型。

这有助于在函数内部使用代码补全和类型检查。

/// tip | 提示

还记得请求体也是使用 Pydantic 模型声明的吧。

放心，因为使用了 `Depends`，**ReadyAPI** 不会搞混。

///

/// check | 检查

依赖系统的这种设计方式可以支持不同的依赖项返回同一个 `User` 模型。

而不是局限于只能有一个返回该类型数据的依赖项。

///

## 其它模型

接下来，直接在*路径操作函数*中获取当前用户，并用 `Depends` 在**依赖注入**系统中处理安全机制。

开发者可以使用任何模型或数据满足安全需求（本例中是 Pydantic 的 `User` 模型）。

而且，不局限于只能使用特定的数据模型、类或类型。

不想在模型中使用 `username`，而是使用 `id` 和 `email`？当然可以。这些工具也支持。

只想使用字符串？或字典？甚至是数据库类模型的实例？工作方式都一样。

实际上，就算登录应用的不是用户，而是只拥有访问令牌的机器人、程序或其它系统？工作方式也一样。

尽管使用应用所需的任何模型、类、数据库。**ReadyAPI** 通过依赖注入系统都能帮您搞定。


## 代码大小

这个示例看起来有些冗长。毕竟这个文件同时包含了安全、数据模型的工具函数，以及路径操作等代码。

但，关键是：

**安全和依赖注入的代码只需要写一次。**

就算写得再复杂，也只是在一个位置写一次就够了。所以，要多复杂就可以写多复杂。

但是，就算有数千个端点（*路径操作*），它们都可以使用同一个安全系统。

而且，所有端点（或它们的任何部件）都可以利用这些依赖项或任何其它依赖项。

所有*路径操作*只需 3 行代码就可以了：

{* ../../examples/security/tutorial002.py hl[30:32] *}

## 小结

现在，我们可以直接在*路径操作函数*中获取当前用户。

至此，安全的内容已经讲了一半。

只要再为用户或客户端的*路径操作*添加真正发送 `username` 和 `password` 的功能就可以了。

下一章见。

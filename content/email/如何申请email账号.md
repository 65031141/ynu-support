Title: 申请邮箱账号
Tags: email, apply for
Authors: 刘东华
Summary: 这篇文章的简短描述
Lang: zh

这是`申请邮箱账号`的内容。

::uml:: format="png" alt="Sample sequence diagram"
  participant User

  User -> A: DoWork
  activate A #FFBBBB

  A -> A: Internal call
  activate A #DarkSalmon

  A -> B: << createRequest >>
  activate B

  B --> A: RequestCreated
  deactivate B
  deactivate A
  A -> User: Done
  deactivate A
::end-uml::

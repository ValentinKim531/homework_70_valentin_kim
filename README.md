## 🌍 passwords and logins for webapp:
```text
login: admin, password: admin
login: root, password: 1234
login: manager, password: manager
login: lead, password: lead
login: dev, password: dev
```


---

 # 🧑‍💻 DetailView, UpdateView и DeleteView для API тасктрекера

 ## 📃 DetailView
---
 **Для детального просмотра задачи необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` 
  <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a> , используя метод `GET`, указать следущий путь, на примере задачи с *id=1*: 
  
```python
    http://127.0.0.1:8000/api/issue/1
```

и нажать кнопку `Send`

***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 1,
    "summary": "Homework # 57",
    "description": "Homework # 57",
    "type": [
        1
    ],
    "status": 1,
    "project": 2
}
```

**Для детального просмотра проекта необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `GET`, указать следущий путь, на примере проекта с *id=2*: 

```python
    http://127.0.0.1:8000/api/project/2
```
 * нажать кнопку `Send`

***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 2,
    "start_date": "2023-03-10",
    "end_date": "2023-03-31",
    "title": "Django Model tutorial",
    "description": "Django web applications access and manage data through Python objects referred to as models.",
    "users": [
        1,
        34,
        32
    ]
}
```
---
## 📝 UpdateView

**Для обновления/редактирования задачи необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `PUT`, указать следущий путь, на примере задачи с *id=1*:
  
```python 
    http://127.0.0.1:8000/api/issue-update/1
```

 *  добавить в `Body > raw` словарик данной задачи с желаемыми изменениями для обновления, например: 

```python
    {
    "summary": "Homework # 100",
    "description": "Homework # 100",
    "type": [
        1
    ],
    "status": 1,
    "project": 2
    }
```

 * нажать кнопку `Send`
  
***Результат запроса будет отражен в следующем виде:***

```python
    {
        "id": 1,
        "summary": "Homework # 100",
        "description": "Homework # 100",
        "type": [
            1
        ],
        "status": 1,
        "project": 2
    }
```

**Для обновления/редактирования проекта необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `PUT`, указать следущий путь, на примере задачи с *id=2*: 

```python
    http://127.0.0.1:8000/api/project-update/2
```

 * добавить в `Body > raw` словарь данного проекта с желаемыми изменениями для обновления, например: 

```python
    {
    "id": 2,
    "start_date": "2023-03-10",
    "end_date": "2023-03-31",
    "title": "Django Model tutorial",
    "description": "New description",
    "users": [
        1,
        34,
        32
    ]
}
```

 * нажать кнопку `Send`
  
***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 2,
    "start_date": "2023-03-10",
    "end_date": "2023-03-31",
    "title": "Django Model tutorial",
    "description": "New description",
    "users": [
        1,
        34,
        32
    ]
}
```
---
## 📫 DeleteView

**Для удаления задачи необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `DELETE`, указать следущий путь, на примере задачи с *id=1*: 
  
```python
    http://127.0.0.1:8000/api/issue-delete/1
```

 * нажать кнопку `Send`

***При успешном исполнениии результат запроса будет отражен в следующем виде:***

```python
    {
        "Задача была успешно удалена, со следующим ID:": 1
    }
```

**Для удаления проекта необходимо:**

 *  запустить приложение путем набора в терминале "./manage.py runserver"
 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `DELETE`, указать следущий путь, на примере проекта с *id=2*: 
  
```python
    http://127.0.0.1:8000/api/project-delete/2
```

 * нажать кнопку `Send`

***При успешном исполнениии результат запроса будет отражен в следующем виде:***

```python
    {
        "Проект был успешно удален, со следующим ID:": 2
    }
```

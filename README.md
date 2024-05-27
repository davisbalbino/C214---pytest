# C214---pytest

### **Pytest para a App de Task**

### **Introdução**

O pytest é um framework de teste poderoso e fácil de usar para Python. Ele suporta testes de funcionalidades, testes de unidade e testes de integração. Nesta documentação, vamos cobrir como usar o pytest para testar a nossa aplicação de gerenciamento de tarefas.

### **Instalação**

Antes de começar, é necessário garantir que o pytest esteja instalado. Abra um terminal e execute o seguinte comando:

```python
pip install pytest
```

### **Estrutura do Projeto**

A estrutura do projeto é organizada da seguinte forma:

```markdown

project/
│
├── app.py
├── task/
│   ├── __init__.py
│   ├── task.py
│   ├── task_manager.py
│   ├── user.py
│   └── user_manager.py
│
└── tests/
    ├── __init__.py
    ├── test_task.py
    ├── test_task_manager.py
    ├── test_user.py
    └── test_user_manager.py

```

- **app.py**: Arquivo principal da aplicação Flask.
- **task/**: Diretório contendo as classes relacionadas às tarefas e usuários.
- **tests/**: Diretório contendo os testes unitários.

### **Testes Unitários com Pytest**

Vamos criar testes unitários para as classes **`Task`**, **`TaskManager`**, **`User`**, e **`UserManager`**.

### **Teste da Classe `Task`**

### **`tests/test_task.py`**

```python
import pytest
from task.task import Task

def test_task_creation():
    task = Task("Test Task", "This is a test task.")
    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.completed is False

def test_mark_as_completed():
    task = Task("Test Task", "This is a test task.")
    task.mark_as_completed()
    assert task.completed is True
```

### **Teste da Classe `TaskManager`**

### **`tests/test_task_manager.py`**

```python
pythonCopiar código
import pytest
from task.task import Task
from task.task_manager import TaskManager
from task.user import User
from task.user_manager import UserManager

@pytest.fixture
def setup_task_manager():
    user_manager = UserManager()
    task_manager = TaskManager(user_manager)
    user = User(1, "John Doe")
    task = Task("Test Task", "This is a test task.")
    user_manager.add_user(user)
    task_manager.add_task(task)
    return task_manager, user_manager, user, task

def test_add_task(setup_task_manager):
    task_manager, _, _, _ = setup_task_manager
    assert len(task_manager.get_all_tasks()) == 1

def test_assign_task_to_user(setup_task_manager):
    task_manager, user_manager, user, task = setup_task_manager
    task_manager.assign_task_to_user(task.task_id, user.user_id)
    assert len(user.tasks) == 1
    assert user.tasks[0].task_id == task.task_id

def test_get_completed_tasks(setup_task_manager):
    task_manager, _, _, task = setup_task_manager
    task.mark_as_completed()
    completed_tasks = task_manager.get_completed_tasks()
    assert len(completed_tasks) == 1
    assert completed_tasks[0].task_id == task.task_id
```

### **Teste da Classe `User`**

### **`tests/test_user.py`**

```python
import pytest
from task.user import User
from task.task import Task

def test_user_creation():
    user = User(1, "John Doe")
    assert user.user_id == 1
    assert user.name == "John Doe"

def test_add_task():
    user = User(1, "John Doe")
    task = Task("Test Task", "This is a test task.")
    user.add_task(task)
    assert len(user.tasks) == 1
    assert user.tasks[0].task_id == task.task_id
```

### **Teste da Classe `UserManager`**

### **`tests/test_user_manager.py`**

```python
import pytest
from task.user_manager import UserManager
from task.user import User

def test_add_user():
    user_manager = UserManager()
    user = User(1, "John Doe")
    user_manager.add_user(user)
    assert len(user_manager.get_all_users()) == 1

def test_get_user():
    user_manager = UserManager()
    user = User(1, "John Doe")
    user_manager.add_user(user)
    retrieved_user = user_manager.get_user(1)
    assert retrieved_user.user_id == user.user_id
    assert retrieved_user.name == user.name
```

### **Executando o Projeto**

Para executar o projeto, caso esteja na pasta task_manager basta usar o app.py. Caso contrario é só entrar na pasta e executar o arquivo app.py:

```bash
cd task_manager
python app.py
```

### **Executando os Testes**

Para executar os testes, navegue até o diretório onde estão localizados os arquivos de teste (**`tests/`**) e execute o seguinte comando:

```bash
pytest
```

Isso vai descobrir e executar todos os testes no diretório **`tests/`**.

### **Conclusão**

Nesta documentação, cobrimos como usar o pytest para testar as classes **`Task`**, **`TaskManager`**, **`User`**, e **`UserManager`** na nossa aplicação de gerenciamento de tarefas. Os testes cobrem a criação de objetos, marcação de tarefas como completas, adição de tarefas a usuários, entre outros cenários. Certifique-se de executar os testes regularmente para garantir que a aplicação funcione conforme o esperado após as alterações no código.
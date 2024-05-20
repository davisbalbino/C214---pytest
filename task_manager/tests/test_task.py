# tests/test_task.py
from tasks.task import Task

def test_create_task():
    task = Task('Teste Task', 'Descrição')
    assert task.title == 'Teste Task'
    assert task.description == 'Descrição'
    assert not task.completed

def test_mark_task_as_completed():
    task = Task('Teste Task', 'Descrição')
    task.mark_as_completed()
    assert task.completed

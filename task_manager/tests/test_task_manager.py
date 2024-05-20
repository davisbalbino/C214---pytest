# tests/test_task_manager.py
from tasks.task import Task
from tasks.task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    task = Task('Teste Task', 'Descrição')
    manager.add_task(task)
    assert task in manager.get_all_tasks()

def test_remove_task():
    manager = TaskManager()
    task = Task('Teste Task', 'Descrição')
    manager.add_task(task)
    manager.remove_task(task)
    assert task not in manager.get_all_tasks()

def test_get_all_tasks():
    manager = TaskManager()
    task1 = Task('Teste  1', 'Task 1')
    task2 = Task('Teste  2', 'Task 2')
    manager.add_task(task1)
    manager.add_task(task2)
    assert manager.get_all_tasks() == [task1, task2]

def test_get_completed_tasks():
    manager = TaskManager()
    task1 = Task('Test Task 1', 'Task 1')
    task2 = Task('Test Task 2', 'Task 2')
    manager.add_task(task1)
    manager.add_task(task2)
    task1.mark_as_completed()
    assert manager.get_completed_tasks() == [task1]

def test_get_pending_tasks():
    manager = TaskManager()
    task1 = Task('Test Task 1', 'Task 1')
    task2 = Task('Test Task 2', 'Task 2')
    manager.add_task(task1)
    manager.add_task(task2)
    task1.mark_as_completed()
    assert manager.get_pending_tasks() == [task2]

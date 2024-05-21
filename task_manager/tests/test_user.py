# test_user.py

import pytest
from tasks.user_manager import UserManager
from tasks.user import User

@pytest.fixture
def mock_task(mocker):
    task = mocker.Mock()
    task.assign_to = mocker.Mock()
    return task

def test_user_creation():
    user = User(1, "Alice")
    assert user.user_id == 1
    assert user.name == "Alice"
    assert user.tasks == []
    
def test_add_task_to_user(mock_task, mocker):
    user = User(1, "Alice")
    user.add_task = mocker.Mock()
    
    mock_task.assign_to.side_effect = lambda user: user.add_task(mock_task)
    mock_task.assign_to(user)

    user.add_task.assert_called_once_with(mock_task)
    mock_task.assign_to.assert_called_once_with(user)

@pytest.mark.parametrize("completed", [True, False])
def test_mark_task_as_completed(mock_task, completed):
    mock_task.completed = completed
    assert mock_task.completed == completed


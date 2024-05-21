import pytest
from tasks.user import User
from tasks.user_manager import UserManager

def test_add_user():
    user_manager = UserManager()
    user = User(1, "Alice")
    user_manager.add_user(user)
    
    # Verifica se o usuário está na lista de usuários do user_manager
    assert any(u.user_id == 1 for u in user_manager.users)
    
    # Verifica se o usuário adicionado é exatamente o mesmo que foi inserido
    assert user_manager.get_user(1) == user

def test_add_existing_user():
    user_manager = UserManager()
    user = User(1, "Alice")
    user_manager.add_user(user)
    with pytest.raises(ValueError):
        user_manager.add_user(user)

def test_get_user():
    user_manager = UserManager()
    user = User(1, "Alice")
    user_manager.add_user(user)
    fetched_user = user_manager.get_user(1)
    assert fetched_user == user

def test_get_nonexistent_user():
    user_manager = UserManager()
    fetched_user = user_manager.get_user(1)
    assert fetched_user is None

def test_remove_user():
    user_manager = UserManager()
    user = User(1, "Alice")
    user_manager.add_user(user)
    user_manager.remove_user(1)
    assert 1 not in user_manager.users

def test_remove_nonexistent_user():
    user_manager = UserManager()
    with pytest.raises(ValueError):
        user_manager.remove_user(1)

# OpenRouter agent report

Model: cohere/north-mini-code:free

```python
import pytest
from todo import TodoList


def test_add_task_basic():
    todo = TodoList()
    task_id = todo.add_task("Buy milk")
    assert task_id == 1
    tasks = todo.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[0]["completed"] is False


def test_add_task_multiple_ids():
    todo = TodoList()
    id1 = todo.add_task("Task 1")
    id2 = todo.add_task("Task 2")
    assert id1 == 1
    assert id2 == 2
    tasks = todo.list_tasks()
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2


def test_add_task_title_is_stripped():
    todo = TodoList()
    task_id = todo.add_task("  Walk dog  ")
    tasks = todo.list_tasks()
    assert tasks[0]["title"] == "Walk dog"


def test_add_task_empty_title_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Title cannot be empty or whitespace"):
        todo.add_task("")
    with pytest.raises(ValueError, match="Title cannot be empty or whitespace"):
        todo.add_task("   ")


def test_add_task_duplicate_titles_allowed():
    todo = TodoList()
    todo.add_task("Repeat")
    todo.add_task("Repeat")
    tasks = todo.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Repeat"
    assert tasks[1]["title"] == "Repeat"


def test_complete_task_happy_path():
    todo = TodoList()
    todo.add_task("Task")
    todo.complete_task(1)
    tasks = todo.list_tasks()
    assert tasks[0]["completed"] is True


def test_complete_task_already_completed():
    todo = TodoList()
    todo.add_task("Task")
    todo.complete_task(1)
    todo.complete_task(1)  # second call should not raise
    tasks = todo.list_tasks()
    assert tasks[0]["completed"] is True


def test_complete_task_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task ID 99 not found"):
        todo.complete_task(99)


def test_remove_task_happy_path():
    todo = TodoList()
    todo.add_task("Task")
    todo.remove_task(1)
    tasks = todo.list_tasks()
    assert tasks == []


def test_remove_task_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task ID 42 not found"):
        todo.remove_task(42)


def test_list_tasks_includes_completed_and_pending():
    todo = TodoList()
    todo.add_task("Pending")
    todo.add_task("Done")
    todo.complete_task(1)
    tasks = todo.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["completed"] is True
    assert tasks[1]["completed"] is False


def test_list_tasks_shallow_copy():
    todo = TodoList()
    todo.add_task("Test")
    tasks = todo.list_tasks()
    # modify a returned task dict
    tasks[0]["completed"] = True
    # internal list should remain unchanged
    internal_tasks = todo.list_tasks()
    assert internal_tasks[0]["completed"] is False


def test_ids_not_reused_after_removal():
    todo = TodoList()
    id1 = todo.add_task("First")
    id2 = todo.add_task("Second")
    todo.remove_task(id1)
    id3 = todo.add_task("Third")
    assert id3 == 3  # IDs continue sequentially
    tasks = todo.list_tasks()
    assert [t["id"] for t in tasks] == [2, 3]


def test_add_task_returns_int():
    todo = TodoList()
    task_id = todo.add_task("Hello")
    assert isinstance(task_id, int)


# Non‑integer ID validation is the caller’s responsibility, so we do not test it here.
```

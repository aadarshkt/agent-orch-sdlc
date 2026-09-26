# OpenRouter agent report

Model: cohere/north-mini-code:free

# Goal
Implement a lightweight, in‑memory to‑do list manager that lets users add, complete, remove, and list tasks without any external dependencies.

## Functional Requirements
1. **Add a task** – `add_task(title)` stores a new task with a unique integer ID and returns the ID.  
2. **Complete a task** – `complete_task(task_id)` marks the task with the given ID as completed; raises `ValueError` if the ID does not exist.  
3. **Remove a task** – `remove_task(task_id)` deletes the task with the given ID; raises `ValueError` if the ID does not exist.  
4. **List tasks** – `list_tasks()` returns all tasks, including pending and completed, as a list of dictionaries with keys `id`, `title`, and `completed`.  
5. **Validation** – `add_task` must reject empty or whitespace‑only titles, raising `ValueError`.  
6. **Error handling** – Any unknown `task_id` supplied to `complete_task` or `remove_task` must raise `ValueError`.

## Public API
```python
from typing import List, Dict, Any

class TodoList:
    def add_task(self, title: str) -> int:
        """
        Add a new task with the given title.
        Returns the generated task ID.
        Raises ValueError if title is empty or whitespace.
        """
        ...

    def complete_task(self, task_id: int) -> None:
        """
        Mark the task with `task_id` as completed.
        Raises ValueError if `task_id` does not exist.
        """
        ...

    def remove_task(self, task_id: int) -> None:
        """
        Remove the task with `task_id`.
        Raises ValueError if `task_id` does not exist.
        """
        ...

    def list_tasks(self) -> List[Dict[str, Any]]:
        """
        Return a list of all tasks.
        Each task dict contains: id (int), title (str), completed (bool).
        """
        ...
```

## Edge Cases to Handle
- **Empty title** – `add_task("")` or `add_task("   ")` → raise `ValueError`.  
- **Duplicate titles** – allowed; no uniqueness constraint.  
- **Unknown task ID** – `complete_task` or `remove_task` with a non‑existent ID → raise `ValueError`.  
- **Non‑integer ID** – API expects `int`; type checking is the caller’s responsibility.  
- **Concurrent modifications** – not required; in‑memory storage is not thread‑safe.

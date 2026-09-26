from typing import List, Dict, Any

class TodoList:
    def __init__(self):
        self._tasks: List[Dict[str, Any]] = []
        self._next_id: int = 1

    def add_task(self, title: str) -> int:
        """
        Add a new task with the given title.
        Returns the generated task ID.
        Raises ValueError if title is empty or whitespace.
        """
        stripped = title.strip()
        if not stripped:
            raise ValueError("Title cannot be empty or whitespace.")
        task = {"id": self._next_id, "title": stripped, "completed": False}
        self._tasks.append(task)
        self._next_id += 1
        return task["id"]

    def complete_task(self, task_id: int) -> None:
        """
        Mark the task with `task_id` as completed.
        Raises ValueError if `task_id` does not exist.
        """
        for task in self._tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return
        raise ValueError(f"Task ID {task_id} not found.")

    def remove_task(self, task_id: int) -> None:
        """
        Remove the task with `task_id`.
        Raises ValueError if `task_id` does not exist.
        """
        for i, task in enumerate(self._tasks):
            if task["id"] == task_id:
                del self._tasks[i]
                return
        raise ValueError(f"Task ID {task_id} not found.")

    def list_tasks(self) -> List[Dict[str, Any]]:
        """
        Return a list of all tasks.
        Each task dict contains: id (int), title (str), completed (bool).
        """
        # Return a shallow copy to avoid external modifications.
        return [task.copy() for task in self._tasks]

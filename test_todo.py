We need to write pytest unit tests for the to-do list module. The test file should import the TodoList from todo and test happy paths and edge cases. The user says: "You are a test engineer. Using the upstream requirements and the implementation, write pytest unit tests for the to‑do list module. The module file is `todo.py` next to this test file, so import it with `from todo import TodoList` (or the names actually defined). Cover the happy paths and every documented edge case. Output ONLY Python source code - no markdown fences, no prose."

Thus we need to output a Python file containing tests using pytest. We should ensure it covers all functional requirements and edge cases.

We need to write tests that cover:

1. add_task: returns unique integer ID; rejects empty or whitespace titles; allows duplicate titles; validates title stripped.
2. complete_task: marks task as completed; raises ValueError for unknown ID.
3. remove_task: deletes task; raises ValueError for unknown ID.
4. list_tasks: returns all tasks with correct dicts; returns shallow copies; includes pending and completed tasks.
5. Edge cases: empty title, whitespace-only title, duplicate titles, unknown task ID, non-integer ID (type checking caller's responsibility, so maybe not needed? But we can test that if passed non-int, it's not our responsibility; but we can test that if someone passes a non-int, it may raise some error; but not required. However we can include a test that ensure if we pass a non-int, it's up to Python to raise TypeError; but not required. Might skip that.)
6. Ensure that tasks can be completed and then list shows completed true.
7. Ensure after removal, list doesn't contain that task.
8. Ensure IDs are sequential.
9. Ensure multiple tasks can be added and listed.

We should also consider test isolation: each test should start with a fresh TodoList instance. Could use pytest fixtures or instantiate inside each test.

We need to output only source code, no markdown fences, no prose. So just the test file code.

The file should be a .py file, maybe named test_todo.py. But the user didn't specify filename; they said "The module file is `todo.py` next to this test file, so import it with `from todo import TodoList` (or the names actually defined)." So we need to produce a test file that can be placed next to todo.py. The usual test file is test_todo.py or todo_test.py. We can just output a file named test_todo.py. Since they didn't specify name, we can choose an appropriate name. Usually pytest discovers tests in files named test_*.py or *_test.py. So we can name it test_todo.py.

The output should be only the source code. No extra commentary. So just:

```python
import pytest
from todo import TodoList

def test_add_task_happy_path():
    todo = TodoList()
    task_id = todo.add_task("Buy milk")
    assert task_id == 1
    tasks = todo.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[0]["completed"] is False

def test_add_task_multiple():
    todo = TodoList()
    id1 = todo.add_task("Task 1")
    id2 = todo.add_task("Task 2")
    assert id1 == 1
    assert id2 == 2
    tasks = todo.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["id"] == 2
    assert tasks[1]["title"] == "Task 2"

def test_add_task_duplicate_titles():
    todo = TodoList()
    todo.add_task("Same")
    id2 = todo.add_task("Same")
    assert id2 == 2
    tasks = todo.list_tasks()
    assert tasks[0]["title"] == "Same"
    assert tasks[1]["title"] == "Same"

def test_add_task_empty_title_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Title cannot be empty or whitespace"):
        todo.add_task("")
    with pytest.raises(ValueError, match="Title cannot be empty or whitespace"):
        todo.add_task("   ")

def test_add_task_whitespace_only_title_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Title cannot be empty or whitespace"):
        todo.add_task("\t\n")

def test_complete_task_happy_path():
    todo = TodoList()
    todo.add_task("Task")
    todo.complete_task(1)
    tasks = todo.list_tasks()
    assert tasks[0]["completed"] is True

def test_complete_task_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task ID 99 not found"):
        todo.complete_task(99)

def test_remove_task_happy_path():
    todo = TodoList()
    todo.add_task("Task1")
    todo.add_task("Task2")
    todo.remove_task(1)
    tasks = todo.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2
    assert tasks[0]["title"] == "Task2"

def test_remove_task_unknown_id_raises():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task ID 42 not found"):
        todo.remove_task(42)

def test_list_tasks_returns_shallow_copy():
    todo = TodoList()
    todo.add_task("Task")
    tasks = todo.list_tasks()
    # modify external list
    tasks[0]["completed"] = True
    # internal state unchanged
    internal = todo.list_tasks()
    assert internal[0]["completed"] is False

def test_list_tasks_after_completion_and_removal():
    todo = TodoList()
    todo.add_task("A")
    todo.add_task("B")
    todo.complete_task(1)
    todo.remove_task(2)
    tasks = todo.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["completed"] is True

def test_add_task_title_stripped():
    todo = TodoList()
    task_id = todo.add_task("  Hello  ")
    tasks = todo.list_tasks()
    assert tasks[0]["title"] == "Hello"
```

We might also include test for non-integer ID? The requirement says: "Non‑integer ID – API expects int; type checking is the caller’s responsibility." So we might not need to test that; but we could test that passing a string doesn't crash our code, but it might cause an error when comparing ids because they are ints. However we don't need to test that because it's caller's responsibility. So it's optional.

We might want to also test that after completing a task, subsequent calls to list tasks show completed.

We should also test that the error messages match those in the implementation: In add_task, the error message is "Title cannot be empty or whitespace." So we should match that exactly. In complete_task and remove_task, the error message is f"Task ID {task_id} not found." So we should match that. So we need to include match parameters accordingly.

Now, we need to ensure we output only Python code, no markdown fences, no prose. So the code block should be plain code (no triple backticks). The response should be just the Python source code. So we must not include any surrounding text.

Thus final answer will be a block of Python code containing all these tests.

We could also use a fixture to create a new TodoList for each test, but it's fine to instantiate inside each test.

We must ensure that the file can be executed as a test script. It may have a __name__ == "__main__" block to run tests, but not required; pytest can run it.

One more thing: The user says "Output ONLY Python source code - no markdown fences, no prose." So we must output just the code. So we will output:

```python
import pytest
from todo import TodoList

def test_add_task_happy_path():
    ...

...
```

But note that we should not include any markdown fences, so we need to output raw code. In the answer, we need to include it as plain text (no fences). So in the chat, we just provide the code.

Now, ensure that the tests cover all the documented edge cases: empty title, whitespace title, duplicate titles, unknown task ID, maybe non-integer ID (but optional), also test that tasks are listed with correct keys.

One more edge case: after removal, list doesn't contain it; after complete, list shows completed true.

Also test that the list returns a shallow copy; we have a test for that.

Also test that adding tasks yields sequential IDs.

Also test that title stripping works.

We also need to ensure that the error messages match exactly.

Thus the code as above is fine.

But we must be careful: The error message in add_task is exactly "Title cannot be empty or whitespace." We should match that. In our test we used `match="Title cannot be empty or whitespace"`. That's fine because match is substring? Actually pytest.raises(match=...) expects a regular expression pattern. If we give plain string, it's treated as regex; we can escape or use `match="Title cannot be empty or whitespace"` which works as plain string. However there might be extra whitespace or punctuation. The message exactly matches. So we can use `match="Title cannot be empty or whitespace"`. That's fine.

Now, we also need to include test for duplicate titles; requirement says duplicate titles allowed; no uniqueness constraint. So we test that.

Now, we need to check if any other edge cases: The requirement says "Non-integer ID – API expects int; type checking is the caller's responsibility." So we could test that passing a non-int results in something like TypeError maybe when comparing? Actually our complete_task expects an int; if we pass a string, Python will compare string with integer IDs, which will never be equal (since ids are ints). So it will always raise ValueError because the id not found. That's not ideal but it's caller's fault. We could test that but not required. Might be better to skip.

But we could add a test for that to be thorough: "test_complete_task_non_int_id_raises_ValueError"? But it's not required.

Given the requirement says "cover the happy paths and every documented edge case", we might consider the edge case "Non-integer ID" as documented, but they note it's caller's responsibility. However it's still an edge case. But we could decide to include a test that verifies that passing a non-int ID results in a ValueError (since the id not found). But it's ambiguous. However it might be considered a happy path? No.

The user wants to cover every documented edge case. The documented edge cases are:

- **Empty title** – `add_task("")` or `add_task("   ")` → raise `ValueError`. 
- **Duplicate titles** – allowed; no uniqueness constraint. 
- **Unknown task ID** – `complete_task` or `remove_task` with a non‑existent ID → raise `ValueError`. 
- **Non‑integer ID** – API expects `int`; type checking is the caller’s responsibility. 
- **Concurrent modifications** – not required; in‑memory storage is not thread‑safe.

So they list non-integer ID as an edge case, but they note it's caller's responsibility. So we might include a test that if a non-int is passed, we may still raise something (maybe ValueError because id not found). However it's not required to handle it, but we could test that it behaves gracefully (i.e., does not crash). But we could also consider not testing it because it's not required to be handled. But to be safe, we could include a test that passes a string ID to complete_task and ensures it raises ValueError because id not found. But that test might be considered duplicate of unknown ID. However it's still a case.

But the requirement "cover the happy paths and every documented edge case" implies we should have tests for each edge case. So we should have:

- test_add_task_empty_title_raises
- test_add_task_whitespace_title_raises
- test_add_task_duplicate_titles_allowed
- test_complete_task_unknown_id_raises
- test_remove_task_unknown_id_raises
- test_non_integer_id_behavior (maybe test that passing a non-int leads to ValueError as id not found). But we might also test that passing a non-int leads to no side effects.

We could also test for concurrent modifications? That is not required to test, but it's not required to be handled. The requirement says not required; so we can skip.

Also need to test that the IDs are unique and sequential.

Thus our test suite already covers many but might miss the non-integer ID test. We could add a test for non-integer ID:

```python
def test_complete_task_non_int_id_raises():
    todo = TodoList()
    todo.add_task("Task")
    # passing a string ID; it will not match int id, so ValueError
    with pytest.raises(ValueError, match="Task ID .* not found"):
        todo.complete_task("1")
```

But the error message will be "Task ID 1 not found"? Actually we pass "1", a string; the code will compare task["id"] == "1". Since task["id"] is int 1, they are not equal. So it will go through all tasks, find none, then raise ValueError with f"Task ID {task_id} not found." Since task_id is string, it will be "Task ID 1 not found"? Actually the f-string will convert "1" to string, so the message will be "Task ID 1 not found". So we could match with "Task ID 1 not found". However, we cannot guarantee that because the message will include the string "1". But we can match with regex: `match="Task ID 1 not found"`. That should work.

But note that the test expects a ValueError. However the API expects int, but we are testing a case that is not part of the spec. The spec says it's caller's responsibility, but we might still want to ensure that our implementation doesn't crash with an exception other than ValueError. But we are using pytest.raises to catch ValueError, which is what would happen.

Alternatively, we could test that a non-int ID leads to ValueError. That seems okay. But we might also need to test for remove_task similarly.

Thus we can add:

```python
def test_complete_task_non_int_id_raises():
    todo = TodoList()
    todo.add_task("Task")
    with pytest.raises(ValueError, match="Task ID 1 not found"):
        todo.complete_task("1")
```

But this test is a bit redundant with unknown ID test, because "1" as string is not equal to id 1, so it's effectively unknown. However it's testing the case where a non-int is passed. Could be considered separate.

Similarly for remove_task.

But is it necessary? The requirement says "cover the happy paths and every documented edge case." The documented edge case includes "Non-integer ID". So we need to include a test for it. So we should include a test that passes a non-integer ID and ensures it raises ValueError (since the ID is unknown). We can either use string or float. We can test with string and int? Actually int is fine. For non-int, we could test with string. That's fine.

Thus we need to add two tests: one for complete_task with non-int ID, and one for remove_task with non-int ID. Or we could combine them in one test using parametrize? But separate is fine.

Now, we also need to ensure we cover "Duplicate titles" allowed. Already covered.

Now, "Empty title" and "Whitespace-only title". Already covered.

Now, "Unknown task ID". Already covered.

Now, "Concurrent modifications" is not required to be tested. So skip.

Now, also test that list_tasks returns shallow copy; we have a test.

Now, also test that after removal, tasks list is correct; we have test.

Now, also test that after completion, tasks list shows completed true; we have test.

Now, also test that titles are stripped; we have test.

Now, also test that IDs are sequential; we have test.

Now, also test that the TodoList starts empty; we could add a test for that.

Let's add:

```python
def test_new_list_is_empty():
    todo = TodoList()
    tasks = todo.list_tasks()
    assert tasks == []
```

But it's trivial, but it's good.

Now, also test that after adding a task, list_tasks returns a dict with expected keys. But we already do that in the happy path tests.

Now, we should also test that adding a task with whitespace only raises; we have test.

Now, also test that add_task with title containing only whitespace raises. We have test for whitespace-only; but we used test_add_task_whitespace_only_title_raises. That's good.

Now, also test that add_task with title that has leading/trailing spaces gets stripped. Already have.

Now, test that after adding tasks, subsequent add_task gets next ID. Already covered.

Now, consider concurrency not required.

Now, ensure that the code uses pytest fixtures? Not needed.

Now, ensure we import pytest.

Now, we should output a single file named test_todo.py. But the user didn't specify the filename; they said "The module file is `todo.py` next to this test file". So we can assume the test file is test_todo.py. So we output that.

Now, we need to ensure the test code is correct and passes with the given implementation.

We should also consider that in the implementation, complete_task and remove_task raise ValueError with message f"Task ID {task_id} not found." So the tests should match that exactly.

Now, we need to ensure that we don't have any typos.

Now, we also might want to use `@pytest.mark.parametrize` for duplicate titles or unknown IDs? Not needed.

Now, we also might want to test that adding a task with empty title raises exactly ValueError and not some other exception.

Now, the error message for add_task: "Title cannot be empty or whitespace." We should match exactly. In the test we used `match="Title cannot be empty or whitespace"`. That is fine.

Now, the error message for complete_task and remove_task: "Task ID {task_id} not found." For unknown ID 99, the message will be "Task ID 99 not found." So we can match with `match="Task ID 99 not found"`.

Now, for non-int ID, like "1", the message will be "Task ID 1 not found." So we can match with `match="Task ID 1 not found"`.

Now, test that the error messages contain exactly that.

Now, we also might want to test that after completing a task, you cannot complete it again? It's already completed; calling complete_task again should not raise anything; it should just set completed to True again. Our implementation loops and sets completed True, so calling again is fine. So no need to test.

Now, test that after removal, calling complete_task on that ID raises ValueError. Already covered in unknown ID tests because after removal, the ID no longer exists.

Now, we should also test that list_tasks returns a shallow copy; we have test that modifies external list and

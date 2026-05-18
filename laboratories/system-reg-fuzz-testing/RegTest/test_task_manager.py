# test_task_manager.py
import pytest
from task_manager import TaskManager

def test_add_and_list_tasks(regtest):
    """
    1. Creează o instanță a clasei TaskManager.
    2. Adaugă două taskuri
    3. Obține lista taskurilor cu metoda list_tasks().
    4. Scrie rezultatul în regtest (folosind regtest.write()).
    """
    taskManager = TaskManager()
    taskManager.add_task("something")
    taskManager.add_task("something else")

    tasks = taskManager.list_tasks()

    regtest.write(str(tasks))


def test_mark_done_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Marchează acest task ca finalizat (index 0).
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda mark_done(index).
    """
    tskMan = TaskManager()
    tskMan.add_task("some task?")
    tskMan.mark_done(0)
    tasks = tskMan.list_tasks()

    regtest.write(str(tasks))

def test_delete_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă două taskuri
    3. Șterge primul task (index 0).
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda delete_task(index).
    """
    taskManager = TaskManager()
    taskManager.add_task("something")
    taskManager.add_task("something else?")
    taskManager.delete_task(0)
    tasks = taskManager.list_tasks()

    regtest.write(str(tasks))


def test_edit_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Editează descrierea acestui task cu o descriere nouă
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda edit_task(index, noua_descriere).
    """
    taskManager = TaskManager()
    taskManager.add_task("some task")
    taskManager.edit_task(0, "new description")

    tasks = taskManager.list_tasks()

    regtest.write(str(tasks))

def test_combination_operations(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă două taskuri
    3. Marchează al doilea task ca finalizat.
    4. Editează primul task cu o descriere nouă
    5. Șterge al doilea task.
    6. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: combină metodele add_task, mark_done, edit_task, delete_task.
    """
    taskManager = TaskManager()
    taskManager.add_task("something")
    taskManager.add_task("another task")

    taskManager.mark_done(1)
    taskManager.edit_task(0, "new description")

    taskManager.delete_task(1)
    tasks = taskManager.list_tasks()

    regtest.write(str(tasks))


def test_invalid_index_mark_done(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să marchezi ca finalizat un index invalid
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: folosește try-except și str(e) ca să obții mesajul excepției.
    """
    taskManager = TaskManager()
    taskManager.add_task("some other task")
    try:
        taskManager.mark_done(2)
    except IndexError as e:
        regtest.write(str(e))

def test_invalid_index_delete(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să ștergi un task cu index invalid (ex: index -1).
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: la fel ca la test_invalid_index_mark_done.
    """
    taskManager = TaskManager()
    taskManager.add_task("some task")
    try:
        taskManager.delete_task(-1)
    except IndexError as e:
        regtest.write(str(e))

def test_invalid_index_edit(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să editezi un index invalid (ex: index 2) cu o descriere nouă.
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: folosește try-except și scrie mesajul excepției.
    """
    taskManager = TaskManager()
    taskManager.add_task("task")
    try:
        taskManager.edit_task(2,"new description")
    except IndexError as e:
        regtest.write(str(e))

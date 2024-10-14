import unittest
from unittest.mock import patch
from src.todo_list import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertIn("Buy groceries", self.todo_list.tasks)
        self.assertFalse(self.todo_list.tasks["Buy groceries"])

    @patch('builtins.print')
    def test_add_duplicate_task(self, mock_print):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Buy groceries")
        mock_print.assert_called_with("Task 'Buy groceries' already exists.")

    def test_remove_task(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.remove_task("Buy groceries")
        self.assertNotIn("Buy groceries", self.todo_list.tasks)

    @patch('builtins.print')
    def test_remove_non_existent_task(self, mock_print):
        self.todo_list.remove_task("Go for a walk")
        mock_print.assert_called_with("Task 'Go for a walk' does not exist.")

    def test_complete_task(self):
        self.todo_list.add_task("Read a book")
        self.todo_list.complete_task("Read a book")
        self.assertTrue(self.todo_list.tasks["Read a book"])

    @patch('builtins.print')
    def test_complete_non_existent_task(self, mock_print):
        self.todo_list.complete_task("Go for a walk")
        mock_print.assert_called_with("Task 'Go for a walk' does not exist.")

    def test_get_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Read a book")
        tasks = self.todo_list.get_tasks()
        expected_tasks = [
            {'task': 'Buy groceries', 'completed': False},
            {'task': 'Read a book', 'completed': False}
        ]
        self.assertEqual(tasks, expected_tasks)

if __name__ == '__main__':
    unittest.main()
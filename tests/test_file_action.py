from tests.test_helper import *
from unittest.mock import patch
from actions.file_action import create_file, delete_file, modify_file

class TestFileAction(unittest.TestCase):

    @patch('actions.file_action.log_activity')
    @patch('builtins.input', side_effect=['testfile', '.txt'])
    def test_create_file(self, mock_input, mock_log_activity):
        create_file()
        mock_log_activity.assert_called_once_with(
            "file_create",
            {
                "filepath": "user_created_files/testfile.txt",
                "file_type": ".txt"
            }
        )

    @patch('actions.file_action.log_activity')
    @patch('actions.file_action.list_user_files', return_value=["testfile.txt"])
    @patch('builtins.input', side_effect=['testfile.txt', 'appended content'])
    def test_modify_file(self, mock_input, mock_list_files, mock_log_activity):
        modify_file()
        mock_log_activity.assert_called_once_with(
            "file_modify",
            {
                "filepath": "user_created_files/testfile.txt",
                "content_appended": "appended content"
            }
        )

    @patch('actions.file_action.log_activity')
    @patch('actions.file_action.list_user_files', return_value=["testfile.txt"])
    @patch('builtins.input', side_effect=['testfile.txt'])
    def test_delete_file(self, mock_list_files, mock_input, mock_log_activity):
        with patch('os.remove') as mock_remove:
            delete_file()
            mock_remove.assert_called_once_with("user_created_files/testfile.txt")
            mock_log_activity.assert_called_once_with(
                "file_delete",
                {"filepath": "user_created_files/testfile.txt"}
            )

if __name__ == '__main__':
    unittest.main()

from tests.test_helper import *
from unittest.mock import patch, MagicMock
from actions.process_action import handle_process_action

class TestProcessAction(unittest.TestCase):
    @patch('actions.process_action.subprocess.Popen')
    @patch('actions.process_action.log_activity')
    def test_process_create(self, mock_log_activity, mock_popen):
        mock_process = MagicMock()
        mock_process.pid = 12345
        mock_popen.return_value = mock_process

        with patch('builtins.input', side_effect=['echo Hello']):
            handle_process_action()
        
        mock_popen.assert_called_once_with('echo Hello', shell=True)

        mock_log_activity.assert_called_once_with(
            "process_start",
            {
                "command": "echo Hello",
                "process_id": 12345,
                "process_name": "echo"
            }
        )

if __name__ == '__main__':
    unittest.main()

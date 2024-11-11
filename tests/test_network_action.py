from tests.test_helper import *
from unittest.mock import patch, MagicMock
from actions.network_action import handle_network_action

class TestNetworkAction(unittest.TestCase):

    @patch('actions.network_action.log_activity')
    @patch('actions.network_action.subprocess.run')
    @patch('builtins.input', side_effect=['http://example.com', '80', 'POST', 'data=example'])
    @patch('socket.gethostbyname', return_value='127.0.0.1')
    def test_network_action_post(self, mock_socket, mock_input, mock_subprocess, mock_log_activity):
        mock_result = MagicMock()
        mock_result.stdout = "HTTP/1.1 200 OK\n"
        mock_subprocess.return_value = mock_result

        handle_network_action()

        mock_subprocess.assert_called_once_with(
            ['curl', '-i', 'http://example.com:80', '-d', 'data=example'],
            capture_output=True, text=True, check=True
        )

        mock_log_activity.assert_called_once_with(
            "network_request",
            {
                "request_type": "POST",
                "destination_address": "http://example.com",
                "destination_port": "80",
                "protocol": "POST",
                "data_sent": "data=example",
                "amount_of_data_sent": len("data=example"),
                "source_address": '127.0.0.1',
                "process_name": "curl",
                "process_id": unittest.mock.ANY
            }
        )

    @patch('actions.network_action.log_activity')
    @patch('actions.network_action.subprocess.run')
    @patch('builtins.input', side_effect=['http://example.com', '80', 'GET'])
    @patch('socket.gethostbyname', return_value='127.0.0.1')
    def test_network_action_get(self, mock_socket, mock_input, mock_subprocess, mock_log_activity):
        mock_result = MagicMock()
        mock_result.stdout = "HTTP/1.1 200 OK\n"
        mock_subprocess.return_value = mock_result

        handle_network_action()

        mock_subprocess.assert_called_once_with(
            ['curl', '-i', 'http://example.com:80'],
            capture_output=True, text=True, check=True
        )

        mock_log_activity.assert_called_once_with(
            "network_request",
            {
                "request_type": "GET",
                "destination_address": "http://example.com",
                "destination_port": "80",
                "protocol": "GET",
                "data_sent": "N/A",
                "amount_of_data_sent": 0,
                "source_address": '127.0.0.1',
                "process_name": "curl",
                "process_id": unittest.mock.ANY
            }
        )

if __name__ == '__main__':
    unittest.main()

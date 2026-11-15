import os
from pathlib import Path
import subprocess
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend import (Server, classify_server_line, find_server, list_endpoints, local_address,
                     parse_endpoints, server_args)


class BackendTests(unittest.TestCase):
    def test_capture_readiness_is_not_socket_readiness(self):
        self.assertEqual(classify_server_line('[info] server started'), 'listening')
        self.assertEqual(classify_server_line('[info] tcp listen success'), 'log')
        self.assertEqual(classify_server_line('[info] audio capture ready'), 'ready')
        self.assertEqual(classify_server_line('[error] PipeWire capture failed: device lost'), 'capture_error')
        self.assertEqual(classify_server_line('No PipeWire audio sinks found'), 'error')

    def test_endpoints(self):
        output = ('[info] PipeWire\nendpoint list:\n'
                  '\t* id: 1234 name: Speakers (HDMI)\n'
                  '\t  id: 55   name: Audio Share Sink\ntotal: 2\n')
        self.assertEqual(parse_endpoints(output),
                         [('1234', 'Speakers (HDMI)', True),
                          ('55', 'Audio Share Sink', False)])

    def test_args(self):
        self.assertEqual(server_args('as-cmd', ' 192.168.1.4 ', '65530', '42'),
                         ['as-cmd', '--bind=192.168.1.4:65530', '--endpoint=42'])
        for host, port in [('127.0.0.1', 123), ('0.0.0.0', 123),
                           ('not a host', 123), ('192.168.1.2', '65536'),
                           ('192.168.1.2', '12junk'), ('192.168.1.2', 0)]:
            with self.subTest(host=host, port=port), self.assertRaises(ValueError):
                server_args('as-cmd', host, port, 'default')

    def test_local_address(self):
        result = subprocess.CompletedProcess([], 0, '[{"link_type":"loopback","addr_info":[{"family":"inet","local":"127.0.0.1"}]},{"link_type":"ether","addr_info":[{"family":"inet","local":"192.168.2.3"}]}]')
        with patch('backend.subprocess.run', return_value=result):
            self.assertEqual(local_address(), '192.168.2.3')
        with patch('backend.subprocess.run', side_effect=FileNotFoundError):
            self.assertEqual(local_address(), '')

    def test_binary_override(self):
        with patch.dict(os.environ, {'AUDIO_SHARE_SERVER': '/missing/as-cmd'}):
            with self.assertRaises(FileNotFoundError):
                find_server()

    def test_endpoint_error(self):
        with patch('backend.subprocess.run', return_value=subprocess.CompletedProcess([], 1, '', 'PipeWire unavailable')):
            with self.assertRaisesRegex(RuntimeError, 'PipeWire unavailable'):
                list_endpoints('as-cmd')

    def test_process_lifecycle(self):
        done = threading.Event()
        lines = []
        exits = []
        server = Server(lines.append, lambda code: (exits.append(code), done.set()))
        server.start([sys.executable, '-u', '-c',
                      'import time; print("server started"); time.sleep(30)'])
        with self.assertRaises(RuntimeError):
            server.start([sys.executable])
        server.stop()
        self.assertTrue(done.wait(5))
        self.assertIsNone(server.process)
        self.assertNotEqual(exits[0], 0)


if __name__ == '__main__':
    unittest.main()

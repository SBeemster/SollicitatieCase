import unittest
import server

class MockSocket():
    
    def __init__(self):
        self.open = True
        self.closed = False
        self.message = None

    async def send(self, message):
        self.message = message
        self.open = False
        pass

    async def close(self):
        self.closed = True
        pass


class TestWebSocket(unittest.IsolatedAsyncioTestCase):

    async def test_message_received(self):
        mockSocket = MockSocket()
        await server.population(mockSocket, "mockPath")
        
        self.assertIsNotNone(mockSocket.message)

    async def test_message_greater(self):
        mockSocket = MockSocket()
        await server.population(mockSocket, "mockPath")
        
        self.assertGreater(int(mockSocket.message), server.pop_start)

    async def test_message_equal(self):
        mockSocket = MockSocket()
        await server.population(mockSocket, "mockPath")
        
        self.assertEqual(int(mockSocket.message), server.pop_now)

    async def test_connection_closed(self):
        mockSocket = MockSocket()
        await server.population(mockSocket, "mockPath")

        self.assertEqual(mockSocket.closed, True)

if __name__ == '__main__':
    unittest.main()
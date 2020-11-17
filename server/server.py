import asyncio
import websockets
from datetime import datetime


# Server properties
port = 5678
host = "127.0.0.1"
# Population properties
birth_timeout = 386
time_start = round(datetime.strptime("01/01/2020", "%d/%m/%Y").timestamp() * 1000)
time_now = round(datetime.now().timestamp() * 1000)
pop_start = 7794799021
pop_now = round(pop_start + ((time_now - time_start) / birth_timeout))


async def population(websocket, path):
    global pop_now
    while websocket.open:
        pop_now += 1
        await websocket.send(str(pop_now))
        await asyncio.sleep(birth_timeout / 1000)
    await websocket.close()


if __name__ == "__main__":
    try:
        print(f"Starting server at ws://{host}:{port}/")
        start_server = websockets.serve(population, host, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        asyncio.get_event_loop().stop()
        print ("Stopped server")

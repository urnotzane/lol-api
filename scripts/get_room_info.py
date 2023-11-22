# 获取房间所有数据，仅在客户端用户已创建房间后可使用
import asyncio
import willump
import json

async def get_room_info():
    data = await (await wllp.request('GET', '/lol-lobby/v2/lobby')).json()
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False))


async def main():
    global wllp
    wllp = await willump.start()
    await get_room_info()
    await wllp.close()

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()


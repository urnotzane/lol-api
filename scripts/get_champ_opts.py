# 获取可选英雄
import asyncio
import willump
import json

async def get_champ_opts():
    data = await (await wllp.request('GET', '/lol-champ-select/v1/pickable-champion-ids')).json()
    text = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    print(text, ensure_ascii=False)


async def main():
    global wllp
    wllp = await willump.start()
    await get_champ_opts()
    await wllp.close()

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()


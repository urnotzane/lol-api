# 根据 queueId 创建常规房间
# 参数和房间数据：https://github.com/XHXIAIEIN/LeagueCustomLobby#queue-maps-game-modes-game-types
async def createLobby(connection):
  queue = {'queueId': 420}
  await connection.request('POST', '/lol-lobby/v2/lobby', data=queue)
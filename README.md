# LOL API

## 获取所有API数据
Swagger
你可以使用 Swagger 并导入 API 列表，得到所有客户端的通信接口，这样会非常方便调试。

_Swagger v2 _

https://127.0.0.1:2999/swagger/v2/swagger.json
OpenAPI v3

https://127.0.0.1:2999/swagger/v3/openapi.json

## 查询房间信息
### /lol-lobby/v2/lobby
房间界面、禁用阶段、配置天赋阶段返回数据是一样的
## 禁用英雄
### /lol-player-behavior/v1/ban
```json
{
    "errorCode": "RPC_ERROR",
    "httpStatus": 404,
    "implementationDetails": {},
    "message": "Not found"
}
```
### /lol-champ-select/v1/session/timer
获取英雄BP阶段的一些数据

### /lol-champ-select/v1/session
获取BP阶段详细数据
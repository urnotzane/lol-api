# LOL API

> https://apipheny.io/riot-games-api/
> https://riot-api-libraries.readthedocs.io/en/latest/index.html

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

一个完整的2v2对局BP数据
```json
{
    "actions": [
        [
            {
                "actorCellId": 1,
                "championId": 96,
                "completed": true,
                "id": 1,
                "isAllyAction": true,
                "isInProgress": false,
                "pickTurn": 1,
                "type": "pick"
            },
            {
                "actorCellId": 2,
                "championId": 30,
                "completed": true,
                "id": 2,
                "isAllyAction": false,
                "isInProgress": false,
                "pickTurn": 1,
                "type": "pick"
            },
            {
                "actorCellId": 3,
                "championId": 62,
                "completed": true,
                "id": 3,
                "isAllyAction": false,
                "isInProgress": false,
                "pickTurn": 1,
                "type": "pick"
            },
            {
                "actorCellId": 0,
                "championId": 113,
                "completed": true,
                "id": 4,
                "isAllyAction": true,
                "isInProgress": false,
                "pickTurn": 1,
                "type": "ban"
            }
        ],
        [
            {
                "actorCellId": 0,
                "championId": 523,
                "completed": true,
                "id": 5,
                "isAllyAction": true,
                "isInProgress": false,
                "pickTurn": 3,
                "type": "ban"
            }
        ],
        [
            {
                "actorCellId": 0,
                "championId": 133,
                "completed": true,
                "id": 6,
                "isAllyAction": true,
                "isInProgress": false,
                "pickTurn": 5,
                "type": "ban"
            }
        ],
        [
            {
                "actorCellId": 0,
                "championId": 16,
                "completed": true,
                "id": 7,
                "isAllyAction": true,
                "isInProgress": false,
                "pickTurn": 1,
                "type": "pick"
            }
        ]
    ],
    "allowBattleBoost": false,
    "allowDuplicatePicks": false,
    "allowLockedEvents": false,
    "allowRerolling": false,
    "allowSkinSelection": true,
    "bans": {
        "myTeamBans": [
            113,
            523,
            133
        ],
        "numBans": 6,
        "theirTeamBans": []
    },
    "benchChampions": [],
    "benchEnabled": false,
    "boostableSkinCount": 1,
    "chatDetails": {
        "mucJwtDto": {
            "channelClaim": "",
            "domain": "",
            "jwt": "",
            "targetRegion": ""
        },
        "multiUserChatId": "c1~f8bd76991373b09604c4b3143f62900d299521de",
        "multiUserChatPassword": "J5sHbPT3fO6P9KhB"
    },
    "counter": -1,
    "gameId": 0,
    "hasSimultaneousBans": false,
    "hasSimultaneousPicks": false,
    "isCustomGame": true,
    "isSpectating": false,
    "localPlayerCellId": 0,
    "lockedEventIndex": -1,
    "myTeam": [
        {
            "assignedPosition": "",
            "cellId": 0,
            "championId": 16,
            "championPickIntent": 0,
            "nameVisibilityType": "",
            "obfuscatedPuuid": "",
            "obfuscatedSummonerId": 0,
            "puuid": "93f8c8b2-dcba-5635-b2a2-d775a0ed3c82",
            "selectedSkinId": 16000,
            "spell1Id": 6,
            "spell2Id": 7,
            "summonerId": 3374773814903104,
            "team": 1,
            "wardSkinId": -1
        },
        {
            "assignedPosition": "",
            "cellId": 1,
            "championId": 96,
            "championPickIntent": 0,
            "nameVisibilityType": "",
            "obfuscatedPuuid": "",
            "obfuscatedSummonerId": 0,
            "puuid": "",
            "selectedSkinId": 96000,
            "spell1Id": 18446744073709552000,
            "spell2Id": 18446744073709552000,
            "summonerId": 0,
            "team": 1,
            "wardSkinId": -1
        }
    ],
    "pickOrderSwaps": [],
    "recoveryCounter": 0,
    "rerollsRemaining": 0,
    "skipChampionSelect": false,
    "theirTeam": [
        {
            "assignedPosition": "",
            "cellId": 2,
            "championId": 30,
            "championPickIntent": 0,
            "nameVisibilityType": "",
            "obfuscatedPuuid": "",
            "obfuscatedSummonerId": 0,
            "puuid": "",
            "selectedSkinId": 30000,
            "spell1Id": 0,
            "spell2Id": 0,
            "summonerId": 0,
            "team": 2,
            "wardSkinId": -1
        },
        {
            "assignedPosition": "",
            "cellId": 3,
            "championId": 62,
            "championPickIntent": 0,
            "nameVisibilityType": "",
            "obfuscatedPuuid": "",
            "obfuscatedSummonerId": 0,
            "puuid": "",
            "selectedSkinId": 62000,
            "spell1Id": 0,
            "spell2Id": 0,
            "summonerId": 0,
            "team": 2,
            "wardSkinId": -1
        }
    ],
    "timer": {
        "adjustedTimeLeftInPhase": 0,
        "internalNowInEpochMs": 1700805810178,
        "isInfinite": false,
        "phase": "GAME_STARTING",
        "totalTimeInPhase": 0
    },
    "trades": [
        {
            "cellId": 1,
            "id": 101,
            "state": "INVALID"
        }
    ]
}
```

### /lol-gameflow/v1/session
获取游戏对局数据
```json
{
    "gameClient": {
        "observerServerIp": "119.147.190.85",
        "observerServerPort": 8088,
        "running": true,
        "serverIp": "183.60.85.125",
        "serverPort": 5390,
        "visible": false
    },
    "gameData": {
        "gameId": 8523954631,
        "gameName": "",
        "isCustomGame": true,
        "password": "",
        "playerChampionSelections": [
            {
                "championId": 16,
                "selectedSkinIndex": 0,
                "spell1Id": 6,
                "spell2Id": 7,
                "summonerInternalName": "摸鱼达人王"
            }
        ],
        "queue": {
            "allowablePremadeSizes": [],
            "areFreeChampionsAllowed": true,
            "assetMutator": "",
            "category": "Custom",
            "championsRequiredToPlay": 0,
            "description": "",
            "detailedDescription": "",
            "gameMode": "CLASSIC",
            "gameTypeConfig": {
                "advancedLearningQuests": false,
                "allowTrades": true,
                "banMode": "StandardBanStrategy",
                "banTimerDuration": 38,
                "battleBoost": false,
                "crossTeamChampionPool": false,
                "deathMatch": false,
                "doNotRemove": false,
                "duplicatePick": false,
                "exclusivePick": true,
                "id": 2,
                "learningQuests": false,
                "mainPickTimerDuration": 43,
                "maxAllowableBans": 6,
                "name": "GAME_CFG_DRAFT_STD",
                "onboardCoopBeginner": false,
                "pickMode": "DraftModeSinglePickStrategy",
                "postPickTimerDuration": 33,
                "reroll": false,
                "teamChampionPool": false
            },
            "id": -1,
            "isRanked": false,
            "isTeamBuilderManaged": false,
            "lastToggledOffTime": 0,
            "lastToggledOnTime": 0,
            "mapId": 11,
            "maximumParticipantListSize": 5,
            "minLevel": 0,
            "minimumParticipantListSize": 0,
            "name": "",
            "numPlayersPerTeam": 5,
            "queueAvailability": "Available",
            "queueRewards": {
                "isChampionPointsEnabled": false,
                "isIpEnabled": false,
                "isXpEnabled": false,
                "partySizeIpRewards": []
            },
            "removalFromGameAllowed": false,
            "removalFromGameDelayMinutes": 0,
            "shortName": "",
            "showPositionSelector": false,
            "spectatorEnabled": false,
            "type": "PRACTICE_GAME"
        },
        "spectatorsAllowed": false,
        "teamOne": [
            {
                "championId": 96,
                "lastSelectedSkinIndex": 0,
                "profileIconId": 0,
                "teamOwner": false,
                "teamParticipantId": 0
            },
            {
                "championId": 16,
                "lastSelectedSkinIndex": 0,
                "profileIconId": 25,
                "puuid": "93f8c8b2-dcba-5635-b2a2-d775a0ed3c82",
                "summonerId": 3374773814903104,
                "summonerInternalName": "摸鱼达人王",
                "summonerName": "摸鱼达人王",
                "teamOwner": false,
                "teamParticipantId": 1
            }
        ],
        "teamTwo": [
            {
                "championId": 30,
                "lastSelectedSkinIndex": 0,
                "profileIconId": 0,
                "teamOwner": false,
                "teamParticipantId": 0
            },
            {
                "championId": 62,
                "lastSelectedSkinIndex": 0,
                "profileIconId": 0,
                "teamOwner": false,
                "teamParticipantId": 0
            }
        ]
    },
    "gameDodge": {
        "dodgeIds": [],
        "phase": "None",
        "state": "Invalid"
    },
    "map": {
        "assets": {
            "champ-select-background-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Shared/sound/music-cs-blindpick-default.ogg",
            "champ-select-flyout-background": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/champ-select-flyout-background.jpg",
            "champ-select-planning-intro": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/champ-select-planning-intro.jpg",
            "game-select-icon-active": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/game-select-icon-active.png",
            "game-select-icon-active-video": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/video/game-select-icon-active.webm",
            "game-select-icon-default": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/game-select-icon-default.png",
            "game-select-icon-disabled": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/game-select-icon-disabled.png",
            "game-select-icon-hover": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/game-select-icon-hover.png",
            "game-select-icon-intro-video": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/video/game-select-icon-intro.webm",
            "gameflow-background": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/gameflow-background.jpg",
            "gameflow-background-dark": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/gameflow-background-dark.jpg",
            "gameselect-button-hover-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Shared/sound/sfx-gameselect-button-hover.ogg",
            "icon-defeat": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-defeat.png",
            "icon-defeat-v2": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-defeat-v2.png",
            "icon-defeat-video": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/video/icon-defeat.webm",
            "icon-empty": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-empty.png",
            "icon-hover": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-hover.png",
            "icon-leaver": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-leaver.png",
            "icon-leaver-v2": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-leaver-v2.png",
            "icon-loss-forgiven-v2": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-loss-forgiven-v2.png",
            "icon-v2": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-v2.png",
            "icon-victory": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/icon-victory.png",
            "icon-victory-video": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/video/icon-victory.webm",
            "map-north": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/map-north.png",
            "map-south": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/map-south.png",
            "music-inqueue-loop-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/sound/music-inqueue-loop-summonersrift.ogg",
            "parties-background": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/parties-background.jpg",
            "postgame-ambience-loop-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/sound/sfx-ambience-loop-summonersrift.ogg",
            "ready-check-background": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/ready-check-background.png",
            "ready-check-background-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/sound/sfx-readycheck-sr-portal.ogg",
            "sfx-ambience-pregame-loop-sound": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/sound/sfx-ambience-loop-summonersrift.ogg",
            "social-icon-leaver": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/social-icon-leaver.png",
            "social-icon-victory": "lol-game-data/assets/content/src/LeagueClient/GameModeAssets/Classic_SRU/img/social-icon-victory.png"
        },
        "categorizedContentBundles": {},
        "description": "正义之地最新潮最威严的战场当属召唤师峡谷。无数对立的召唤师们在这片战场上延续着战斗，这片战场也因此而得名。有三条不同的道路贯穿整个战场。与友军一起攻击敌人最脆弱的地方，摧毁他们的基地！",
        "gameMode": "CLASSIC",
        "gameModeName": "召唤师峡谷",
        "gameModeShortName": "召唤师峡谷",
        "gameMutator": "",
        "id": 11,
        "isRGM": false,
        "mapStringId": "SR",
        "name": "召唤师峡谷",
        "perPositionDisallowedSummonerSpells": {},
        "perPositionRequiredSummonerSpells": {},
        "platformId": "",
        "platformName": "",
        "properties": {
            "suppressRunesMasteriesPerks": false
        }
    },
    "phase": "InProgress"
}
```

## 对局开始
> https://github.com/XHXIAIEIN/LeagueCustomLobby/wiki/client:--game-client

以下为对局开始后才可以访问的API，端口是固定的`2999`。

### /liveclientdata/allgamedata
获取当前对局中，所有玩家的英雄数据。等级、属性、技能、装备、符文、事件、地图数据等...

其中事件存在在events里，包括击杀、双杀、三杀等。
	
creepScore	补兵数
kills	击杀数
deaths	死亡数
assists	助攻数
wardScore	视野得分

目前，补兵数 creepScore 的数据并非实时刷新，而是每 10 个补兵更新一次。
https://github.com/RiotGames/developer-relations/issues/416

```json
{
    "activePlayer": {
        "abilities": {
            "E": {
                "abilityLevel": 1,
                "displayName": "恶魔审判",
                "id": "VayneCondemn",
                "rawDescription": "GeneratedTip_Spell_VayneCondemn_Description",
                "rawDisplayName": "GeneratedTip_Spell_VayneCondemn_DisplayName"
            },
            "Passive": {
                "displayName": "暗夜猎手",
                "id": "VaynePassive",
                "rawDescription": "GeneratedTip_Passive_VaynePassive_Description",
                "rawDisplayName": "GeneratedTip_Passive_VaynePassive_DisplayName"
            },
            "Q": {
                "abilityLevel": 1,
                "displayName": "闪避突袭",
                "id": "VayneTumble",
                "rawDescription": "GeneratedTip_Spell_VayneTumble_Description",
                "rawDisplayName": "GeneratedTip_Spell_VayneTumble_DisplayName"
            },
            "R": {
                "abilityLevel": 0,
                "displayName": "终极时刻",
                "id": "VayneInquisition",
                "rawDescription": "GeneratedTip_Spell_VayneInquisition_Description",
                "rawDisplayName": "GeneratedTip_Spell_VayneInquisition_DisplayName"
            },
            "W": {
                "abilityLevel": 1,
                "displayName": "圣银弩箭",
                "id": "VayneSilveredBolts",
                "rawDescription": "GeneratedTip_Spell_VayneSilveredBolts_Description",
                "rawDisplayName": "GeneratedTip_Spell_VayneSilveredBolts_DisplayName"
            }
        },
        "championStats": {
            "abilityHaste": 0,
            "abilityPower": 0,
            "armor": 43.2140007019043,
            "armorPenetrationFlat": 0,
            "armorPenetrationPercent": 1,
            "attackDamage": 72.6614990234375,
            "attackRange": 550,
            "attackSpeed": 0.9093361496925354,
            "bonusArmorPenetrationPercent": 1,
            "bonusMagicPenetrationPercent": 1,
            "critChance": 0,
            "critDamage": 175,
            "currentHealth": 498.29180908203125,
            "healShieldPower": 0,
            "healthRegenRate": 1.0399000644683838,
            "lifeSteal": 0,
            "magicLethality": 0,
            "magicPenetrationFlat": 0,
            "magicPenetrationPercent": 1,
            "magicResist": 34.016998291015625,
            "maxHealth": 868.27001953125,
            "moveSpeed": 330,
            "omnivamp": 0,
            "physicalLethality": 0,
            "physicalVamp": 0,
            "resourceMax": 340.1500244140625,
            "resourceRegenRate": 1.6471999883651733,
            "resourceType": "MANA",
            "resourceValue": 340.1500244140625,
            "spellVamp": 0,
            "tenacity": 5
        },
        "currentGold": 516.3764038085938,
        "fullRunes": {
            "generalRunes": [
                {
                    "displayName": "致命节奏",
                    "id": 8008,
                    "rawDescription": "perk_tooltip_LethalTempo",
                    "rawDisplayName": "perk_displayname_LethalTempo"
                },
                {
                    "displayName": "凯旋",
                    "id": 9111,
                    "rawDescription": "perk_tooltip_9111",
                    "rawDisplayName": "perk_displayname_9111"
                },
                {
                    "displayName": "传说：欢欣",
                    "id": 9104,
                    "rawDescription": "perk_tooltip_9104",
                    "rawDisplayName": "perk_displayname_9104"
                },
                {
                    "displayName": "致命一击",
                    "id": 8014,
                    "rawDescription": "perk_tooltip_CoupDeGrace",
                    "rawDisplayName": "perk_displayname_CoupDeGrace"
                },
                {
                    "displayName": "血之滋味",
                    "id": 8139,
                    "rawDescription": "perk_tooltip_TasteOfBlood",
                    "rawDisplayName": "perk_displayname_TasteOfBlood"
                },
                {
                    "displayName": "寻宝猎人",
                    "id": 8135,
                    "rawDescription": "perk_tooltip_TreasureHunter",
                    "rawDisplayName": "perk_displayname_TreasureHunter"
                }
            ],
            "keystone": {
                "displayName": "致命节奏",
                "id": 8008,
                "rawDescription": "perk_tooltip_LethalTempo",
                "rawDisplayName": "perk_displayname_LethalTempo"
            },
            "primaryRuneTree": {
                "displayName": "精密",
                "id": 8000,
                "rawDescription": "perkstyle_tooltip_7201",
                "rawDisplayName": "perkstyle_displayname_7201"
            },
            "secondaryRuneTree": {
                "displayName": "主宰",
                "id": 8100,
                "rawDescription": "perkstyle_tooltip_7200",
                "rawDisplayName": "perkstyle_displayname_7200"
            },
            "statRunes": [
                {
                    "id": 5005,
                    "rawDescription": "perk_tooltip_StatModAttackSpeed"
                },
                {
                    "id": 5008,
                    "rawDescription": "perk_tooltip_StatModAdaptive"
                },
                {
                    "id": 5002,
                    "rawDescription": "perk_tooltip_StatModArmor"
                }
            ]
        },
        "level": 5,
        "summonerName": "长发及腰懒得洗",
        "teamRelativeColors": true
    },
    "allPlayers": [
        {
            "championName": "暗夜猎手",
            "isBot": false,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "反曲之弓",
                    "itemID": 1043,
                    "price": 400,
                    "rawDescription": "GeneratedTip_Item_1043_Description",
                    "rawDisplayName": "Item_1043_Name",
                    "slot": 0
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 5,
            "position": "",
            "rawChampionName": "game_character_displayname_Vayne",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "致命节奏",
                    "id": 8008,
                    "rawDescription": "perk_tooltip_LethalTempo",
                    "rawDisplayName": "perk_displayname_LethalTempo"
                },
                "primaryRuneTree": {
                    "displayName": "精密",
                    "id": 8000,
                    "rawDescription": "perkstyle_tooltip_7201",
                    "rawDisplayName": "perkstyle_displayname_7201"
                },
                "secondaryRuneTree": {
                    "displayName": "主宰",
                    "id": 8100,
                    "rawDescription": "perkstyle_tooltip_7200",
                    "rawDisplayName": "perkstyle_displayname_7200"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 10,
                "deaths": 1,
                "kills": 0,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "长发及腰懒得洗",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "净化",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerBoost_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerBoost_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "虚弱",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerExhaust_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerExhaust_DisplayName"
                }
            },
            "team": "ORDER"
        },
        {
            "championName": "赏金猎人",
            "isBot": true,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "女神之泪",
                    "itemID": 3070,
                    "price": 400,
                    "rawDescription": "GeneratedTip_Item_3070_Description",
                    "rawDisplayName": "Item_3070_Name",
                    "slot": 0
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 5,
            "position": "",
            "rawChampionName": "game_character_displayname_MissFortune",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "强攻",
                    "id": 8005,
                    "rawDescription": "perk_tooltip_PressTheAttack",
                    "rawDisplayName": "perk_displayname_PressTheAttack"
                },
                "primaryRuneTree": {
                    "displayName": "精密",
                    "id": 8000,
                    "rawDescription": "perkstyle_tooltip_7201",
                    "rawDisplayName": "perkstyle_displayname_7201"
                },
                "secondaryRuneTree": {
                    "displayName": "巫术",
                    "id": 8200,
                    "rawDescription": "perkstyle_tooltip_7202",
                    "rawDisplayName": "perkstyle_displayname_7202"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 10,
                "deaths": 0,
                "kills": 0,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "赏金猎人（电脑）",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "幽灵疾步",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "治疗术",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                }
            },
            "team": "ORDER"
        },
        {
            "championName": "麦林炮手",
            "isBot": true,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "萃取",
                    "itemID": 1083,
                    "price": 450,
                    "rawDescription": "GeneratedTip_Item_1083_Description",
                    "rawDisplayName": "Item_1083_Name",
                    "slot": 0
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 5,
            "position": "",
            "rawChampionName": "game_character_displayname_Tristana",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "强攻",
                    "id": 8005,
                    "rawDescription": "perk_tooltip_PressTheAttack",
                    "rawDisplayName": "perk_displayname_PressTheAttack"
                },
                "primaryRuneTree": {
                    "displayName": "精密",
                    "id": 8000,
                    "rawDescription": "perkstyle_tooltip_7201",
                    "rawDisplayName": "perkstyle_displayname_7201"
                },
                "secondaryRuneTree": {
                    "displayName": "巫术",
                    "id": 8200,
                    "rawDescription": "perkstyle_tooltip_7202",
                    "rawDisplayName": "perkstyle_displayname_7202"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 20,
                "deaths": 0,
                "kills": 0,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "麦林炮手（电脑）",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "幽灵疾步",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "治疗术",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                }
            },
            "team": "ORDER"
        },
        {
            "championName": "暮光之眼",
            "isBot": true,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "多兰之盾",
                    "itemID": 1054,
                    "price": 450,
                    "rawDescription": "GeneratedTip_Item_1054_Description",
                    "rawDisplayName": "Item_1054_Name",
                    "slot": 0
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 5,
            "position": "",
            "rawChampionName": "game_character_displayname_Shen",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "不灭之握",
                    "id": 8437,
                    "rawDescription": "perk_tooltip_GraspOfTheUndying",
                    "rawDisplayName": "perk_displayname_GraspOfTheUndying"
                },
                "primaryRuneTree": {
                    "displayName": "坚决",
                    "id": 8400,
                    "rawDescription": "perkstyle_tooltip_7204",
                    "rawDisplayName": "perkstyle_displayname_7204"
                },
                "secondaryRuneTree": {
                    "displayName": "巫术",
                    "id": 8200,
                    "rawDescription": "perkstyle_tooltip_7202",
                    "rawDisplayName": "perkstyle_displayname_7202"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 10,
                "deaths": 0,
                "kills": 0,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "暮光之眼（电脑）",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "幽灵疾步",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "治疗术",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                }
            },
            "team": "CHAOS"
        },
        {
            "championName": "寒冰射手",
            "isBot": true,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "长剑",
                    "itemID": 1036,
                    "price": 350,
                    "rawDescription": "GeneratedTip_Item_1036_Description",
                    "rawDisplayName": "Item_1036_Name",
                    "slot": 0
                },
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "短剑",
                    "itemID": 1042,
                    "price": 300,
                    "rawDescription": "GeneratedTip_Item_1042_Description",
                    "rawDisplayName": "Item_1042_Name",
                    "slot": 1
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 4,
            "position": "",
            "rawChampionName": "game_character_displayname_Ashe",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "强攻",
                    "id": 8005,
                    "rawDescription": "perk_tooltip_PressTheAttack",
                    "rawDisplayName": "perk_displayname_PressTheAttack"
                },
                "primaryRuneTree": {
                    "displayName": "精密",
                    "id": 8000,
                    "rawDescription": "perkstyle_tooltip_7201",
                    "rawDisplayName": "perkstyle_displayname_7201"
                },
                "secondaryRuneTree": {
                    "displayName": "巫术",
                    "id": 8200,
                    "rawDescription": "perkstyle_tooltip_7202",
                    "rawDisplayName": "perkstyle_displayname_7202"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 10,
                "deaths": 0,
                "kills": 0,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "寒冰射手（电脑）",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "幽灵疾步",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "治疗术",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                }
            },
            "team": "CHAOS"
        },
        {
            "championName": "爆破鬼才",
            "isBot": true,
            "isDead": false,
            "items": [
                {
                    "canUse": false,
                    "consumable": false,
                    "count": 1,
                    "displayName": "多兰之戒",
                    "itemID": 1056,
                    "price": 400,
                    "rawDescription": "GeneratedTip_Item_1056_Description",
                    "rawDisplayName": "Item_1056_Name",
                    "slot": 0
                },
                {
                    "canUse": true,
                    "consumable": false,
                    "count": 1,
                    "displayName": "侦查守卫",
                    "itemID": 3340,
                    "price": 0,
                    "rawDescription": "GeneratedTip_Item_3340_Description",
                    "rawDisplayName": "Item_3340_Name",
                    "slot": 6
                }
            ],
            "level": 6,
            "position": "",
            "rawChampionName": "game_character_displayname_Ziggs",
            "respawnTimer": 0,
            "runes": {
                "keystone": {
                    "displayName": "奥术彗星",
                    "id": 8229,
                    "rawDescription": "perk_tooltip_ArcaneComet",
                    "rawDisplayName": "perk_displayname_ArcaneComet"
                },
                "primaryRuneTree": {
                    "displayName": "巫术",
                    "id": 8200,
                    "rawDescription": "perkstyle_tooltip_7202",
                    "rawDisplayName": "perkstyle_displayname_7202"
                },
                "secondaryRuneTree": {
                    "displayName": "主宰",
                    "id": 8100,
                    "rawDescription": "perkstyle_tooltip_7200",
                    "rawDisplayName": "perkstyle_displayname_7200"
                }
            },
            "scores": {
                "assists": 0,
                "creepScore": 30,
                "deaths": 0,
                "kills": 1,
                "wardScore": 0
            },
            "skinID": 0,
            "summonerName": "爆破鬼才（电脑）",
            "summonerSpells": {
                "summonerSpellOne": {
                    "displayName": "幽灵疾步",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHaste_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHaste_DisplayName"
                },
                "summonerSpellTwo": {
                    "displayName": "治疗术",
                    "rawDescription": "GeneratedTip_SummonerSpell_SummonerHeal_Description",
                    "rawDisplayName": "GeneratedTip_SummonerSpell_SummonerHeal_DisplayName"
                }
            },
            "team": "CHAOS"
        }
    ],
    "events": {
        "Events": [
            {
                "EventID": 0,
                "EventName": "GameStart",
                "EventTime": 0.027270900085568428
            },
            {
                "EventID": 1,
                "EventName": "MinionsSpawning",
                "EventTime": 65.03478240966797
            },
            {
                "Assisters": [],
                "EventID": 2,
                "EventName": "ChampionKill",
                "EventTime": 199.5167999267578,
                "KillerName": "爆破鬼才（电脑）",
                "VictimName": "长发及腰懒得洗"
            },
            {
                "EventID": 3,
                "EventName": "FirstBlood",
                "EventTime": 199.5167999267578,
                "Recipient": "爆破鬼才（电脑）"
            }
        ]
    },
    "gameData": {
        "gameMode": "CLASSIC",
        "gameTime": 344.08392333984375,
        "mapName": "Map11",
        "mapNumber": 11,
        "mapTerrain": "Default"
    }
}

```





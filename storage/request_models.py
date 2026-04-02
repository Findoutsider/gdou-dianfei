from pydantic import BaseModel

LoginUrl = "https://dkgl.gdou.edu.cn/kbp/auth/app/userLogin"
GetEleBalanceUrl = "https://dkgl.gdou.edu.cn/kbp/ele/wechat/ele/eleBalance"
GetUserInfoUrl = "https://dkgl.gdou.edu.cn/kbp/auth/userInfo"
GetEleSituationUrl = "https://dkgl.gdou.edu.cn/kbp/ele/wechat/eleSituation"
GetRoomInfoUrl = "https://dkgl.gdou.edu.cn/kbp/admin/sys/personRoom/page"
GetRoomListUrl = "https://dkgl.gdou.edu.cn/kbp/ele/mobile/assigned/room/list"


class LoginRequest(BaseModel):
    # 学号
    username: str
    password: str
    loginType: int = 1


class EleBalanceRequest(BaseModel):
    # 1为宿舍，2为空调，3为照明，4为插座，但1和4都是请求都是0
    useEleType: int
    roomCode: str


class RoomInfoRequest(BaseModel):
    username: str
    pageSize: int = 10
    pageNumber: int = 1


class EleSituationRequest(BaseModel):
    # param: { "username": "" }
    pass

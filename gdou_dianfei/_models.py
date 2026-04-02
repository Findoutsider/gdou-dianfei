from typing import Any

from pydantic import BaseModel

# API URLs
LoginUrl = "https://dkgl.gdou.edu.cn/kbp/auth/app/userLogin"
GetEleBalanceUrl = "https://dkgl.gdou.edu.cn/kbp/ele/wechat/ele/eleBalance"
GetUserInfoUrl = "https://dkgl.gdou.edu.cn/kbp/auth/userInfo"
GetRoomListUrl = "https://dkgl.gdou.edu.cn/kbp/ele/mobile/assigned/room/list"


# 请求体
class LoginRequest(BaseModel):
    username: str
    password: str
    loginType: int = 1


class EleBalanceRequest(BaseModel):
    # 1为宿舍，2为空调，3为照明，4为插座
    useEleType: int
    roomCode: str


# 返回体
class UserInfoResponseData(BaseModel):
    userId: int
    username: str
    name: str
    status: int
    password: str
    remark: Any
    roleCodes: list
    isVisitor: bool
    personType: int
    isMortal: int
    serviceList: list
    startDate: Any
    endDate: Any
    loginApp: Any
    promptChangePassword: Any


class LoginResponseData(BaseModel):
    accessToken: str
    userInfo: UserInfoResponseData
    openId: Any


class LoginResponse(BaseModel):
    code: int
    msg: str
    data: LoginResponseData


class EleBalanceResponseData(BaseModel):
    roomCode: str
    areaInfo: str
    moneyBalance: float
    itemSubsidyBalance: float
    moneySubsidyBalance: float
    todayBalance: float
    monthBalance: float
    billBalance: float
    billCreateTime: Any


class EleBalanceResponse(BaseModel):
    code: int
    msg: str
    data: EleBalanceResponseData


class UserInfoResponse(BaseModel):
    code: int
    msg: str
    data: UserInfoResponseData


class RoomInfo(BaseModel):
    areaInfo: str
    endDate: Any
    payModel: int
    roomCode: str
    useAmountTotal: float
    useEleTypeList: list[int]
    userIdentity: int


class RoomListResponse(BaseModel):
    code: int
    msg: str
    data: list[RoomInfo]

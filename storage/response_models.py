from typing import Any

from pydantic import BaseModel


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

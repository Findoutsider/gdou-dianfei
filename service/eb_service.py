import requests

from exception.exceptions import AuthFailedException, NoAuthException
from storage.request_models import *
from storage.response_models import *
from utils.passwd import decrypt, encrypt


class EBService:
    def __init__(self, username: str, password: str, login_type: int = 1):
        self.username = username
        self.password = password
        self.login_type = login_type
        self.token = ""
        self.roomCode: list[str] = []
        self.isAuthenticated = False
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        })

    def _post(self, url: str, data: dict = None, json: dict = None) -> requests.Response:
        return self.session.post(url, data=data, json=json)

    def _get(self, url: str, params: dict = None) -> requests.Response:
        return self.session.get(url, params=params)

    def login(self) -> LoginResponseData:
        password = encrypt(self.password)
        data = LoginRequest(username=self.username, password=password, loginType=self.login_type)
        response = self._post(LoginUrl, json=data.__dict__)
        response_data = LoginResponse(**response.json())

        if response_data.code != 200:
            raise AuthFailedException(response_data.msg)

        self.token = response_data.data.accessToken
        self.session.headers.update({"Authorization": f"{self.token}"})
        self.isAuthenticated = True

        return response_data.data

    def get_user_info(self) -> UserInfoResponseData:
        if not self.isAuthenticated:
            raise NoAuthException("请先登录")

        response = self._get(GetUserInfoUrl)
        response_data = UserInfoResponse(**response.json())
        if response_data.code != 200:
            raise Exception(response_data.msg)

        return response_data.data

    def get_room_list(self) -> RoomListResponse:
        if not self.isAuthenticated:
            raise NoAuthException("请先登录")

        response = self._get(GetRoomListUrl)
        response_data = RoomListResponse(**response.json())
        if response_data.code != 200:
            raise Exception(response_data.msg)

        self.roomCode = [room.roomCode for room in response_data.data]
        return response_data

    def get_ac_ele_balance(self, roomIndex: int = 1) -> EleBalanceResponseData:
        if not self.isAuthenticated:
            raise NoAuthException("请先登录")
        if not self.roomCode:
            self.get_room_list()

        roomIndex = roomIndex - 1

        data = EleBalanceRequest(useEleType=2, roomCode=self.roomCode[roomIndex])

        response = self._post(GetEleBalanceUrl, json=data.__dict__)
        response_data = EleBalanceResponse(**response.json())
        if response_data.code != 200:
            raise Exception(response_data.msg)

        return response_data.data

    def get_light_ele_balance(self, roomIndex: int = 1) -> EleBalanceResponseData:
        if not self.isAuthenticated:
            raise NoAuthException("请先登录")
        if self.roomCode == []:
            self.get_room_list()

        roomIndex = roomIndex - 1

        data = EleBalanceRequest(useEleType=3, roomCode=self.roomCode[roomIndex])

        response = self._post(GetEleBalanceUrl, json=data.__dict__)
        response_data = EleBalanceResponse(**response.json())
        if response_data.code != 200:
            raise Exception(response_data.msg)

        return response_data.data

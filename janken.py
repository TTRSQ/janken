#coding: utf-8

import sys
import requests
import json 

# TODO: エラー処理


#======== ジャンケン =========
class Janken:
    # 自分から勝てる相手に向かった有向グラフ
    weapons = {
        "rock":     [1, 3],
        "paper":    [2, 1],
        "scissors": [3, 2],
    }

    def result(field_weapons, side):


#======== プレーヤー =========
class JankenPlayer(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def validate_weapon(weapon):
        for _weapon in Janken.weapons.keys():
            if weapon == _weapon:
                return
        print('Error')
        exit(0)

    @abstractmethod
    def get_weapon(self):
        pass

class ShellUser(JankenPlayer):
    def get_weapon(self):
        weapon = input()
        return weapon

class Comupter(JankenPlayer):
    def get_weapon(self):
        json_str = requests.get("https://github.com")
        dic_data = json.load(json_str)
        return dic_data["weapon"]


#======== 試合管理 =========
class JankenManager:
    def __init__(self, players, max_num):
        self.janken  = Janken()
        slef.players = players
        self.max_num = max_num
    
    def execute(self):
        field_weapons = []
        for player in players:
            field_weapons.append(player.get_weapon)
        
        side = self.result(field_weapons, )


args = sys.argv
janken_times = args[1]

janken_manager = JankenManager(
    [ShellUser(), Comupter()],
    janken_times
)

janken_manager.execute()
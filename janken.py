#coding: utf-8

import sys
import requests
import json
from abc import ABCMeta, abstractmethod

# TODO: エラー処理


#======== ジャンケン =========
class Janken:
    # 自分から勝てる相手に向かった有向グラフ
    weapons = {
        "rock":     [1, 3],
        "paper":    [2, 1],
        "scissors": [3, 2],
    }

    @classmethod
    def result(cls, field_weapons, side):
        pass

#======== プレーヤー =========
class JankenPlayer(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def validate_weapon(self, weapon):
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
        self.validate_weapon(weapon)
        return weapon

class Comupter(JankenPlayer):
    def get_weapon(self):
        json_str = requests.get("https://example.com/janken").text
        dic_data = json.loads(json_str)
        weapon = dic_data["weapon"]
        self.validate_weapon(weapon)
        return weapon


#======== 試合管理 =========
class JankenManager:
    def __init__(self, players, max_num):
        self.players = players
        self.max_num = max_num
    
    def execute(self):
        for i in range(self.max_num):
            field_weapons = []
            for player in self.players:
                weapon = player.get_weapon()
                print(player.get_name(), "select", weapon)
                field_weapons.append(weapon)
                Janken.result(field_weapons, weapon)

args = sys.argv
janken_times = int(args[1])

janken_manager = JankenManager(
    [ShellUser("You"), Comupter("Com")],
    janken_times
)

janken_manager.execute()

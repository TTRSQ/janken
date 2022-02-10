# janken
抽象化を用いてじゃんけんを実装してくれという友達の要望に答えたもの


## ワード整理

- クライアント
	
	```
	その名の通り客で,サーバーに注文(request)をして
	回答(respons)をもらう
	```

- 標準入力
	
	```
	雑に標準入力とか言われたときはシェル(ターミナルとか)
	でぶっ込めるようにしてくれという意味と捉えれば問題ない
	```

- endpoint
	
	```
	webサービス界隈で使うと、ネット上のここに
	その関数(api)の受け口あるよくらいの意味
	
	apiにリクエストを送る方法は代表的に get と post があって
	
	```

- json

	```
	- 文字列としてデータを持つ一般的な方法,'{"key": "value"}'の形でかく
	- ただの文字列なのでデータとして扱うにはバラしてプログラム内の変数に代入する
		必要があるが、これをパースという
	- jsonをパースするためのライブラリはクソほどあるので自分で書く必要はない
	```
	
## python3で話進めます

### 今回できないといけないこと
1. 標準入力を受け取る
1. apiリクエストを送る
1. jsonパース
1. オブジェクト思考でコードを書く

## 標準入力
1. インターフェース例がクソ雑なのでとりあえず入力だけ取れれば良さそう
1. 「python 標準入力」で検索してみる
1. `str = input()`で文字列受け取れそう

## apiリクエスト
一般的にapiってurl叩くとjsonが帰ってくるネット上の関数と思ってよい  
「python3 api request」で検索すると以下の形でjson取れそう

```
import requests
str = requests.get("https://github.com").text # strにjson文字列が入る
```

## jsonパース
「python3 json パース」で同様に

```
import json  
data = json.loads(json_str) # json文字列 => dic型
```

## オブジェクト思考
正直定義不足すぎて意味不明な注文なのであまり親身に対応する必要性がない気がするが、一旦オブジェクト指向とは何かについて考える

```
### 見た目的には
- データと関数をセットにしたもの（オブジェクト）
- 自分の（変数、状態）面等を自分で見るもの（オブジェクト）

### 概念的には
- カプセル化
	- インターフェース(上記関数)を通してオブジェクトにアクセスする制約
- 継承
	- 具象概念で抽象概念を取りまとめることができる
- ポリモーフィズム
	- 共通なインターフェースの中で概念に遊びを持たせる
```

# コードを書くときの思考

### ジャンケンという概念を正しく定義するために色々考える

- ジャンケンは何で成り立っているか
	- 手の種類(グーチョキパーのこと)(data)
	- 手同士の強さ関係(data)
	- 上記に基づいた戦い(function)
- 参加者は必ずしも二人ではないのでその辺にも対応したい
- 参加者の関係に構造はなく、同じ立場の人は同じ結果になる
	- 2階からパーを出した人は一階の戦いでグーが勝った場合勝ちみたいなことにはならない
- battle(field: [weapon, ...], side) result


```
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
        json_str = requests.get("https://github.com").text
        dic_data = json.loads(json_str)
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
```

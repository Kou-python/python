import random
import time

# 初期状態
play_count = 0
win_count = 0
lose_count = 0

# 数字、手
ROCK = 0
SCISSORS = 1
PAPER = 2

HANDS = {
    ROCK: "グー",
    SCISSORS: "チョキ",
    PAPER: "パー"
}

# 数字、結果
WIN = 0
LOSE = 1
DRAW = 2

RESULTS = {
    WIN: "勝ち",
    LOSE: "負け",
    DRAW: "引き分け"
}

while True:
    player_hand = None
    while player_hand not in HANDS.keys():
        print("じゃんけんの手を入力してね")
        print("ぐー[0],ちょき[1],パー[2]")
        player_hand = int(input("> "))

    cpu_hand = random.randint(0, 2)

    print("じゃんけん、ぽん！...")
    if player_hand == cpu_hand:
        results = DRAW
    elif player_hand == ROCK and cpu_hand == SCISSORS:
        results = WIN
    elif player_hand == SCISSORS and cpu_hand == PAPER:
        results = WIN
    elif player_hand == PAPER and cpu_hand == ROCK:
        results = WIN
    else:
        results = LOSE

    print("あなたの手: {}".format(HANDS[player_hand]))
    print("CPUの手: {}".format(HANDS[cpu_hand]))
    print("勝敗: {}".format(RESULTS[results]))

    play_count += 1
    if results == WIN:
        win_count += 1
    elif results == LOSE:
        lose_count += 1

    print("[あなたの戦績] 勝負数{}, 勝利数{}, 敗北数{}".format(play_count, win_count, lose_count))

    YES= 1
    NO= 2

    FINISH = {
        YES: "はい",
        NO: "いいえ"
    }

    finish = None
    while finish not in FINISH.keys():
        print("ゲームを続けますか？ 続ける[1]やめる[2]")
        finish = int(input("> "))

    if finish==YES:
        continue
    else:
        break
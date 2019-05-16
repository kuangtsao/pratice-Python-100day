"""
玩家搖兩個骰子，如果第一次就搖出7或11點，玩家勝；如果第一次就搖出2,3,12點，莊家勝
；其他情況遊戲繼續：玩家再次搖兩個骰子，如果出7點，莊家勝；如果搖出第一次搖的點數，玩家勝；都不是則遊戲繼續。

玩家有1000元的賭注，全部輸光則遊戲結束。

"""

from random import randint

asset = 1000

while asset > 0:
    print ('總注金：', asset)
    gamble_continue = False
    while True:
        bet = int(input('請下注：'))
        if bet > 0 and bet <= asset:
            break
    first_gamble = randint(1, 6) + randint(1, 6)
    print('玩家搖出了%d點' % first_gamble)
    if first_gamble == 7 or first_gamble == 11:
        print('贏得彩金！')
        asset += bet
    elif first_gamble == 2 or first_gamble == 3 or first_gamble == 12:
        print('輸去彩金！')
        asset -= bet
    else: 
        gamble_continue = True
     
    while gamble_continue:
        print('第二次對決！')
        second_gamble = randint(1, 6) + randint(1, 6)
        print('玩家搖出了%d點' % second_gamble)

        if second_gamble == 7:
            print('莊家勝！')
            asset -= bet
            gamble_continue = False
        elif second_gamble == first_gamble:
            print('玩家勝！')
            asset += bet
            gamble_continue = False


print('沒錢啦！')

   


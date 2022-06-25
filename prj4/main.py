import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'


def get_bet(max_bet):
    while True:
        print("Сколько ставим на кон? (1 - {}) или (Q)uit".format(max_bet))
        bet = input('> ').upper().strip()
        if (bet == 'Q') or (bet == 'QUIT'):
            print('Спасибо за игру!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet
        else:
            print('Слишком большая ставка!')
            continue


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(pl_hand, dl_hand, show_dl_hand):
    print()
    if show_dl_hand:
        print('ДИЛЕР:', get_hand_value(dl_hand))
        display_cards(dl_hand)
    else:
        print('ДИЛЕР: ???')
        display_cards([BACKSIDE] + dl_hand[1:])

    print('ИГРОК:', get_hand_value(pl_hand))
    display_cards(pl_hand)


def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces = number_of_aces + 1
        elif rank in ('J', 'Q', 'K'):
            value = value + 10
        else:
            value = value + int(rank)

    value = value + number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value = value + 10
    return value


def display_cards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] = rows[0] + ' ___ '
        if card == BACKSIDE:
            rows[1] = rows[1] + '|## |'
            rows[2] = rows[2] + '|###|'
            rows[3] = rows[3] + '|_##|'
        else:
            rank, suit = card
            rows[1] = rows[1] + '|{} |'.format(rank.ljust(2))
            rows[2] = rows[2] + '| {} |'.format(suit)
            rows[3] = rows[3] + '|_{}|'.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def get_move(pl_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(pl_hand) == 2 and money > 0:
            moves.append('(D)ouble down')
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


def main():
    print('''
        Игра "Блекджек"
        
        Правила:
            Нужно набрать сумму очков, максимально близкую к 21, но не больше.
            Короли, Дамы и Валеты дают по 10 очков.
            Тузы дают или 1, или 11 очков.
            Карты с 2 до 10 дают номинальное количество очков.
            (H) - для получения ещё одной карты
            (S) - для остановки взятия карт
            (D) - в свой первый ход можно удвоить сумму ставки, 
            но тогда нужно взять одну карту перед остановкой.
            В случае ничьей ставка возвращается игроку.
            
            Диллер не берет карты, если больше 17 очков.    
    
    ''')
    money = 5000
    while True:
        if money <= 0:
            print('Увы, но ваши деньги закончились!')
            print('Хорошо, что это ненастоящие деньги...')
            print('Спасибо за игру и приятного дня!')
            sys.exit()
        print('На счету: {}'.format(money))
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print('Ставка: {}'.format(bet))
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == 'D':
                additional_bet = get_bet((min(bet, (money - bet))))
                bet = bet + additional_bet
                print('Ставка успешно увеличена до {}'.format(bet))
                print('Ставка:', bet)

            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print('Твоя карта - {} {}'.format(rank, suit))
                player_hand.append(new_card)
                if get_hand_value(player_hand) > 21:
                    continue
            if move in ('S', 'D'):
                break
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print('Дилер берет карту...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input('Нажми Enter чтобы продолжить')
                print('\n\n')

        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print('Дилер перебрал! Ты забираешь домой {}$!!!'.format(bet))
            money = money + bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('Это проигрышь! Ты теряешь {}$'.format(bet))
            money = money - bet
        elif player_value > dealer_value:
            print('Чистая победа! Забирай {}$!'.format(bet))
            money = money + bet
        elif player_value == dealer_value:
            print('Это ничья.Ставка возвращается обратно...')

        input('Press Enter to continue...')
        print('\n\n')


if __name__ == '__main__':
    main()

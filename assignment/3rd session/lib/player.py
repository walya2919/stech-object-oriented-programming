ACTIONS = {"HOLD": 0, "DRAW": 1}

class Player:
    def __init__(self, money):
        self.money = money
        self.hands = []

    def reset(self, play_money):
        self.money = self.money - play_money
        self.hands = []

    def act(self, states, evaluate):
        raise NotImplementedError

    def draw(self, new_card):
        self.hands.append(new_card)

    def reward(self, reward_money):
        self.money = self.money + reward_money


class Dealer(Player):
    def __init__(self, money):
        super().__init__(money)
        self.name = "Dealer"
        self.number = "00000000"

    def act(self, states, evaluate):
        value = evaluate(self.hands)
        if value < 17:
            return ACTIONS["DRAW"]
        return ACTIONS["HOLD"]


class Seojin24102406(Player):
    def __init__(self, money):
        super().__init__(money)
        self.name = "Seojin"
        self.number = 24102406

    def act(self, states, evaluate):
        HAND_TYPE={"SOFT" : 0, "HARD" : 1}
        
        # define my hand type
        for card in self.hands:
            if card.value == 1:
                my_hand = HAND_TYPE["SOFT"]
            else:
                my_hand = HAND_TYPE["HARD"]
        value = evaluate(self.hands)

        for state, idx in zip(states, range(len(states))):
            if state["name"] == "Dealer":
                break
        dealer_value = evaluate(states[idx]["card"])
        if len(self.hands) == 2:
            if my_hand == HAND_TYPE["SOFT"]:
                if value < 18:
                    return ACTIONS["DRAW"]
                elif value > 18:
                    return ACTIONS["HOLD"]
                elif dealer_value <= 8:
                    return ACTIONS["HOLD"]
                else:
                    return ACTIONS["DRAW"]
            elif my_hand == HAND_TYPE["HARD"]:
                if value >= 17:
                    return ACTIONS["HOLD"]
                elif value <= 11:
                    return ACTIONS["DRAW"]
                elif value >= 13:
                    if dealer_value < 7:
                        return ACTIONS["HOLD"]
                    else:
                        return ACTIONS["DRAW"]
                else:
                    if 4 <= dealer_value & dealer_value <= 6:
                        return ACTIONS["HOLD"]
                    else:
                        return ACTIONS["DRAW"]
        
        if value > 17:
            return ACTIONS["HOLD"]
        else:
            return ACTIONS["DRAW"]
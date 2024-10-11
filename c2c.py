import random
import numpy as np

class Game:
    def __init__(self):
        self.deck = [0, 1, 2]
        self.cards = [None, None]
        self.scores = [0, 0]

    def deal_cards(self):
        self.cards = random.sample(self.deck, 2)

    def compare_cards(self): 
        if self.cards[0] > self.cards[1]:
            self.scores[0] += 1
            self.scores[1] -= 1
        elif self.cards[0] < self.cards[1]:
            self.scores[0] -= 1
            self.scores[1] += 1

    def play_round(self):
        self.deal_cards()
        self.compare_cards()

def run_simulation(num_games):
    game = Game()
    for _ in range(num_games):
        game.play_round()
    return game.scores

def analyze_game(num_games, num_simulations):
    all_scores = [run_simulation(num_games) for _ in range(num_simulations)]
    player1_scores = np.array([scores[0] for scores in all_scores])
    player2_scores = np.array([scores[1] for scores in all_scores])

    # Calculate variance and standard deviation (same for both players)
    variance = np.var(player1_scores)
    std_dev = np.std(player1_scores)

    print(f"\nGame Statistics (over {num_simulations} simulations of {num_games} games each):")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

    for player, scores in enumerate([player1_scores, player2_scores], 1):
        expected_value = np.mean(scores)
        winrate = (np.sum(scores > 0) / num_simulations) * 100
        
        # Calculate 95% confidence interval
        standard_error = std_dev / np.sqrt(num_simulations)
        confidence_interval = (
            expected_value - 1.96 * standard_error,
            expected_value + 1.96 * standard_error
        )

        print(f"\nPlayer {player} Statistics:")
        print(f"Expected Value: {expected_value:.2f}")
        print(f"Winrate: {winrate:.2f}%")
        print(f"95% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")

def main():
    num_games = 1000
    num_simulations = 1000
    analyze_game(num_games, num_simulations)

if __name__ == "__main__":
    main()
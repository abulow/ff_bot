from sentences import *

# Setup

team1 = "Hit the Quon"
team2 = "Relegate Lurie"
player1 = "Doug Martin"
position1 = "RB"
player2 = "Kirk Cousins"
position2 = "QB"
auction = "99"

week_num = "7"
winning_team = "Hit the Quon"
winning_owner = "Adam Bulow"
winning_score = "150"
winning_wins = "2"
winning_losses = "5"
losing_team = "Relegate Lurie"
losing_owner = "Adam Sharf"
losing_score = "102"
losing_wins = "4"
losing_losses = "3"

testing_keys = ["Trade Sentences", "Add/Drop Waiver Sentences", "Add/Drop Sentences", "Add Sentences", "Drop Sentences", "Score Sentences"]
testing_values = [trade_sentences, add_drop_waiver_sentences, add_drop_sentences, add_sentences, drop_sentences, score_sentences]
testing_dictionary = {key: value for key, value in zip(testing_keys, testing_values)}

def test_sentences():
    sentence_prompt = None
    exit_words = ['quit', 'q', 'exit']
    skip_words = ['skip', 'next']
    print("---------------")
    print("Sentence Tester")
    print("---------------")
    print()
    print("Instructions: ")
    print("- Press enter to proceed to the next sentence.")
    print("- To quit, enter any of: " + ', '.join(["'" + word + "'" for word in exit_words]) + ".")
    print("- To skip to the next sentence type, enter any of: " + ', '.join(["'" + word + "'" for word in skip_words]) + ".")
    print()
    for name, sentence_list in testing_dictionary.items():
        if sentence_prompt in exit_words:
            break
        start_list_prompt = input(name + ": ").lower()
        print()
        if start_list_prompt in exit_words:
            break
        elif start_list_prompt in skip_words:
            continue
        for sentence in sentence_list:
            cleaned_sentence = clean_sentence(sentence, team1, team2, player1, position1, player2, position2, auction, week_num, winning_team, winning_owner, winning_score, winning_wins, winning_losses, losing_team, losing_owner, losing_score, losing_wins, losing_losses)
            print(cleaned_sentence)
            print()
            cleaned_sentence_length = len(cleaned_sentence)
            sentence_prompt = input("Characters: " + str(cleaned_sentence_length) + " ")
            print()
            if sentence_prompt in exit_words + skip_words:
                break
    print("Done")

if __name__ == '__main__':
    test_sentences()
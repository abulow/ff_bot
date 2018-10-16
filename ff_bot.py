import tweepy as tp
from random import choice
from get_data import *
import sys
from config.sentences import *
from config.league_settings import *
from config.twitter_login import *

def tweet_trade(api, row):
    if row.Transaction == 'Accepted Trade':
        sentence = choice(trade_sentences)
        new_sentence = clean_sentence(sentence, team1=row.Team1, team2=row.Team2, player1=choice(row.Team1_Traded_Players.split(', ')), player2=choice(row.Team2_Traded_Players.split(', ')))
        try:
            api.update_status(new_sentence)
        except:
            pass

def tweet_add_drop_waiver(api, row):
    sentence = choice(add_drop_waiver_sentences)
    new_sentence = clean_sentence(sentence, team1=row.Team1, player1=row.Dropped_Player, player2=row.Added_Player, position1=row.Dropped_Player_Position, position2=row.Added_Player_Position, auction=row.Waiver_Bid)
    try:
        api.update_status(new_sentence)
    except:
        pass

def tweet_add_drop(api, row):
    sentence = choice(add_drop_sentences)
    new_sentence = clean_sentence(sentence, team1=row.Team1, player1=row.Dropped_Player, player2=row.Added_Player, position1=row.Dropped_Player_Position, position2=row.Added_Player_Position)
    try:
        api.update_status(new_sentence)
    except:
        pass

def tweet_add(api, row):
    sentence = choice(add_sentences)
    new_sentence = clean_sentence(sentence, team1=row.Team1, player1=row.Added_Player, position1=row.Added_Player_Position)
    try:
        api.update_status(new_sentence)
    except:
        pass

def tweet_drop(api, row):
    sentence = choice(drop_sentences)
    new_sentence = clean_sentence(sentence, team1=row.Team1, player1=row.Dropped_Player, position1=row.Dropped_Player_Position)
    try:
        api.update_status(new_sentence)
    except:
        pass

def tweet_transaction(api, row):
    if 'Trade' in row.Transaction:
        return tweet_trade(api, row)
    elif row.Transaction == 'Add/Drop':
        if row.Is_Waiver:
            return tweet_add_drop_waiver(api, row)
        else:
            return tweet_add_drop(api, row)
    elif row.Transaction == 'Add':
        return tweet_add(api, row)
    else:
        return tweet_drop(api, row)

def tweet_transactions(api):
    transactions_df = get_transactions_df(league_id, year)
    if not transactions_df is None:
        transactions_df = transactions_df.sort_values('Datetime')
        for idx, row in transactions_df.iterrows():
            tweet_transaction(api, row)

def tweet_score(api, row, week_num):
    sentence = choice(score_sentences)
    new_sentence = clean_sentence(sentence, week_num=week_num, winning_team=row.Winning_Team, winning_owner=row.Winning_Owner, winning_score=row.Winning_Score, winning_wins=row.Winning_Wins, winning_losses=row.Winning_Losses, losing_team=row.Losing_Team, losing_owner=row.Losing_Owner, losing_score=row.Losing_Score, losing_wins=row.Losing_Wins, losing_losses=row.Losing_Losses)
    try:
        api.update_status(new_sentence)
    except:
        pass

def tweet_scores(api, week_num):
    scoreboard_df = get_scoreboard_df(league_id, year, week)
    for idx, row in scoreboard_df.iterrows():
        tweet_score(api, row, week_num)

def run_bot(mode='transactions', week_num=''):
    # login to twitter account api
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)

    if mode == 'transactions':
        tweet_transactions(api)
    elif mode == 'scores':
        tweet_scores(api, week_num)

if __name__ == '__main__':
    print('Running...')

    mode = sys.argv[1]
    try:
        week_num = sys.argv[2]
    except:
        week_num = ''
    run_bot(mode, week_num)

    print("Done.")
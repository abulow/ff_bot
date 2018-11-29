from espnff import League
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import numpy as np

# Helper
def clean_owner(owner):
    if owner == 'Arturo Arturo':
        return 'Jose Chayet'
    elif owner == 'Adam Willis':
        return 'Adam Sloane'
    else:
        return owner

# For use after matchups have been completed and ESPN records have been updated (Tuesday morning)
def get_scoreboard_df(league_id, year, week):
    league = League(league_id, year)
    scoreboard = league.scoreboard(week=week)
    scoreboard_list_of_dicts = [
    {
    'Home_Team': matchup.home_team.team_name.title(),
    'Home_Owner': clean_owner(matchup.home_team.owner.title()),
    'Home_Score': matchup.home_score,
    'Home_Wins': matchup.home_team.wins,
    'Home_Losses': matchup.home_team.losses,
    'Away_Team': matchup.away_team.team_name.title(),
    'Away_Owner': clean_owner(matchup.away_team.owner.title()),
    'Away_Score': matchup.away_score,
    'Away_Wins': matchup.away_team.wins,
    'Away_Losses': matchup.away_team.losses,
    'Winner': matchup.home_team.team_name.title() if matchup.home_score > matchup.away_score else matchup.away_team.team_name.title(),
    'Loser': matchup.home_team.team_name.title() if matchup.home_score < matchup.away_score else matchup.away_team.team_name.title()
    }
    for matchup in scoreboard
    ]

    cols = ['Team', 'Owner', 'Score', 'Wins', 'Losses']
    # Updating Wins and Losses based on this week's result
    for matchup_dict in scoreboard_list_of_dicts:
        if matchup_dict['Winner'] == matchup_dict['Home_Team']:
            for col in cols:
                matchup_dict['Winning_' + col] = str(matchup_dict['Home_' + col])
                matchup_dict['Losing_' + col] = str(matchup_dict['Away_' + col])
        else:
            for col in cols:
                matchup_dict['Winning_' + col] = str(matchup_dict['Away_' + col])
                matchup_dict['Losing_' + col] = str(matchup_dict['Home_' + col])

    scoreboard_df = pd.DataFrame(scoreboard_list_of_dicts)
    scoreboard_df = scoreboard_df[['Winning_' + col for col in cols] + ['Losing_' + col for col in cols]]
    return scoreboard_df

### Transaction Parsers 

# use for all
def parse_team1_abbrev(text):
    return text.split(' ')[0]

# use for trades
def parse_team2_abbrev(text):
    return text.split(' to ')[1].split('.')[0]

# use for trades
def parse_trade_team1_players(text):
    team1 = parse_team1_abbrev(text)
    players = [x.split(',')[0] for x in text.split(team1 + ' traded ')[1:]]
    return ', '.join(players)

# use for trades
def parse_trade_team2_players(text):
    team2 = parse_team2_abbrev(text)
    players = [x.split(',')[0] for x in text.split(team2 + ' traded ')[1:]]
    return ', '.join(players)

# use for adds and add/drops
def parse_added_player(text):
    return text.split(' added ')[1].split(',')[0]

# use for drops and add/drops
def parse_dropped_player(text):
    return text.split(' dropped ')[1].split(',')[0]

# use for adds and add/drops
def parse_added_player_position(text):
    return text.split(' added ')[1].split(' from ')[0].split(' ')[-1].replace('D/ST', '')

# use for drops and add/drops
def parse_dropped_player_position(text):
    return text.split(' dropped ')[1].split(' to ')[0].split(' ')[-1].replace('D/ST', '')

def parse_waiver_bid(text):
    return text.split(' for ')[1].replace('.', '')

### End of transactions parsers

def clean_abbrev(abbrev):
    clean = abbrev.replace('stdy', 'JOSE')
    clean = clean.replace('Slon', 'SLON')
    clean = clean.replace('ARTE', 'AA')
    return clean

# Run every minute - Gives new transactions for current day through 1 month before. Returns None if no new transactions.
def get_transactions_df(league_id, year, abbrevs):
    # Get all transactions from current day through 1 month before
    current_date = datetime.now().date()
    current_date_string = current_date.strftime("%Y%m%d")
    last_month_date = current_date - timedelta(days=30)
    last_month_date_string = last_month_date.strftime("%Y%m%d")
    url = 'http://games.espn.com/ffl/recentactivity?leagueId=' + str(league_id) + '&seasonId=' + str(year) + '&activityType=2&startDate=' + str(last_month_date_string) + '&endDate=' + str(current_date_string) + '&teamId=-1&tranType=-2'
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.select_one('table.tableBody')
    trs = table.find_all('tr')
    headers = ['Datetime', 'Transaction', 'Description']
    rows = []
    for tr in trs[2:]:
        rows.append([])
        for td in tr:
            try:
                rows[-1].append(td.text)
            except:
                pass
    rows = [x[:-1] for x in rows]
    for x in rows:
        x[0] = datetime.strptime(x[0] + str(year), '%a, %b %d%I:%M %p%Y')
        x[1] = clean_abbrev(x[1].split('\xa0\xa0')[1].replace('(By LM)', '').replace(' (Waivers)', ''))
        x[2] = clean_abbrev(x[2].split(' ')[0]) + ' ' + clean_abbrev(' '.join(x[2].split(' ')[1:]).replace('*', ''))
        if 'Trade' in x[1]:
            for abbrev in abbrevs:
                x[1] = x[1].replace(abbrev + ' ', '')
                x[2] = x[2].replace(abbrev, abbrev + '. ')
                x[2] = x[2].replace(abbrev[0] + '. ' + abbrev[1:], abbrev)
            x[2] = x[2].replace('.  ', ' ').strip(' ')
        else:
            for abbrev in abbrevs:
                x[1] = x[1].replace(abbrev + ' ', '')
                x[2] = x[2].replace(abbrev, '. ' + abbrev)
            x[2] = x[2][2:] + '.'
    transactions_df = pd.DataFrame.from_records(rows, columns=headers)
    past_transactions_csv_fn = 'past_transactions.csv'
    
    # Reference past transactions csv
    past_transactions_df = pd.read_csv(past_transactions_csv_fn, parse_dates=['Datetime'], index_col=False)

    # Only keep new transactions
    transactions_df_merged_with_indicator = transactions_df.merge(past_transactions_df.drop_duplicates(), how='left', indicator=True)
    transactions_df = transactions_df_merged_with_indicator[transactions_df_merged_with_indicator['_merge'] == 'left_only']

    if transactions_df.empty:
        return None
    else:
        pd.options.mode.chained_assignment = None
        transactions_df['Team1'] = transactions_df.apply(lambda x: parse_team1_abbrev(x.Description), axis=1)
        transactions_df['Team2'] = transactions_df.apply(lambda x: parse_team2_abbrev(x.Description) if 'Trade' in x.Transaction else np.NaN, axis=1)
        transactions_df['Team1_Traded_Players'] = transactions_df.apply(lambda x: parse_trade_team1_players(x.Description) if 'Trade' in x.Transaction else np.NaN, axis=1)
        transactions_df['Team2_Traded_Players'] = transactions_df.apply(lambda x: parse_trade_team2_players(x.Description) if 'Trade' in x.Transaction else np.NaN, axis=1)
        transactions_df['Added_Player'] = transactions_df.apply(lambda x: parse_added_player(x.Description) if 'Add' in x.Transaction else np.NaN, axis=1)
        transactions_df['Added_Player_Position'] = transactions_df.apply(lambda x: parse_added_player_position(x.Description) if 'Add' in x.Transaction else np.NaN, axis=1)
        transactions_df['Dropped_Player'] = transactions_df.apply(lambda x: parse_dropped_player(x.Description) if 'Drop' in x.Transaction else np.NaN, axis=1)
        transactions_df['Dropped_Player_Position'] = transactions_df.apply(lambda x: parse_dropped_player_position(x.Description) if 'Drop' in x.Transaction else np.NaN, axis=1)
        transactions_df['Is_Waiver'] = transactions_df.apply(lambda x: 1 if ' for $' in x.Description else 0, axis=1)
        transactions_df['Waiver_Bid'] = transactions_df.apply(lambda x: parse_waiver_bid(x.Description) if x.Is_Waiver else np.NaN, axis=1)

        # Use these new transactions to append to past transactions csv
        partial_transactions_df = transactions_df[['Datetime', 'Transaction', 'Description']]
        past_transactions_df = pd.concat([partial_transactions_df, past_transactions_df])
        past_transactions_df.to_csv(past_transactions_csv_fn, index=False)
        return transactions_df

# End of currently used functions

# Not currently used
# Run this on Tuesday (once standings have been updated, not sure what time ESPN does this)
def get_standings_df(league_id, year):
    url = 'http://games.espn.com/ffl/standings?leagueId=' + str(league_id) + '&seasonId=' + str(year)
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.select_one('#xstandTbl_div0')
    trs = [tr for tr in table.find_all('tr')]
    headers = [td.text.title() if td.text not in ['PF', 'PA'] else td.text for td in trs[1]]
    headers = [header if header!='Div' else 'Overall' for header in headers]
    headers[0] = 'Team'
    headers.insert(1, 'Owner')
    rows = [[td.text for td in tr] for tr in trs][2:]
    for row in rows:
        team_and_owner = row[0].title()
        team, owner_raw = team_and_owner.split(' (')
        owner = clean_owner(owner_raw.strip(')'))
        row[0] = team
        row.insert(1, owner)
    standings_df = pd.DataFrame.from_records(rows, columns=headers)
    return standings_df

# Not currently used
# Mostly a helper, could do a report using this once a week if you want to
def get_budget_df(league_id):
    url = 'http://games.espn.com/ffl/tools/waiverorder?leagueId=' + str(league_id)
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.select_one('table.tableBody')
    trs = table.find_all('tr')
    headers = ['Team', 'Owner', 'Position', 'Remaining_Budget']
    rows = []
    for tr in trs[2:]:
        rows.append([])
        for td in tr:
            try:
                rows[-1].append(td.text.title().replace('\xa0', ''))
            except:
                pass
    budget_df = pd.DataFrame.from_records(rows, columns=headers)
    return budget_df

# Not currently used
# Run every morning. Will return None if no Free Agent Auction moves were made for the day.
def get_faa_df(league_id):
    # Check date
    current_date_string = datetime.now().strftime("%A, %B %d, %Y")
    url = 'http://games.espn.com/ffl/waiverreport?leagueId=' + str(league_id)
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    date_string = soup.select_one('em').text

    if date_string != current_date_string:
        return None

    table = soup.select_one('table.tableBody')
    trs = table.find_all('tr')
    headers = ['Order', 'Team', 'Player', 'Bid', 'Result', 'Note']
    rows = []
    for tr in trs[2:]:
        try:
            elements = [x.strip('. ').replace('*', '') for x in tr.text.split('\n')]
            elements.remove('')
            elements[0] = '' if elements[0] == '\xa0' else elements[0]
            elements[1] = elements[1].title()
            trans_type = 'Added' if 'Added' in elements[3] else 'Unsuccessful'
            elements.insert(-1, elements[-1].split(trans_type)[0])
            elements.insert(-1, trans_type)
            elements.insert(-1, elements[-1].split(trans_type)[1].replace('.', '').replace('\xa0', '').replace('Reason: ', ''))
            elements = elements[:-1]
            rows.append(elements)
        except:
            pass
    faa_df = pd.DataFrame.from_records(rows, columns=headers)
    # add remaining budgets
    budget_df = get_budget_df(league_id=league_id)
    faa_df = faa_df.merge(budget_df[['Team', 'Remaining_Budget']], on='Team', how='left')
    return faa_df
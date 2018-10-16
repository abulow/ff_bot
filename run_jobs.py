from datetime import datetime, timedelta
import time
from ff_bot import *
from config.league_settings import *

def run():
    scoreboard_start_times = [first_scoreboard_start_time + timedelta(weeks=i) for i in range(16) if (first_scoreboard_start_time + timedelta(weeks=i)) > datetime.now()]
    week_nums = {x: str(idx+1) for idx, x in enumerate(scoreboard_start_times)}
    while datetime.now() < end_of_season:
        run_bot('transactions')
        first_remaining_scoreboard_start_time = scoreboard_start_times[0]
        if scoreboard_start_times and (datetime.now() > first_remaining_scoreboard_start_time):
            week_num = week_nums[first_remaining_scoreboard_start_time]
            run_bot('scores', week_num=week_num)
            scoreboard_start_times = scoreboard_start_times[1:]
        time.sleep(60)

if __name__ == '__main__':
    while True:
        try:
            print('Run started, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            run()
            print('Run stopped, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            break
        except Exception as e:
            print()
            print('An error occured, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            print(e)
            print()
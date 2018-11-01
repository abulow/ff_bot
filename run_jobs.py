from datetime import datetime, timedelta
import time
from ff_bot import *
from config.league_settings import *

def run():
    scoreboard_start_times = [first_scoreboard_start_time + timedelta(weeks=i) for i in range(16)]
    week_nums = {x: str(idx+1) for idx, x in enumerate(scoreboard_start_times)}
    remaining_scoreboard_start_times = [x for x in scoreboard_start_times if x > datetime.now()]
    while datetime.now() < end_of_season:
        run_bot('transactions')
        if remaining_scoreboard_start_times and (datetime.now() > remaining_scoreboard_start_times[0]):
            week_num = week_nums[remaining_scoreboard_start_times[0]]
            run_bot('scores', week_num=week_num)
            remaining_scoreboard_start_times = remaining_scoreboard_start_times[1:]
        print()
        print('Updated, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
        time.sleep(60)

if __name__ == '__main__':
    while True:
        try:
            print('Run started, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            run()
            print()
            print('Run stopped, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            break
        except Exception as e:
            print()
            print('An error occured, Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
            print(e)
            time.sleep(60)
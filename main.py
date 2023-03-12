import schedule
import time
import parser
import ps_parser2

schedule.every().day.at('12:00').do(parser.parse)
schedule.every().day.at('12:00').do(ps_parser2.parsing)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)

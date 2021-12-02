import argparse
import time

from apscheduler.schedulers.blocking import BlockingScheduler

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scheduler = BlockingScheduler()

def job():
    print(f"Job start at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://familyweb.wistron.com/whrs/login.aspx")
    
    input_employ_id = driver.find_element_by_id("userpass")
    input_employ_id.send_keys(args.employ_id)
    input_employ_id.send_keys(Keys.ENTER)

    input_symptom = driver.find_element_by_id("symptom1")
    input_symptom.click()

    input_commute_way = driver.find_element_by_id("commute_way1")
    input_commute_way.click()

    input_submit = driver.find_element_by_id("btn")
    input_submit.click()
    driver.close()
    print("Job done")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--employ_id", type=str)
    parser.add_argument("--hour", default=9, help="which hour to trigger job (0-23) default=9", type=int)
    parser.add_argument("--minute", default=0, help="which minute to trigger job (0-59) default=0", type=int)
    args = parser.parse_args()
    scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=args.hour, minute=args.minute)
    scheduler.start()

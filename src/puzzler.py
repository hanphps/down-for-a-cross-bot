from selenium import webdriver
import requests
import utils
import time
import random
class Puzzler:

    def __init__(self):
        self._session = None
        self._curr_req = None

    def get_puzzle(self,cross_type: str,cross_date: str)->list:
        return_list = []
        puzzle_list = requests.get(url=utils.DOWN_API).json()
        puzzles = puzzle_list['puzzles']

        if cross_type is not None:
            if cross_type != 'r':
                act_type = utils.MAPPING[cross_type]
                # Only get first 50 sadly
                for id in range(0,len(puzzles)):
                    if act_type.lower() in puzzles[id]['content']['info']['title'].lower():
                        if cross_date is not None and cross_date !='today':
                            act_date = utils.MAPPING[cross_date]
                            if act_date.lower() in puzzles[id]['content']['info']['title'].lower():
                                return_list.append([puzzles[id]['content']['info']['title'],puzzles[id]['pid']])
                        elif cross_date is not None and cross_date =='today':
                            if puzzles[id]['content']['info']['type'] == 'Daily Puzzle':
                                return_list.append([puzzles[id]['content']['info']['title'],puzzles[id]['pid']])
                                break
                        else:
                            return_list.append([puzzles[id]['content']['info']['title'],puzzles[id]['pid']])

            else:
                id = random.randint(0,len(puzzles))
                return_list.append([puzzles[id]['content']['info']['title'],puzzles[id]['pid']])
        
        return return_list

    def create_puzzle(self,pid: str)->str:
        return_str = ''
        self._session = webdriver.Firefox()
        self._curr_req = utils.REQUEST+pid

        req = self._session.get(self._curr_req)
        wait_time = 0
        redirected = True

        while self._session.current_url == self._curr_req:
            time.sleep(utils.REFRESHTIME)
            wait_time += utils.REFRESHTIME
            print('Waiting for response')
            if wait_time > utils.TIMEOUT:
                redirected = False
                return_str = 'Puzzle loading timed out. Please try again'
                raise Exception('Puzzle loading timed out')
        if redirected:
            return_str = self._session.current_url
        
        self._session.quit()
        self._curr_req = None
        return return_str

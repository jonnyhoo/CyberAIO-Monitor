import re
import json
import requests
import threading
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from discord_hooks import Webhook
import discord
from user_agent import generate_user_agent
import time

def cyber():
    cycle = 0
    while cycle == 0:
        headers = {
            'authority': 'www.cybersole.io',
            'upgrade-insecure-requests': '1',
            'user-agent': generate_user_agent(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }


        soup = BeautifulSoup(requests.get('https://www.cybersole.io/', headers=headers, proxies=dict(https='LOGIN:PASS@IP:PORT')).text, 'lxml')

        try:
            if soup.find('button', id='purchase-btn').text.strip() == 'Sold Out | Windows Only | £200*':
                sleep(15)
                cyber()
            else:
                print(soup.find('button', id='purchase-btn').text.strip())
                get_cyber()
        except:
            get_cyber()
            
            
if __name__ == '__main__':
    cyber()

import os, wave, struct
import json
import logging
from dotenv import load_dotenv
from dotenv import find_dotenv
import requests

load_dotenv()

SMARTY_API_KEY = os.getenv('SMARTY_API_KEY')
from bardapi import Bard
from dotenv import load_dotenv
import os

load_dotenv()


# _BARD_API_KEY = 'bAgmWDRQutzKGpDHgJVcCu5903xSGRD2oSRNDTz4tpsBphfS0jeAczvsgFNI9G1UBO89Hg.'

def call_bard(query):
    bard = Bard()
    answer = bard.get_answer(query)
    return (answer['content'])


print(call_bard('were?'))

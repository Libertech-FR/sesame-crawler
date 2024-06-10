import asyncio
import base64
import logging
import os
from dotenv import load_dotenv
import hashlib
from datetime import datetime

from src.a_moins_b import a_moins_b
from src.export_ind import export_ind
from src.import_ind import import_ind

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)
load_dotenv()

basic_auth = [
    os.getenv('STC_API_USERNAME', ''),
    os.getenv('STC_API_PASSWORD', ''),
]
basic_auth = [value for value in basic_auth if value is not None]
joined_auth = ':'.join(map(str, basic_auth)).encode('utf-8')


url = f"{os.getenv('STC_API_BASEURL', 'https://taiga.archi.fr')}/taiga_libext/JsonRPC/api.php"
headers = {
    "Authorization": f"Basic {base64.b64encode(joined_auth).decode('utf-8')}",
    "Content-Type": "application/json; charset=utf-8",
}



async def main():

    print("Starting import_ind...")
    start_time = datetime.now()
    await import_ind()
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"import_ind completed in {execution_time}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

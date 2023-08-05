import logging
import pyrogram
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config



if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
        bot_token=5732190759:AAEJS6JREMSgkIDQZzU4oUHlz6AXzFprezk,
        api_id=14136462,
        api_hash=54391f1d451d5223e26fc28ac6c86a67,
        plugins=plugins
    )
    Config.AUTH_USERS.add(1571060413)
    app.run()

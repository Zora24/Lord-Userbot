import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Config as Config
else:
    from local_config import Development as Config


Config = Config

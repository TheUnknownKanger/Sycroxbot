import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as config
else:
    from localconfig import config


Var = config

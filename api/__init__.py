import os
import sys
import logging
import logging.config
from flask import Flask
from flasgger import Swagger


# configure app
app = Flask(__name__)
swagger = Swagger(app)

dotenv_path = os.path.join(os.getcwd(), '.env')
if os.path.isfile(dotenv_path):
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)

app.config.from_object(os.environ.get('CONFIG_OBJECT'))

# config log handler
handler = logging.StreamHandler(sys.stdout)

if not app.debug:
    handler = logging.handlers.SysLogHandler(address='/dev/log')

formatter = logging.Formatter(
    '{"timestamp": "%(asctime)s",'
    '"level": "%(levelname)s",'
    '"message": "%(message)s"'
    '"path": "%(pathname)s"'
    '"line": "%(lineno)d"}'
)
handler.setFormatter(formatter)

log = logging.getLogger(os.environ.get("LOGGER_NAME", __name__))
log.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
log.addHandler(handler)

import os
import json
from api import app as application


@application.route('/')
def index():
    return json.dumps({'message': 'KABUM!'})


if __name__ == '__main__':
    application.run(debug=application.debug,
                    host=os.environ.get('HOST', '0.0.0.0'),
                    port=int(os.environ.get('PORT', 5000)))

import os
import json
from api import app as application
from api.v1.resources import CalculaFreteView as v1_Frete


application.add_url_rule(
    '/v1/frete',
    view_func=v1_Frete.as_view('frete'),
    methods=['POST']
)


@application.route('/')
def index():
    return json.dumps({'message': 'KABUM!'})


if __name__ == '__main__':
    application.run(debug=application.debug,
                    host=os.environ.get('HOST', '0.0.0.0'),
                    port=int(os.environ.get('PORT', 5000)))

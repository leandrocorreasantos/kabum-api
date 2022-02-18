from api import log
from flask import request
from flask.views import MethodView
from api.utils import calcula_frete
from api.v1.schema import (
    FreteSchema,
    PackageDataSchema,
    EmptyDataSchema,
    ValidationErrorSchema,
)


class CalculaFreteView(MethodView):
    def post(self):
        schema = FreteSchema()
        schema.many = True
        data = request.get_json()
        if not data:
            return EmptyDataSchema().build()

        log.info("data: {}".format(data))

        try:
            pacote = PackageDataSchema().load(data)
        except Exception as e:
            log.error("Validation error: {}".format(e))
            return ValidationErrorSchema().build(e.messages)

        log.info("pacote: {}".format(pacote))
        log.info("dimensao: {}".format(pacote["dimensao"]))
        log.info("largura: {}".format(pacote["dimensao"]["largura"]))

        fretes = calcula_frete(
            pacote["dimensao"]["largura"],
            pacote["dimensao"]["altura"],
            pacote["peso"]
        )

        return FreteSchema().build(fretes)

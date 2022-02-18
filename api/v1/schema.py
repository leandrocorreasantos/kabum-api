from http.client import (
    OK,
    BAD_REQUEST
)
from flask import jsonify
from marshmallow import Schema, fields


class DefaultSchema(Schema):
    @classmethod
    def build(cls, data):
        many = False
        if type(data) == list:
            many = True
        return jsonify(cls(many=many).dump(data)), OK.value


class MedidaSchema(Schema):
    altura = fields.Float(required=True)
    largura = fields.Float(required=True)


class PackageDataSchema(DefaultSchema):
    dimensao = fields.Nested(MedidaSchema, required=True)
    peso = fields.Float(required=True)


class FreteSchema(DefaultSchema):
    nome = fields.String()
    valor_frete = fields.Float()
    prazo_entrega = fields.Integer()


class EmptyDataSchema(DefaultSchema):
    message = fields.String(default="Empty Data")
    code = fields.Integer(default=BAD_REQUEST)
    description = fields.String(default="Request data is empty")

    @classmethod
    def build(cls):
        return jsonify(cls().dump({})), BAD_REQUEST.value


class BadRequestSchema(EmptyDataSchema):
    message = fields.String(default="Bad Request")
    description = fields.String(default="Bad Request")


class ValidationErrorSchema(Schema):

    @classmethod
    def build(cls, messages):
        return jsonify(messages), BAD_REQUEST.value

from flask_restx import Namespace, Resource
from resources.examples.models import ExampleModel

api = Namespace("examples", description="サンプル")

_example_model = ExampleModel(api)


@api.route("")
class ExamplesResource(Resource):
    @api.doc(description="取得APIサンプル")
    @api.marshal_with(_example_model.example_get_response_model())
    def get(self):  # noqa: ANN201
        """取得APIサンプル"""
        pass

    @api.doc(description="登録APIサンプル")
    @api.expect(_example_model.example_post_request_model())
    @api.response(201, "登録成功")
    def post(self):  # noqa: ANN201
        """登録APIサンプル"""
        pass


@api.route("/<int:example_id>")
class ExampleResource(Resource):
    @api.doc(description="更新APIサンプル")
    @api.expect(_example_model.example_put_request_model(), validate=True)
    @api.response(204, "更新成功")
    def put(self, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        pass

    @api.doc(description="更新APIサンプル")
    @api.expect(_example_model.example_patch_request_model(), validate=True)
    @api.response(204, "更新成功")
    def patch(self, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        pass

    @api.doc(description="削除APIサンプル")
    @api.response(204, "削除成功")
    def delete(self, example_id: int):  # noqa: ANN201
        """削除APIサンプル"""
        pass

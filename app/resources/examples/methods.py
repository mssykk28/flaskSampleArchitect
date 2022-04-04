from db.connection import db_connection
from db.repositories import example_repository
from flask_restx import Namespace, Resource
from resources.examples.models import ExampleModel
from sqlalchemy.orm import Session

api = Namespace("examples", description="サンプル")

_example_model = ExampleModel(api)


@api.route("")
class Examples(Resource):
    @db_connection()
    @api.doc(description="取得APIサンプル")
    @api.marshal_list_with(_example_model.example_get_response_model())
    def get(self, db_session: Session):  # noqa: ANN201
        """取得APIサンプル"""
        return example_repository.find_all(db_session)

    @db_connection()
    @api.doc(description="登録APIサンプル")
    @api.expect(_example_model.example_post_request_model())
    @api.response(201, "登録成功")
    def post(self, db_session: Session):  # noqa: ANN201
        """登録APIサンプル"""
        example_repository.create(db_session, api.payload)
        return "登録成功", 201


@api.route("/<int:example_id>")
class Example(Resource):
    @db_connection()
    @api.doc(description="詳細取得APIサンプル")
    @api.marshal_with(_example_model.example_get_response_model())
    def get(self, db_session: Session, example_id: int):  # noqa: ANN201
        """詳細取得APIサンプル"""
        return example_repository.find_by_id(db_session, example_id)

    @db_connection()
    @api.doc(description="更新APIサンプル")
    @api.expect(_example_model.example_put_request_model(), validate=True)
    @api.response(204, "更新成功")
    def put(self, db_session: Session, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        example = example_repository.find_by_id(db_session, example_id)
        example_repository.update(db_session, example, api.payload)
        return "更新成功", 204

    @db_connection()
    @api.doc(description="更新APIサンプル")
    @api.expect(_example_model.example_patch_request_model(), validate=True)
    @api.response(204, "更新成功")
    def patch(self, db_session: Session, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        example = example_repository.find_by_id(db_session, example_id)
        example_repository.update(db_session, example, api.payload)
        return "更新成功", 204

    @db_connection()
    @api.doc(description="削除APIサンプル")
    @api.response(204, "削除成功")
    def delete(self, db_session: Session, example_id: int):  # noqa: ANN201
        """削除APIサンプル"""
        example_repository.delete(db_session, example_id)
        return "削除成功", 204

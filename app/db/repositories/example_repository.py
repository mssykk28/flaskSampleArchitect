from typing import List

from db.entities.example import Example


def find_all(db_session) -> List[Example]:
    return db_session.query(Example).all()


def create(db_session, payload) -> Example:
    example = Example(
        example_string=payload.get("example_string"),
        example_number=payload.get("example_number"),
        example_datetime=payload.get("example_datetime"),
        example_boolean=payload.get("example_boolean"),
    )
    db_session.add(example)
    db_session.commit()
    return example


def find_by_id(db_session, example_id) -> Example:
    return db_session.query(Example).filter(Example.id == example_id).one_or_none()


def update(db_session, example, payload):
    db_session.query(Example).filter(Example.id == example.id).update(payload)
    db_session.commit()
    return example


def delete(db_session, example_id):
    db_session.query(Example).filter(Example.id == example_id).delete()

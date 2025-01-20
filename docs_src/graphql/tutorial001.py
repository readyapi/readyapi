import strawberry
from readyapi import ReadyAPI
from strawberry.readyapi import GraphQLRouter


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQLRouter(schema)

app = ReadyAPI()
app.include_router(graphql_app, prefix="/graphql")

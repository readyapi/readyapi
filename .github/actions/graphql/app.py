#! usr/bin/python

from database import db_session
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True, context={"session": db_session}
    ),
)


@app.route("/")
def index():
    return "Go to /graphql"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7779)
" "

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import engine, db_session, User as UserModel
from database import Thing as ThingModel
from sqlalchemy.sql import text
import graphene.types.datetime
import database


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Things(SQLAlchemyObjectType):
    class Meta:
        model = ThingModel
        interfaces = (relay.Node, )


# Used to Create New User
class createUser(graphene.Mutation):
    user = graphene.Field(Users)
    ok = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        username = graphene.String()

    def mutate(root, info, email, name, username):
        user = UserModel(name=name, email=email, username=username)
        # db_session.add(user)
        # db_session.commit()

        with engine.connect() as con:
            statement = text(
                "insert into users (name, email, username) "
                f"values ('{name}', :email, :username)")
            
            con.execute(statement, {'email': email, 'username': username})

        ok = True
        return createUser(user=user, ok=ok)


# Used to Change Username with Email
class changeUsername(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(Users)

    def mutate(root, info, username, email):
        query = Users.get_query(info)
        user = query.filter(UserModel.email == email).first()
        user.username = username
        db_session.commit()
        ok = True

        return changeUsername(user=user, ok=ok)


class deleteUser(graphene.Mutation):
    user = graphene.Field(Users)
    ok = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(root, info, email):
        query = Users.get_query(info)
        user = query.filter(UserModel.email == email).first()
        db_session.delete(user)
        db_session.commit()
        ok = True

        return deleteUser(user=user, ok=ok)


class createThing(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        string = graphene.String()
        boolean = graphene.Boolean()
        date = graphene.types.datetime.DateTime()
        datetime = graphene.types.datetime.DateTime()
        floaty = graphene.Float()
        integer = graphene.Int()
        # arrayString = graphene.List(graphene.String)

    ok = graphene.Boolean()
    thing = graphene.Field(Things)

    def mutate(root, info, text, string, boolean, date, datetime, floaty, integer):

        thing = ThingModel(
            boolean=boolean,
            text=text,
            string=string, 
            date=date, 
            datetime=datetime, 
            floaty=floaty, 
            integer=integer)
        
        db_session.add(thing)
        db_session.commit()
        ok = True

        return createThing(thing=thing, ok=ok)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    user = SQLAlchemyConnectionField(Users)
    find_user = graphene.Field(lambda: Users, username=graphene.String())
    all_users = SQLAlchemyConnectionField(Users)

    thing = SQLAlchemyConnectionField(Things)
    # find_thing = graphene.Field(lambda: Things, username=graphene.String())
    all_things = SQLAlchemyConnectionField(Things)

    def resolve_find_user(root, info, username):
        query = Users.get_query(info)
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        return query.filter(UserModel.username == username).first()


class MyMutations(graphene.ObjectType):
    create_user = createUser.Field()
    delete_user = deleteUser.Field()
    change_username = changeUsername.Field()
    create_thing = createThing.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations, types=[Users, Things])

# end

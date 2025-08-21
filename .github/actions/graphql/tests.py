#!/usr/bin/env python

"""Example automated test script for flask_rest_target

This example automated test/unittest uses pytest.  With
the pytest-peach module this test script can be used
with Peach Web Proxy.

  pytest test_target.py --peach=auto

"""

import os

from requests import post

# HTTP target
target = os.getenv("TARGET_URL", "http://127.0.0.1:7779") + "/graphql"
req_args = {
    # verify disabled server TLS cert verification
    "verify": False,
    # our example can use client cert auth, this sets our user cert.
    # 'cert' : (cert_dir % 'client-cert.pem', cert_dir % 'client-key.pem'),
    "headers": {
        # our example requires an API token for authentication.
        "Authorization": "Token b5638ae7-6e77-4585-b035-7d9de2e3f6b3"
    },
}


def setup_function(self):
    """
    Setup the test by clearing out created users.
    """
    pass


def teardown_function(self):
    """
    Teardown test by clearing out created users.
    """

    body = {
        "query": """
mutation {
  deleteUser(email: "hello@abc.com") {
    user {
      id,
      name,
      email,
      username
    }
  }
}
        """
    }

    post(target, json=body, **req_args)


def test_users_findUser():
    body = {
        "query": """
{
  findUser(username:"mike") {
    edges {
      node {
        name,
        email,
        username
      }
    }
  }
}
        """
    }

    post(target, json=body, **req_args)


def test_thing_create():
    # application/json
    body = {
        "query": """
mutation {
  createThing(
    text: "text",
    string: "string",
    date: "2017-01-10T21:33:15.233Z",
      datetime: "2017-01-10T21:33:15.233Z",
      myenum: one,
      floaty: 0.777,
      integer: 42,
      arrayString: ["one", "two", "three"])
  {
    thing{
      text, date, datetime
    }
  }
}
"""
    }

    r = post(target, json=body, **req_args)

    user = r.json()
    print(user)


def test_user_create():
    # application/json
    body = {
        "query": """
mutation {
  createUser(name: "abc", email: "hello@abc.com", username: "abc") {
    user {
      id,
      name,
      email,
      username
    }
  }
}
"""
    }

    r = post(target, json=body, **req_args)

    user = r.json()
    print(user)


def test_users_getall():
    body = {
        "query": """
{
  allUsers {
    edges {
      node {
        name,
        email,
        username
      }
    }
  }
}
        """
    }

    post(target, json=body, **req_args)


def test_user_update():
    # application/json
    body = {
        "query": """
mutation {
  changeUsername(email: "hello@abc.com", username: "abcd") {
    user {
      id,
      name,
      email,
      username
    }
  }
}
        """
    }

    r = post(target, json=body, **req_args)

    user = r.json()
    print(user)


if __name__ == "__main__":
    print()
    print("This script is intended to be run using pytest module.")
    print("Please see README for more information.")
    print()
    print("Example usage with pytest and pytest-peach:")
    print()
    print("  pytest test_target.py --peach=on")
    print()

# end

from readyapi import ReadyAPI

app = ReadyAPI()

@app.get("/efficiency/fstrings")
async def fstrings_demo():
    """
    Endpoint demonstrating f-strings versus older string formatting methods in Python.
    """
    name = "world"
    percent_format = "%% formatting: Hello, %s!" % name
    str_format = "str.format(): Hello, {}!".format(name)
    f_string = f"f-string: Hello, {name}!"

    return {
        "percent_format": percent_format,
        "str_format": str_format,
        "f_string": f_string,
        "note": "F-strings (since Python 3.6) are faster and more readable than older formatting methods."
    }

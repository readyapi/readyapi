import pytest
from readyapi import BackgroundTasks, ReadyAPI
from readyapi.testclient import TestClient

app = ReadyAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

client = TestClient(app)

def test_send_notification():
    response = client.post("/send-notification/test@example.com")
    assert response.status_code == 200
    assert response.json() == {"message": "Notification sent in the background"}

    with open("log.txt", mode="r") as email_file:
        content = email_file.read()
        assert content == "notification for test@example.com: some notification"

def test_send_notification_edge_case():
    response = client.post("/send-notification/")
    assert response.status_code == 422

def test_send_notification_error_handling():
    def faulty_task():
        raise ValueError("An error occurred")

    app = ReadyAPI()

    @app.post("/send-faulty-notification")
    async def send_faulty_notification(background_tasks: BackgroundTasks):
        background_tasks.add_task(faulty_task)
        return {"message": "Faulty notification sent in the background"}

    client = TestClient(app)
    response = client.post("/send-faulty-notification")
    assert response.status_code == 200
    assert response.json() == {"message": "Faulty notification sent in the background"}

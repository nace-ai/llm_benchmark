from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        response = self.client.post("/v1/auth/jwt/exchange", json={
            "provider": "test",
            "type": "oauth",
            "access_token": "any"
        }, headers={
            "Accept": "application/json"   
        })
        response.raise_for_status()
        login = response.json()
        token = login["jwt_token"]
        team_id = login["user"]["id"]
        response = self.client.get("/v1/profile", headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
        # print("Response status code:", response.status_code)
        # print("Response text:", response.text)

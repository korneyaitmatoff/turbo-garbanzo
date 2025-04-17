from locust import FastHttpUser, task


class WebsiteUser(FastHttpUser):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """

    host = "http://127.0.0.1:8081"

    @task
    def get(self):
        self.client.get("/")

    @task
    def report(self):
        self.client.get("/report")

    @task
    def get_by_id(self):
        self.client.get("/26af75cd-0641-4300-8056-506cba025d55")

    @task
    def post(self):
        self.client.post("/", data={
            "name": "string",
            "cost": 0,
            "is_writeoff": True,
            "is_rented": True
        })

    @task
    def put(self):
        self.client.put("/26af75cd-0641-4300-8056-506cba025d55",
                        data={
                            "name": "string",
                            "cost": 0,
                            "is_writeoff": True,
                            "is_rented": True
                        })

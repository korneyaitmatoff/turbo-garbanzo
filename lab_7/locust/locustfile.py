import math

from locust import HttpUser, LoadTestShape, TaskSet, constant, task

from os import environ


class WebsiteUser(TaskSet):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """

    host = environ.get("API_HOST", "http://127.0.0.1:8081")

    @task
    def get(self):
        self.client.get("/")

    @task
    def report(self):
        self.client.get("/report/")

    @task
    def post(self):
        self.client.post("/", body={
            "name": "test_car",
            "cost": 10,
            "is_writeoff": True,
            "is_rented": True
        })


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [WebsiteUser]


class DoubleWave(LoadTestShape):
    """
    A shape to imitate some specific user behaviour. In this example, midday
    and evening meal times. First peak of users appear at time_limit/3 and
    second peak appears at 2*time_limit/3

    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    min_users = 1
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                    (self.peak_one_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                    + (self.peak_two_users - self.min_users)
                    * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                    + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None

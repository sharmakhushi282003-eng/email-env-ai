from models import EmailObservation, EmailAction
from grader_easy import grade_easy

class EmailEnv:

    def __init__(self):
        self.state = "new_email"

    def reset(self):
        self.state = "new_email"
        return EmailObservation(message="New email received")

    def step(self, action: EmailAction):
        reward = grade_easy(action.action)
        done = True

        obs = EmailObservation(message="Action taken")
        return obs, reward, done, {}

    def state(self):
        return self.state

class EmailEnv:

    def reset(self):
        return {"message": "New email task"}

    def step(self, action_dict):
        return {"reward": 0.5, "done": True}

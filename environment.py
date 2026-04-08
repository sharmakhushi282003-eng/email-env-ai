def step(self, action_dict):
    action = action_dict.get("action", "ignore")

    # simple internal tasks mapping
    if self.current_task == 1:
        reward = 0.8 if action == "reply" else 0.3
    elif self.current_task == 2:
        reward = 0.7 if action == "ignore" else 0.2
    else:
        reward = 0.9 if action == "reply" else 0.4

    done = True

    return {
        "reward": reward,
        "done": done
    }
def reset(self):
    if not hasattr(self, "current_task"):
        self.current_task = 1
    else:
        self.current_task += 1
        if self.current_task > 3:
            self.current_task = 1

    return {
        "message": f"Email task {self.current_task}"
    }

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

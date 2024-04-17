import gym

# Make sure to specify the render mode when creating the environment
env = gym.make("ALE/Breakout-v5", render_mode='human')

state = env.reset()
terminated = False
truncated = False

while not terminated and not truncated:
    action = env.action_space.sample()
    state, reward, terminated, truncated, info = env.step(action)  #unpack values here
    print(state)
    if terminated:
        print("Game Over: Terminated")
        state = env.reset()  # Reset the environment for new episode
    elif truncated:
        print("Game Over: Truncated")
        state = env.reset()  # Reset the environment if truncated before natural termination

env.close()

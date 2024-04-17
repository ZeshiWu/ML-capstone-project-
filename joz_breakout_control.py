import gym

# Initialize the environment with rendering
env = gym.make("ALE/Breakout-v5", render_mode='human')
state = env.reset()
terminated = False
truncated = False

while not terminated and not truncated:
    # Display the current state to the user
    env.render()

    # Get action from user input
    action = input("Enter your action (0 for 'no movement', 1 for 'fire', 2 for 'move right', 3 for 'move left'): ")
    action = int(action)  # Convert input to integer

    # Apply the action to the environment
    state, reward, terminated, truncated, info = env.step(action)
    
    if terminated:
        print("Game Over: Terminated")
        state = env.reset()  # Reset the environment for new episode
    elif truncated:
        print("Game Over: Truncated")
        state = env.reset()

env.close()


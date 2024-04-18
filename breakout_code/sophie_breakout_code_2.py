from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import VecFrameStack, VecNormalize
from stable_baselines3 import PPO
import gymnasium as gym 

# Define global variables
total_episodes = 0
cumulative_reward = 0
output_counter = 0

# PPO
class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
        self.file = open('training_output_detailed.txt', 'w')  # Open a file to write output

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self):
        global total_episodes, cumulative_reward, output_counter
        num_episodes = len(self.locals["rollout_buffer"].infos)
        total_episodes += num_episodes
        if num_episodes > 0:
            episode_rewards = [info['episode']['r'] for info in self.locals["rollout_buffer"].infos]
            average_reward = sum(episode_rewards) / num_episodes
            cumulative_reward += sum(episode_rewards)
            output_counter += 1
            output_str = f"Output {output_counter}: Average over {num_episodes} episodes - Reward: {average_reward}\n"
            print(output_str, end='')  # Print to console
            self.file.write(output_str)  # Write to file
        self.locals["rollout_buffer"].clear()

    def on_training_end(self):
        self.file.close()  # Close the file when training ends

# Environment setup
env = gym.make("ALE/Breakout-v5", render_mode='human')
env = Monitor(env)  # Wrap environment to track episode statistics
env = VecFrameStack(env, n_stack=4)  # Frame stacking
env = VecNormalize(env, norm_reward=False, clip_obs=1e6)  # Normalize observations

# Setup and train the model
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log="./PPOtensorboard/")
callback = CustomCallback()
model.learn(total_timesteps=int(5e5), callback=callback)

# Report overall averages
if total_episodes > 0:
    overall_average_reward = cumulative_reward / total_episodes
    print(f"Overall: Average Reward: {overall_average_reward}")

env.close()

#DQN
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
import gymnasium as gym

# Setup the environment and model
env = gym.make("ALE/Breakout-v5", render_mode='human')
model = DQN("CnnPolicy", env, verbose=1, tensorboard_log="./DQNtensorboard/")

import os

# Define the path to the output file relative to the script location
output_file = "model_output.txt"

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, output_file)

# Open the output file
with open(output_path, "w") as file:
    original_stdout = sys.stdout
    sys.stdout = file

    # Train the model
    model.learn(total_timesteps=int(5e5), progress_bar=True)

    # Restore stdout
    sys.stdout = original_stdout

# Evaluate the model's performance
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=100)
print(f"Mean reward: {mean_reward}, Std reward: {std_reward}")
print("Output written to:", output_file)


# -*- coding: utf-8 -*-
"""Frozen_lake.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12rZi29Ynhg0A-HwesahUU7nJx8CtDAS9
"""

from pathlib import Path
from typing import NamedTuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import categorical
import torch.distributions as distributions
from tqdm import tqdm
import imageio
import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map
from stable_baselines3 import DQN,PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Commented out IPython magic to ensure Python compatibility.
# Load the TensorBoard notebook extension
# %load_ext tensorboard
import subprocess

# Command to clean up DQN TensorBoard logs
subprocess.run(["find", "/content/DQNtensorboard/", "-type", "d", "-name", "DQN_*", "-exec", "rm", "-r", "{}", "+"])

# Command to clean up PPO TensorBoard logs
subprocess.run(["find", "/content/PPOtensorboard/", "-type", "d", "-name", "PPO_*", "-exec", "rm", "-r", "{}", "+"])

"""### 4x4 frozen lake map PPO - is_slippery off

"""
print("4x4 frozen lake map PPO - is_slippery off")

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym

# Define global variables
total_episodes = 0
cumulative_reward = 0
output_counter = 0

class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
        self.file = open('training_output_detailed.txt', 'w')  # Open a file to write output

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self):
        global total_episodes, cumulative_reward, output_counter
        num_episodes = len(self.model.ep_info_buffer)
        total_episodes += num_episodes
        if num_episodes > 0:
            episode_rewards = [info['r'] for info in self.model.ep_info_buffer]
            average_reward = sum(episode_rewards) / num_episodes
            cumulative_reward += sum(episode_rewards)
            output_counter += 1
            output_str = f"Output {output_counter}: Average over {num_episodes} episodes - Reward: {average_reward}\n"
            print(output_str, end='')  # Print to console
            self.file.write(output_str)  # Write to file
        self.model.ep_info_buffer.clear()

    def on_training_end(self):
        self.file.close()  # Close the file when training ends

# Environment setup
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array", map_name="4x4", desc=None)
env = Monitor(env)  # Wrap environment to track episode statistics
env = DummyVecEnv([lambda: env])  # Wrap env in DummyVecEnv for compatibility with SB3

# Setup and train the model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./PPOtensorboard/")
callback = CustomCallback()
model.learn(total_timesteps=int(5e5), callback=callback)

# Report overall averages
if total_episodes > 0:
    overall_average_reward = cumulative_reward / total_episodes
    print(f"Overall: Average Reward: {overall_average_reward}")

env.close()

"""###4x4 frozen lake map PPO - is_slippery on"""
print("4x4 frozen lake map PPO - is_slippery on")

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym

# Define global variables
total_episodes = 0
cumulative_reward = 0
output_counter = 0

class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
        self.file = open('training_output_detailed.txt', 'w')  # Open a file to write output

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self):
        global total_episodes, cumulative_reward, output_counter
        num_episodes = len(self.model.ep_info_buffer)
        total_episodes += num_episodes
        if num_episodes > 0:
            episode_rewards = [info['r'] for info in self.model.ep_info_buffer]
            average_reward = sum(episode_rewards) / num_episodes
            cumulative_reward += sum(episode_rewards)
            output_counter += 1
            output_str = f"Output {output_counter}: Average over {num_episodes} episodes - Reward: {average_reward}\n"
            print(output_str, end='')  # Print to console
            self.file.write(output_str)  # Write to file
        self.model.ep_info_buffer.clear()

    def on_training_end(self):
        self.file.close()  # Close the file when training ends

# Environment setup
env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="rgb_array", map_name="4x4", desc=None)
env = Monitor(env)  # Wrap environment to track episode statistics
env = DummyVecEnv([lambda: env])  # Wrap env in DummyVecEnv for compatibility with SB3

# Setup and train the model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./PPOtensorboard/")
callback = CustomCallback()
model.learn(total_timesteps=int(5e5), callback=callback)

# Report overall averages
if total_episodes > 0:
    overall_average_reward = cumulative_reward / total_episodes
    print(f"Overall: Average Reward: {overall_average_reward}")

env.close()

"""### 8x8 frozen lake map PPO - is_slippery off

"""
print("8x8 frozen lake map PPO - is_slippery off")

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym

# Define global variables
total_episodes = 0
cumulative_reward = 0
output_counter = 0

class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
        self.file = open('training_output_detailed.txt', 'w')  # Open a file to write output

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self):
        global total_episodes, cumulative_reward, output_counter
        num_episodes = len(self.model.ep_info_buffer)
        total_episodes += num_episodes
        if num_episodes > 0:
            episode_rewards = [info['r'] for info in self.model.ep_info_buffer]
            average_reward = sum(episode_rewards) / num_episodes
            cumulative_reward += sum(episode_rewards)
            output_counter += 1
            output_str = f"Output {output_counter}: Average over {num_episodes} episodes - Reward: {average_reward}\n"
            print(output_str, end='')  # Print to console
            self.file.write(output_str)  # Write to file
        self.model.ep_info_buffer.clear()

    def on_training_end(self):
        self.file.close()  # Close the file when training ends

# Environment setup
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array", map_name="8x8", desc=None)
env = Monitor(env)  # Wrap environment to track episode statistics
env = DummyVecEnv([lambda: env])  # Wrap env in DummyVecEnv for compatibility with SB3

# Setup and train the model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./PPOtensorboard/")
callback = CustomCallback()
model.learn(total_timesteps=int(5e5), callback=callback)

# Report overall averages
if total_episodes > 0:
    overall_average_reward = cumulative_reward / total_episodes
    print(f"Overall: Average Reward: {overall_average_reward}")

env.close()

"""### 8x8 frozen lake map PPO - is_slippery on"""
print("8x8 frozen lake map PPO - is_slippery off")

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym


total_episodes = 0
cumulative_reward = 0
output_counter = 0

class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
        self.file = open('training_output_detailed.txt', 'w')  # Open a file to write output

    def _on_step(self) -> bool:
        return True

    def _on_rollout_end(self):
        global total_episodes, cumulative_reward, output_counter
        num_episodes = len(self.model.ep_info_buffer)
        total_episodes += num_episodes
        if num_episodes > 0:
            episode_rewards = [info['r'] for info in self.model.ep_info_buffer]
            average_reward = sum(episode_rewards) / num_episodes
            cumulative_reward += sum(episode_rewards)
            output_counter += 1
            output_str = f"Output {output_counter}: Average over {num_episodes} episodes - Reward: {average_reward}\n"
            print(output_str, end='')
            self.file.write(output_str)
        self.model.ep_info_buffer.clear()

    def on_training_end(self):
        self.file.close()

# Environment setup
env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="rgb_array", map_name="8x8", desc=None)
env = Monitor(env)  # Wrap environment to track episode statistics
env = DummyVecEnv([lambda: env])  # Wrap env in DummyVecEnv for compatibility with SB3

# Setup and train the model
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./PPOtensorboard/")
callback = CustomCallback()
model.learn(total_timesteps=int(5e5), callback=callback)

# Report overall averages
if total_episodes > 0:
    overall_average_reward = cumulative_reward / total_episodes
    print(f"Overall: Average Reward: {overall_average_reward}")

env.close()

"""# 8x8 frozen lake map DQN - is_slippery off"""
print("8x8 frozen lake map DQN - is_slippery off")

#generate_random_map(size=map_size, p=params.proba_frozen, seed=params.seed),
env = gym.make(
        "FrozenLake-v1",
        is_slippery=False,
        render_mode="rgb_array",
        map_name="8x8",
        desc= None
    )

import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
import sys

# Setup the environment and model
env = gym.make("FrozenLake-v1", is_slippery=False, map_name="8x8", render_mode="rgb_array")
model = DQN("MlpPolicy", env, verbose=1, tensorboard_log="./DQNtensorboard/")

#uncomment this when running in colab
'''output_file = "/content/model_output.txt"
with open(output_file, "w") as file:
    original_stdout = sys.stdout
    sys.stdout = file

    # Train the model
    model.learn(total_timesteps=int(5e5), progress_bar=True)


    sys.stdout = original_stdout'''
#uncomment this when running through git repo
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
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=100)
print(f"Mean reward: {mean_reward}, Std reward: {std_reward}")
print("Output written to:", output_file)

"""# CONCLUSION 1- On Randomness Factor

The difference in performance when we turn on/off the is_slippery parameter:

With is_slippery=True: The environment behaves stochastically. Actions taken by the agent do not always result in the intended outcome. For instance, if the agent chooses to move right, there's a chance it might still move up, down, or left. This stochastic nature introduces uncertainty and complexity, making the environment more challenging to navigate successfully.


With is_slippery=False: Each action taken by the agent leads directly to the expected outcome without any deviation. This simplifies the task significantly as the agent can reliably predict the result of its actions, making it easier to learn an effective policy.


When is_slippery is turned off, reaching a perfect score of 1.0 reward in just 10 episodes. The learning algorithm can rapidly converge to an optimal policy.


On the other hand, when is_slippery is on: The agent must learn not only the ideal path to the goal but also how to handle unexpected outcomes of its actions. An average reward capping at around 0.6 suggests that even with optimal learning, the inherent uncertainty of the environment leads to a significant number of failed attempts to reach the goal.

# CONCLUSION 2 - Early training phase vs. Late training phase

Take 4x4 map, PPO, is_slippery off as an example:


Early Training Phase:

*  Low Rewards: Initially, the rewards are very low (0.02 to 0.04), it means that the agent is still learning the optimal paths and strategies. Given that is_slippery is off, the deterministic nature allows for potentially quicker learning, but it still takes some time for the agent to figure out the optimal policy.
*  Exploration: The agent is exploring the environment, adjusting its policy as indicated by its approx_kl and clip_fraction values. KL divergence values are relatively low but show some variation, indicating that the policy is undergoing adjustments, but these changes are not drastic due to the clipping mechanism.


Late training phase:

*  High and Stable Rewards: By the late stages of training, the agent consistently achieves high rewards, mostly reaching 1.0, indicating it has learned to navigate to the goal without falling into holes. This shows successful policy optimization.

*  Reduced KL Divergence and Clip Fraction: These values decrease, showing that policy updates are becoming smaller as the policy stabilizes and requires fewer adjustments.

*  Explained Variance: A high explained variance in some outputs suggests that the model's predictions are closely matching the actual returns.

Take 8x8 map, DQN, is_slippery off as an example:
Early Training Phase:

*  Low Rewards:
The reward mean is consistently 0, suggesting that the agent never reaches the goal in the early stages of training.


*  Exploration:
Exploration rate starting close to 1, and slightly decreasing, this high exploration rate is typical of early training where the model priortizes discovering new strategies over exploiting known paths.

Late training phase:

*  The reward improves significantly, the agent always reaches the goal, showing successful learning.

*  Exploration rate reduced to 0.05, this shows a shift from exploration to exploitation. The agent now leveraged learned strategies to maximize rewards.

# CONCLUSION 3 - 4X4 map vs 8X8 map



When we switch from a 4x4 map to an 8x8 map in the "Frozen Lake" game,


*  Larger State Space: An 8x8 map has significantly more states than a 4x4 map. This means there are more possible locations the agent can be in at any given time, which increases the complexity of the problem.

*  More Decisions: With a larger grid, the number of decisions the agent needs to make before reaching the goal increases. Each decision point potentially introduces opportunities for error.

*  Slower Learning Curve: Reaching a high performance on an 8x8 map by episode 50, as opposed to episode 12 on a 4x4 map, suggests that the agent requires more experiences to learn effective strategies due to the increased complexity. The agent needs more time to explore the environment and achieve successful strategies through trial and error.
"""

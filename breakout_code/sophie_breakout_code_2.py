'''import gymnasium as gym 
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Create and train PPO agent
print('PPO agent')
env = gym.make('Breakout-v4')
model = PPO('CnnPolicy', env, verbose=1)
model.learn(total_timesteps=int(1e5))

# Evaluate the agent
mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=100)
print("Output 1: Average over 100 episodes - Reward: {:.2f}".format(mean_reward))
print("----------------------------------")
print("| rollout/            |          |")
print("|    ep_len_mean      | {:.0f}     |".format(model.ep_info_buffer.episode_lengths.mean()))
print("|    ep_rew_mean      | {:.2f}    |".format(model.ep_info_buffer.episode_rewards.mean()))
print("|    exploration_rate | {:.3f}   |".format(1 - model.exploration_rate))
print("| time/               |          |")
print("|    episodes         | {:.0f}     |".format(len(model.ep_info_buffer)))
print("|    fps              | {:.0f}      |".format(model.num_timesteps / model.total_time))
print("|    time_elapsed     | {:.0f}     |".format(model.total_time))
print("|    total_timesteps  | {:.0f}     |".format(model.num_timesteps))
print("----------------------------------")

# Close environment
env.close()'''

import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy

# Create and train DQN agent
print('DQN agent')

env = gym.make("ALE/Breakout-v5")
model = DQN('CnnPolicy', env, verbose=1)
model.learn(total_timesteps=int(1e5))

# Evaluate the agent
#mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=100)
#print("Output 1: Average over 100 episodes - Reward: {:.2f}".format(mean_reward))
print("----------------------------------")
print("| rollout/            |          |")
print("|    ep_len_mean      | {:.0f}     |".format(model.ep_info_buffer.episode_lengths.mean()))
print("|    ep_rew_mean      | {:.2f}    |".format(model.ep_info_buffer.episode_rewards.mean()))
print("|    exploration_rate | {:.3f}   |".format(1 - model.exploration_rate))
print("| time/               |          |")
print("|    episodes         | {:.0f}     |".format(len(model.ep_info_buffer)))
print("|    fps              | {:.0f}      |".format(model.num_timesteps / model.total_time))
print("|    time_elapsed     | {:.0f}     |".format(model.total_time))
print("|    total_timesteps  | {:.0f}     |".format(model.num_timesteps))
print("----------------------------------")

# Close environment
env.close()


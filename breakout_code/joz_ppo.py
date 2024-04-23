import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.callbacks import BaseCallback
import matplotlib.pyplot as plt
os.environ['KMP_DUPLICATE_LIB_OK']='True'
LOG_DIR = './logs/'
CHECKPOINT_DIR = './train/'

# Number of parallel environments
n_envs = 1 # change to 4 maybe for parallelization?
env = make_atari_env("ALE/Breakout-v5", n_envs=n_envs, monitor_dir=LOG_DIR)
env = VecFrameStack(env, n_stack=4)  # Frame-stacking with 4 frames

class TrainAndSave(BaseCallback):
    def __init__(self, check_freq, save_path, verbose=1):
        super(TrainAndSave, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        self.rewards = []
        self.episode_rewards = []

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self):
        if 'episode' in self.locals:
            self.episode_rewards.append(self.locals['episode']['r'])
        if self.n_calls % self.check_freq == 0:
            if len(self.episode_rewards) > 0:
                average_reward = sum(self.episode_rewards) / len(self.episode_rewards)
                self.rewards.append(average_reward)
                self.episode_rewards = []
            else:
                self.rewards.append(0)
            model_path = os.path.join(self.save_path, f'best_model_{self.n_calls}')
            self.model.save(model_path)
        return True

    def plot_rewards(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.rewards)
        plt.xlabel('Number of Steps (in hundreds of thousands)')
        plt.ylabel('Average Reward')
        plt.title('Reward Over Time')
        plt.show()

model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR,
            learning_rate=0.005, n_steps=128, batch_size=256, n_epochs=10,
            gamma=0.99, gae_lambda=0.95, clip_range=0.2, ent_coef=0.01)

callback = TrainAndSave(check_freq=10000, save_path=CHECKPOINT_DIR)
model.learn(total_timesteps=int(500000), callback=callback)
callback.plot_rewards()

#notes for parameters:
#parameters for parallel4: n_envs=4 and PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR,learning_rate=0.005, n_steps=128, batch_size=256, n_epochs=10,gamma=0.99, gae_lambda=0.95, clip_range=0.2, ent_coef=0.01)
#parameters for baseline: n_envs=1, others same
#parameters for baseline_increasedtimestep: n_envs=1, total_timesteps=int(2000000) others same

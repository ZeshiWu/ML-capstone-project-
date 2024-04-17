import os
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3 import DQN

class TrainAndSave(BaseCallback):
    def __init__(self, check_freq, save_path, verbose=1):
        super(TrainAndSave, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        self.episode_rewards = []
        self.num_episodes = 0
        self.output_number = 0

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self):
        self.output_number += 1
        if self.output_number % self.check_freq == 0:
            mean_reward = round(sum(self.episode_rewards) / max(1, len(self.episode_rewards)), 2)
            print(f"Output {self.output_number}: Average over {len(self.episode_rewards)} episodes - Reward: {mean_reward}")
            self.episode_rewards = []
            self.num_episodes = 0
        return True

    def _on_episode_end(self) -> None:
        self.episode_rewards.append(self.model.ep_info_buffer[0]['r'])
        self.num_episodes += 1

CHECKPOINT_DIR = './train/'
LOG_DIR = './logs/'
window = 4
env = make_atari_env("ALE/Breakout-v5", n_envs=1, monitor_dir=LOG_DIR)
vec_env = VecFrameStack(env, n_stack=window)

callback = TrainAndSave(check_freq=100000, save_path=CHECKPOINT_DIR)
newmodel = DQN('CnnPolicy', vec_env, tensorboard_log=LOG_DIR, verbose=1,
            buffer_size=50000, batch_size=128, learning_starts=10000, gamma=0.95,
            exploration_fraction = 0.3, exploration_final_eps=0.1)

newmodel.learn(total_timesteps=1000000, callback=callback, log_interval=1000)

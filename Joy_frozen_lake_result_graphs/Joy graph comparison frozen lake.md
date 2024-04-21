# 4x4 is slippery vs. 4x4 non slippery

The graph which includes the is_slippery randomness factor, shows more variation in the average reward over time as compared to the non-slippery scenario.

1. Increased Difficulty: The introduction of the is_slippery factor increases the environment's complexity, making it harder for the agent to consistently find the optimal path to the goal. Fewer episodes achieve the maximum reward.
2. After initially improving, there is obvious fluctuation in the reward, possibly due to the exploration strategy and the agent encountering slippery states that lead to failure.
3. Effect of Stochasticity: The inherent stochasticity introduced by the slippery surface causes more unpredictable outcomes, even if the agent selects the same action in the same state across different episodes.

Conclusion: In reinforcement learning, especially in environments with a significant random factor, it is common to have variability in performance. The goal is to maximize the expected return, which does not necessarily mean obtaining the maximum possible return in every single episode. The graph shows the agent's policy is generally good (as it often achieves high rewards), but not perfect due to the environment's challenges.



# 4x4 non slippery vs. 8x8 non slippery
1. Similar Final Performance: Both graphs seem to converge to a high average reward, close to 1.0, which means the agent is able to learn a strategy to reach the goal in both environments.
2. Slightly slower Convergence in 8x8: The 8x8 graph shows that convergence to the optimal performance takes a little bit longer. This is expected because the larger environment has more states and potential transitions, making it more complex and requiring the agent to learn more information before reaching consistent performance.
3. Increased Variability in 8x8 (early stage): The 8x8 graph also shows more variability in the reward during the early learning phase. There are more and deeper dips, suggesting that the agent is occasionally exploring less optimal paths or that it takes longer to generalize the policy due to the increased complexity.


# 8x8 non slippery PPO vs. 8x8 non slippery DQN

The graph for PPO shows a learning curve with a rapid increase in average reward, reaching a high level of performance quickly. The rewards converge to 1.0 and maintain that with few drops. The occasional drops is probably because while the policy learned is generally successful, there are still some exploratory steps or less-optimal decisions. This is typical in reinforcement learning, as exploration is a necessary component to avoid local optima.

On the other hand, the DQN graph shows a less stable learning process, with significant fluctuations throughout training. The performance improves but then sees a significant decline before gradually improving again. This volatility suggests that the DQN is taking longer to find a stable policy in this setting.

Frozen Lake has a discrete and relatively small state space, which might be better navigated by policy-gradient methods like PPO, especially if the policy can be relatively simple.
DQN generally performs better in complex, high-dimensional spaces.




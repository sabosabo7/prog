# RL Q-learning Frozenlake

#%%
import numpy as np
import gym

env = gym.make("FrozenLake-v0")
Q = np.random.uniform(-0.001, 0.001, (env.observation_space.n, env.action_space.n))

# %%
def epsilon_greedy(Q, state, action_num, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(action_num)
    else:
        return Q[state, :].argmax()


#%%
num_episodes = 3000
alpha = 0.5
gamma = 0.95
epsilon = 0.1
rewards = []

#%%
for i in range(num_episodes):
    s = env.reset()

    episode_reward = 0
    while True:
        a = epsilon_greedy(Q, s, env.action_space.n, epsilon)
        s1, r, d, _ = env.step(a)
        env.render()
        episode_reward += r
        Q[s, a] += alpha * (r + gamma * np.max(Q[s1, :] - Q[s, a]))
        s = s1
        if d:
            break
    rewards.append(episode_reward)
# %%
print(max(rewards))

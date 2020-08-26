# RL Q-learning cartpole
#%%
import numpy as np
import gym

input_num = 4
action_num = 2
divide_num = 10
space_num = divide_num ** input_num

env = gym.make("CartPole-v1")
Q = np.random.uniform(-0.001, 0.001, (space_num, action_num))

# %%
def epsilon_greedy(Q, state, action_num, epsilon, episode):
    if np.random.random() < epsilon / (1 + episode):
        return np.random.randint(action_num)
    else:
        return Q[state, :].argmax()


def get_state(obs):
    position = np.digitize(obs[0], np.linspace(-2.4, 2.4, divide_num + 1)[1:-1])
    velocity = np.digitize(obs[1], np.linspace(-5, 5, divide_num + 1)[1:-1])
    angle = np.digitize(obs[2], np.linspace(-12, 12, divide_num + 1)[1:-1])
    angular_velocity = np.digitize(obs[3], np.linspace(-5, 5, divide_num + 1)[1:-1])
    return (
        position * (divide_num ** 3)
        + velocity * (divide_num ** 2)
        + angle * divide_num
        + angular_velocity
    )


#%%
num_episodes = 3000
alpha = 0.5
gamma = 0.8
epsilon = 0.1
max_number_of_step = 200

#%%
episode = 0
while True:
    s = get_state(env.reset())
    for t in range(max_number_of_step):
        a = epsilon_greedy(Q, s, action_num, epsilon, episode)
        s1, r, d, _ = env.step(a)
        # env.render()
        if d and t < 195:
            r = -100
        s1 = get_state(s1)
        Q[s, a] += alpha * (r + gamma * np.max(Q[s1, :] - Q[s, a]))
        s = s1
        if d:
            break

    print("episode", episode, "after", t, "step")
    episode += 1

# %%

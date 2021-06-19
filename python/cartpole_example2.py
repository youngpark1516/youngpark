import gym
import numpy as np

#
# Environment
#
env = gym.make('CartPole-v1')
state = env.reset()
action = env.action_space.sample()

print('State space: ', env.observation_space)
print('Initial state: ', state)
print('\nAction space: ', env.action_space)
print('Random action: ', action)
# Q-Network Modeling
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

num_state = env.observation_space.shape[0]
num_action = env.action_space.n

model = Sequential()
model.add(Dense(32, input_dim=num_state, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(num_action, activation=None))
model.compile(loss='mse', optimizer="adam")
from tqdm import tqdm

num_iteration = 1
min_timesteps_per_batch = 2500

# Hyper parameter
epsilon = 0.3
gamma = 0.95
batch_size = 32

# Q-Network Learning
for i in tqdm(range(num_iteration)):
    timesteps_this_batch = 0
    memory = []
    while True:
        state = env.reset()
        done = False
        while not done:
            if np.random.uniform() < epsilon:
                action = env.action_space.sample()
            else:
                q_value = model.predict(state.reshape(1, num_state))
                action = np.argmax(q_value[0])
            next_state, reward, done, info = env.step(action)
            # Memory
            memory.append((state, action, reward, next_state, done))

            state = next_state

        timesteps_this_batch += len(memory)
        if timesteps_this_batch > min_timesteps_per_batch:
            break

    # Replay
    for state, action, reward, next_state, done in memory:
        if done:
            target = reward
        else:
            target = reward + gamma * (np.max(model.predict(next_state.reshape(1, num_state))[0]))
        q_value = model.predict(state.reshape(1, num_state))
        q_value[0][action] = target
        model.fit(state.reshape(1, num_state), q_value, epochs=1, batch_size=32, verbose=0)

env.close()

from gym.wrappers import Monitor

import base64
from IPython.display import HTML
from IPython import display as ipythondisplay

from pyvirtualdisplay import Display

display = Display(visible=0, size=(1400, 900))
display.start()


def show_video(file_infix):
    with open('./video/openaigym.video.%s.video000000.mp4' % file_infix, 'r+b') as f:
        video = f.read()
        encoded = base64.b64encode(video)
        ipythondisplay.display(HTML(data='''<video alt="Trained CartPole" autoplay 
                loop style="height: 200px;">
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
                 </video>'''.format(encoded.decode('ascii'))))


def wrap_env(env):
    env = Monitor(env, './video', force=True)
    return env


from tensorflow.keras.models import load_model
import os

load_dir = os.getcwd()
model_name = 'keras_dqn_trained_model.h5'
model_path = os.path.join(load_dir, model_name)
model = load_model(model_path)
import gym
import numpy as np

env = wrap_env(gym.make('CartPole-v1'))
num_state = env.observation_space.shape[0]
state = env.reset()
done = False

while not done:
    state = np.array(state).reshape(1, num_state)
    q_value = model.predict(state)
    action = np.argmax(q_value[0])
    state, reward, done, info = env.step(action)

file_infix = env.file_infix
env.close()

show_video(file_infix)
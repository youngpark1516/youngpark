import time
import argparse
import numpy as np
import gym
import gym_minigrid
from gym_minigrid.wrappers import *
from gym_minigrid.window import Window
import copy
import pylab
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential

class DeepSARSAgent:
    def __init__(self):
        # actions which agent can do
        self.action_space = [0, 1, 2]
        # get size of state and action
        self.action_size = len(self.action_space)
        self.state_size = 147
        self.discount_factor = 0.99
        self.learning_rate = 0.001

        self.epsilon = 1.  # exploration
        self.epsilon_decay = .9999
        self.epsilon_min = 0.01
        self.model = self.build_model()


    # approximate Q function using Neural Network
    # state is input and Q Value of each action is output of network
    def build_model(self):
        model = Sequential()
        model.add(Dense(30, input_dim=self.state_size, activation='relu'))
        model.add(Dense(30, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.summary()
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    # get action from model using epsilon-greedy policy
    def get_action(self, state):
        if np.random.rand() <= self.epsilon:
            # The agent acts randomly
            return random.randrange(self.action_size)
        else:
            # Predict the reward value based on the given state
            state = np.float32(state)
            q_values = self.model.predict(state)
            return np.argmax(q_values[0])

    def train_model(self, state, action, reward, next_state, next_action, done):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        state = np.float32(state)
        next_state = np.float32(next_state)
        target = self.model.predict(state)#[0]
        # like Q Learning, get maximum Q value at s'
        # But from target model
        if done:
            target[0][action] = reward
        else:
            target[0][action] = (reward + self.discount_factor *
                              self.model.predict(next_state)[0][next_action])
        # target = np.reshape(target, [1, 5])
        # make minibatch which includes target q value and predicted q value
        # and do the model fit!
        self.model.fit(state, target, epochs=1, verbose=0)

def redraw(img):
    if not args.agent_view:
        img = env.render('rgb_array', tile_size=args.tile_size)

    window.show_img(img)

def reset():
    if args.seed != -1:
        env.seed(args.seed)

    state = env.reset()

    if hasattr(env, 'mission'):
        # print('Mission: %s' % env.mission)
        window.set_caption(env.mission)

    redraw(state)

def step(action):
    state, reward, done, info = env.step(action)
    # print('step=%s, reward=%.2f' % (env.step_count, reward))
    if done:
        # print('done!')
        reset()
    else:
        redraw(state)
    return state, reward, done


def render():
    time.sleep(0.03)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--env",
    help="gym environment to load",
    default='MiniGrid-Dynamic-Obstacles-8x8-v0'
)
parser.add_argument(
    "--seed",
    type=int,
    help="random seed to generate the environment with",
    default=-1
)
parser.add_argument(
    "--tile_size",
    type=int,
    help="size at which to render tiles",
    default=32
)
parser.add_argument(
    '--agent_view',
    default=False,
    help="draw the agent sees (partially observable view)",
    action='store_true'
)



if __name__ == "__main__":
    args = parser.parse_args()

    env = gym.make(args.env)

    if args.agent_view:
        env = RGBImgPartialObsWrapper(env)
        env = ImgObsWrapper(env)

    window = Window('gym_minigrid - ' + args.env)



    agent = DeepSARSAgent()

    global_step = 0
    scores, episodes = [], []

    for e in range(30000):
        done = False
        score = 0
        state = env.reset()
        state = np.reshape(state['image'], [1, 147])
        reset()

        while not done:
            # fresh env
            global_step += 1

            # get action for the current state and go one step in environment
            action = agent.get_action(state)
            # next_state,
            if action == 0:
                action = env.actions.left
            elif action == 1:
                action = env.actions.right
            elif action == 2:
                action = env.actions.forward
            next_state, reward, done = step(action)
            # state = np.reshape(state['image'], [1, 147])
            next_state = np.reshape(next_state['image'], [1, 147])
            next_action = agent.get_action(next_state)
            agent.train_model(state, action, reward, next_state, next_action,
                              done)

            state = next_state
            # every time step we do training
            score += reward

            # state = copy.deepcopy(next_state)
            render()
            if done:
                scores.append(score)
                episodes.append(e)
                # pylab.plot(episodes, scores, 'b')
                print("episode:", e, "  score:", score, "global_step",
                      global_step, "  epsilon:", agent.epsilon)


    window.show(block=True)
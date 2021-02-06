import copy
import pylab
import random
import numpy as np
from environment_REINFORCE improt Env
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class REINFORCE(tf.keras.Model):
    def __init__(self,action_size):
        super(REINFORCE, self).__init__()
        self.fc1 = Dense(24, activation = 'relu')
        self.fc2 = Dense(24, activation='relu')
        self.fc_out = Dense(action_size, activation= 'softmax')

    def call(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        policy = self.fc_out(x)
        return policy

class REINFORCEAgent:
    def __init__(self,state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.discount_factor = 0.99
        self.learning_rate = 0.001
        self.model = self.build_model()

        self.states, self.actions, self.rewards = [], [], []
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten
import random
import numpy as np
import pandas as pd
from operator import add


class DQNAgent(object):

    def __init__(self,visualRange):
        self.reward = 0
        self.gamma = 0.7
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array([])
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate = 0.0005
        self.input_dim = (visualRange*2,visualRange*2,3)
        self.model = self.network(self.input_dim )
        # self.model = self.network("weights.hdf5")
        self.epsilon = 0
        self.actual = []
        self.memory = np.zeros((1000, 52))

    def on_init(self,visualRange):
        input_dim = (1,(visualRange*2),(visualRange*2),3)
        self.model = self.network(input_dim)

    '''
    def get_state(self, game, player, food):

        state = [
            (player.x_change == 20 and player.y_change == 0 and ((list(map(add, player.position[-1], [20, 0])) in player.position) or
            player.position[-1][0] + 20 >= (game.game_width - 20))) or (player.x_change == -20 and player.y_change == 0 and ((list(map(add, player.position[-1], [-20, 0])) in player.position) or
            player.position[-1][0] - 20 < 20)) or (player.x_change == 0 and player.y_change == -20 and ((list(map(add, player.position[-1], [0, -20])) in player.position) or
            player.position[-1][-1] - 20 < 20)) or (player.x_change == 0 and player.y_change == 20 and ((list(map(add, player.position[-1], [0, 20])) in player.position) or
            player.position[-1][-1] + 20 >= (game.game_height-20))),  # danger straight

            (player.x_change == 0 and player.y_change == -20 and ((list(map(add,player.position[-1],[20, 0])) in player.position) or
            player.position[ -1][0] + 20 > (game.game_width-20))) or (player.x_change == 0 and player.y_change == 20 and ((list(map(add,player.position[-1],
            [-20,0])) in player.position) or player.position[-1][0] - 20 < 20)) or (player.x_change == -20 and player.y_change == 0 and ((list(map(
            add,player.position[-1],[0,-20])) in player.position) or player.position[-1][-1] - 20 < 20)) or (player.x_change == 20 and player.y_change == 0 and (
            (list(map(add,player.position[-1],[0,20])) in player.position) or player.position[-1][
             -1] + 20 >= (game.game_height-20))),  # danger right

             (player.x_change == 0 and player.y_change == 20 and ((list(map(add,player.position[-1],[20,0])) in player.position) or
             player.position[-1][0] + 20 > (game.game_width-20))) or (player.x_change == 0 and player.y_change == -20 and ((list(map(
             add, player.position[-1],[-20,0])) in player.position) or player.position[-1][0] - 20 < 20)) or (player.x_change == 20 and player.y_change == 0 and (
            (list(map(add,player.position[-1],[0,-20])) in player.position) or player.position[-1][-1] - 20 < 20)) or (
            player.x_change == -20 and player.y_change == 0 and ((list(map(add,player.position[-1],[0,20])) in player.position) or
            player.position[-1][-1] + 20 >= (game.game_height-20))), #danger left


            player.x_change == -20,  # move left
            player.x_change == 20,  # move right
            player.y_change == -20,  # move up
            player.y_change == 20,  # move down
            food.x_food < player.x,  # food left
            food.x_food > player.x,  # food right
            food.y_food < player.y,  # food up
            food.y_food > player.y  # food down
            ]

        for i in range(len(state)):
            if state[i]:
                state[i]=1
            else:
                state[i]=0

        return np.asarray(state)
    '''
    '''
    def set_reward(self, player, crash):
        self.reward = 0
        if crash:
            self.reward = -10
            return self.reward
        if player.eaten:
            self.reward = 10
        return self.reward
    '''


    def network(self, input_dim, weights=None):
        self.model = Sequential()
        #self.model.add(Dense(50, activation='relu',input_shape= (6*6,)))
        #self.model.add(Dropout(0.15))
        #self.model.add(Dense(50, activation='relu'))
        #self.model.add(Dropout(0.15))
        #self.model.add(Dense(output_dim=120, activation='relu'))
        #self.model.add(Dropout(0.15))
        #self.model.add(Flatten())
        #self.model.add(Dense(6, activation='softmax'))

        self.model.add(Conv2D(9,(3, 3), input_shape=input_dim))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(3, 3)))
        self.model.add(Flatten())  
        self.model.add(Dense(6))
        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(6))
        self.model.add(Activation("softmax"))
        opt = Adam(self.learning_rate)
        self.model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

        if weights:
            self.model.load_weights(weights)
        print(self.model.summary())
        return self.model

    def remember(self, state, action, reward, next_state):
        #self.memory.append((state, action, reward, next_state))
        self.memory=np.array([state, action, reward, next_state])

    def replay_new(self, memory):
        if len(memory) > 700:
            minibatch = random.sample(memory, 700)
        else:
            minibatch = memory

        '''
        for state, action, reward, next_state in minibatch:
            target = reward
            next_state = np.array(next_state)[np.newaxis, :, :,:]
            #target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target = reward + self.gamma * np.amax(self.model.predict([next_state]))
            target_f = self.model.predict(np.array([state]))
            #target_f[0][np.argmax(action)] = target
            target_f[0][action] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)
        '''

    def train_short_memory(self, state, action, reward, next_state):
        self.reward= reward 
        target = reward
        next_state = np.array(next_state)[np.newaxis, :, :,:]
        #target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((-1, -1))))
        target = reward + self.gamma * np.amax(self.model.predict(next_state))
        #target_f = self.model.predict(state.reshape((1, -1)))
        state = np.array(state)[np.newaxis, :, :,:]
        target_f = self.model.predict(state)
        #target_f[0][np.argmax(action)] = target
        target_f[0][action] = target
        #self.model.fit(state.reshape((1, -1)), target_f, epochs=1, verbose=0)
        self.model.fit(state, target_f, epochs=1, verbose=0)

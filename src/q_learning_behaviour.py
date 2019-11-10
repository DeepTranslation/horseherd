from behaviour import *

from random import randint
from DQN import DQNAgent
import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class QLearningBehaviour(Behaviour):
    def __init__(self):
        self.agent = DQNAgent()
        self.age = 0
        self.current_move = None
        self.current_input = None

    def decide(self, input):
        self.current_input = input

        final_move = None

        epsilon = 80 - self.age
        if randint(0, 200) < epsilon:
            final_move = randrange(5)
        else:
            #get old state
            #state_old = agent.get_state(game, player1, food1)
            state_old = np.asarray(input)

            prediction = self.agent.model.predict(input.reshape((1,-1)))
            #final_move = to_categorical(np.argmax(prediction[0]), num_classes=5)
            final_move = np.argmax(prediction[0])

        self.current_move = final_move
        self.age += 1

        return final_move

        #perform new move and get new state
        #self.do_move(final_move, self.x,self.y,agent)
        #state_new = agent.get_state(game, player1, food1)

    def feedback(self, reward):
        #set treward for the new state
        #reward = agent.set_reward(input, move,reward)

        #train short memory base on the new action and state
        state_new = self.current_input #
        final_move = to_categorical(self.current_move, num_classes=5)
        self.agent.train_short_memory(self.current_input, final_move, reward, state_new)

        # store the new data into a long term memory
        self.agent.remember(state_old, final_move, reward, state_new)
        #record = get_record(game.score, record)
        #if display_option:
        #    display(player1, food1, game, record)
        #    pygame.time.wait(speed)

        self.agent.replay_new(agent.memory) #???

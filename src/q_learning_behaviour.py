from behaviour import *

from DQN import DQNAgent
import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class QLearningBehaviour(Behaviour):
    def __init__(self):
        self.agent = DQNAgent()
        
    def decide(self, input):

        #agent.epsilon is set to give randomness to actions
        agent.epsilon = 80 - self.age
        
        #get old state
        #state_old = agent.get_state(game, player1, food1)
        state_old = np.asarray(input)
        
        #perform random actions based on agent.epsilon, or choose the action
        if randint(0, 200) < agent.epsilon:
             final_move = randrange(5)
        else:
        # predict action based on the old state
            final_move = QLearningBehaviour.decide()
        
        return final_move

        prediction = agent.model.predict(input.reshape((1,-1)))
        #final_move = to_categorical(np.argmax(prediction[0]), num_classes=5)
        final_move = np.argmax(prediction[0])

        return final_move

        #perform new move and get new state
        #self.do_move(final_move, self.x,self.y,agent)
        #state_new = agent.get_state(game, player1, food1)

    def feedback(self,state_old,final_move,reward,state_new):
        #set treward for the new state
        #reward = agent.set_reward(input, move,reward)

        #train short memory base on the new action and state
        final_move = to_categorical(final_move, num_classes=5)
        agent.train_short_memory(state_old, final_move, reward, state_new)

        # store the new data into a long term memory
        agent.remember(state_old, final_move, reward, state_new)
        #record = get_record(game.score, record)
        #if display_option:
        #    display(player1, food1, game, record)
        #    pygame.time.wait(speed)

        agent.replay_new(agent.memory) #???

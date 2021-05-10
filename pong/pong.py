#%%

import cv2
import gym
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

import torch
from torch import nn, optim
# from torch.utils.tensorboard import SummaryWriter

from IPython.display import HTML
#%%
class PongEnv(gym.Env):
    def __init__(self):

        SCREEN_WIDTH, SCREEN_HEIGHT = 200, 200
        # self.observation_space = gym.spaces.Tuple([
        #     gym.spaces.Box(
        #         low=0, high=255, shape=(SCREEN_HEIGHT, SCREEN_WIDTH, 3)),
        #     gym.spaces.Box(
        #         low=0, high=255, shape=(SCREEN_HEIGHT, SCREEN_WIDTH, 3))
        # ])
        self.observation_space =gym.spaces.Box(
            low=0, high=255, shape=(SCREEN_HEIGHT, SCREEN_WIDTH, 3),dtype=np.uint8)

        self.action_space = gym.spaces.Tuple(
            [gym.spaces.Discrete(3), gym.spaces.Discrete(3)])
        
        self._game=PongGame(SCREEN_WIDTH, SCREEN_HEIGHT)


    def step(self,action):
        assert self.action_space.contains(action)
        action1p, action2p = action
        obs,rewards, done, _ = self._game.step(action1p,action2p)
        return (obs, rewards, done, {})
    def reset(self):
        obs= self._game.reset()
        return obs


class PongGame():

    ball_v=2
    bar_l=20
    bar1p_v,bar2p_v=1,1

    def __init__(self,SCREEN_WIDTH, SCREEN_HEIGHT):
        
        self.score1p=0
        self.score2p=0
        self.field_x=SCREEN_WIDTH
        self.field_y=SCREEN_HEIGHT
        self.ball_x=self.field_x/2
        self.ball_y=self.field_y/2
        self.ball_ang=np.random.randint(-80,80)

        self.bar1p_x=20
        self.bar1p_y=self.field_y/2
        self.bar1p_l=self.bar_l 

        self.bar2p_x=self.field_x-20
        self.bar2p_y=self.field_y/2
        self.bar2p_l=self.bar_l 

    def reset(self):
        self.score1p=0
        self.score2p=0
        
        self.ball_x=self.field_x/2
        self.ball_y=self.field_y/2
        self.ball_ang=np.random.randint(-80,80)

        self.bar1p_x=20
        self.bar1p_y=self.field_y/2
        self.bar1p_l=self.bar_l 

        self.bar2p_x=self.field_x-20
        self.bar2p_y=self.field_y/2
        self.bar2p_l=self.bar_l 
        obs =self.render()
        return obs 

    def render(self):
        obs = np.zeros((self.field_x,self.field_y,3),np.uint8)
        cv2.rectangle(
            obs,
            (int(self.bar1p_x-4),int(self.bar1p_y-self.bar1p_l/2)),
            (int(self.bar1p_x),int(self.bar1p_y+self.bar1p_l/2)),
            (255,255,255),-1)

        cv2.rectangle(
            obs,
            (int(self.bar2p_x),int(self.bar2p_y-self.bar2p_l/2)),
            (int(self.bar2p_x+4),int(self.bar2p_y+self.bar2p_l/2)),
            (255,255,255),-1)
        
        cv2.circle(obs,(int(self.ball_x),int(self.ball_y)),2,(255,255,255),-1)
        return obs

    def step(self,action1p,action2p,playmode="auto"):
        #step bar 0:-y 1:stay 2:+y
        if playmode=="auto":
            # action1p =  (self.ball_y-self.bar1p_y>2)*2 + (self.ball_y-self.bar1p_y<-2)*0 +(-2<=self.ball_y-self.bar1p_y<=2)*1
            action2p =  (self.ball_y-self.bar2p_y>2)*2 + (self.ball_y-self.bar2p_y<-2)*0 +(-2<=self.ball_y-self.bar2p_y<=2)*1
        
        if action1p==0:
            self.bar1p_y=max(self.bar1p_l/2,self.bar1p_y-self.bar1p_v)
        elif action1p==2:
            self.bar1p_y=min(self.field_y-self.bar1p_l/2,self.bar1p_y+self.bar1p_v)
        if action2p==0:
            self.bar2p_y=max(self.bar2p_l/2,self.bar2p_y-self.bar2p_v)
        elif action2p==2:
            self.bar2p_y=min(self.field_y-self.bar2p_l/2,self.bar2p_y+self.bar2p_v)


        #step ball
        delta_x= self.ball_v*np.cos(np.radians(self.ball_ang)) 
        delta_y= self.ball_v*np.sin(np.radians(self.ball_ang))
        ball_next_x =self.ball_x+delta_x  
        ball_next_y =self.ball_y+delta_y
 
        while delta_x!=0 and delta_y!=0:

            #hit 1p bar    
            if self.bar1p_x<self.ball_x and ball_next_x<self.bar1p_x:
                cross_delta_x = self.bar1p_x-self.ball_x
                cross_delta_y= delta_y/delta_x*cross_delta_x
                cross_y = self.ball_y+cross_delta_y
                if self.bar1p_y-self.bar1p_l/2<cross_y and self.bar1p_y+self.bar1p_l/2>cross_y:
                    self.ball_x += cross_delta_x
                    self.ball_y += cross_delta_y
                    self.ball_ang=180-self.ball_ang
                    delta_x =(delta_x- cross_delta_x)*(-1)
                    delta_y = delta_y-cross_delta_y
                    ball_next_x =self.ball_x+delta_x  
                    ball_next_y =self.ball_y+delta_y
                    continue
            
            #hit 2p bar 
            if self.bar2p_x>self.ball_x and ball_next_x>self.bar2p_x:
                cross_delta_x = self.bar2p_x-self.ball_x
                cross_delta_y= delta_y/delta_x*cross_delta_x
                cross_y = self.ball_y+cross_delta_y
                if self.bar2p_y-self.bar2p_l/2<cross_y and self.bar2p_y+self.bar2p_l/2>cross_y:
                    self.ball_x += cross_delta_x
                    self.ball_y += cross_delta_y
                    self.ball_ang=180-self.ball_ang
                    delta_x =(delta_x- cross_delta_x)*(-1)
                    delta_y = delta_y-cross_delta_y
                    ball_next_x =self.ball_x+delta_x  
                    ball_next_y =self.ball_y+delta_y
                    continue

            #hit top wall        
            if ball_next_y<0 :
                cross_delta_y = 0-self.ball_y 
                cross_delta_x = delta_x/delta_y*cross_delta_y

                self.ball_x += cross_delta_x 
                self.ball_y += cross_delta_y
                self.ball_ang = -self.ball_ang
                delta_x = delta_x- cross_delta_x
                delta_y = (delta_y-cross_delta_y)*(-1)
                ball_next_x =self.ball_x+delta_x  
                ball_next_y =self.ball_y+delta_y
                continue

            #hit bottom wall     
            if ball_next_y>self.field_y:
                cross_delta_y = self.field_y-self.ball_y 
                cross_delta_x = delta_x/delta_y*cross_delta_y

                self.ball_x += cross_delta_x 
                self.ball_y += cross_delta_y
                self.ball_ang = -self.ball_ang
                delta_x = delta_x- cross_delta_x
                delta_y = (delta_y-cross_delta_y)*(-1)
                ball_next_x =self.ball_x+delta_x  
                ball_next_y =self.ball_y+delta_y
                continue
            
            # step ball normally 
            self.ball_x+=delta_x
            self.ball_y+=delta_y
            delta_x = 0
            delta_y = 0

            #check out 
            reward=np.zeros(2)
            if self.ball_x < 0:
                self.score2p+=1
                reward=np.array([-1,1])
                self.ball_x=self.field_x/2
                self.ball_y=self.field_y/2
                self.ball_ang =np.random.randint(-80,80) 
            elif self.ball_x>self.field_x:
                self.score1p+=1
                reward=np.array([1,-1])
                self.ball_x=self.field_x/2
                self.ball_y=self.field_y/2
                self.ball_ang=np.random.randint(-80,80)
            
        #check finish
        done=False
        if self.score1p>10:
            done=True
        elif self.score2p>10:
            done=True
        
        #make obs
        obs = self.render()
        return obs,reward,done,{}

def display_video(frames):
    plt.figure(figsize=(8, 8), dpi=50)
    patch = plt.imshow(frames[0], cmap='gray')
    plt.axis('off')
    
    def animate(i):
        patch.set_data(frames[i])
    
    anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval=50)
    display(HTML(anim.to_jshtml(default_mode='once')))
    plt.close()


# %%
class PongNoopResetEnv(gym.Wrapper):
    def __init__(self, env, noop_max=30):
        gym.Wrapper.__init__(self, env)
        self.noop_max = noop_max
        self.override_num_noops = None
        self.noop_action = (1,1)
        # assert env.unwrapped.get_action_meanings()[0] == 'NOOP'

    def reset(self, **kwargs):
        self.env.reset(**kwargs)
        if self.override_num_noops is not None:
            noops = self.override_num_noops
        else:
            noops = np.random.randint(1, self.noop_max + 1)
        assert noops > 0
        obs = None
        for _ in range(noops):
            obs, _, done, _ = self.env.step(self.noop_action)
            if done:
                obs = self.env.reset(**kwargs)
        return obs

    def step(self, ac):
        return self.env.step(ac)

class PongMaxAndSkipEnv(gym.Wrapper):
    def __init__(self, env, skip=4):
        gym.Wrapper.__init__(self, env)
        self._obs_buffer = np.zeros((2,)+env.observation_space.shape, dtype=np.uint8)
        self._skip       = skip

    def step(self, action):
        total_reward = 0.0
        done = None
        for i in range(self._skip):
            obs, reward, done, info = self.env.step(action)
            if i == self._skip - 2: self._obs_buffer[0] = obs
            if i == self._skip - 1: self._obs_buffer[1] = obs
            total_reward += reward
            if done:
                break
        max_frame = self._obs_buffer.max(axis=0)

        return max_frame, total_reward, done, info

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)

class PongWarpFrame(gym.ObservationWrapper):
    def __init__(self, env, width=84, height=84, grayscale=True, dict_space_key=None):
        super().__init__(env)
        self._width = width
        self._height = height
        self._grayscale = grayscale
        self._key = dict_space_key
        if self._grayscale:
            num_colors = 1
        else:
            num_colors = 3

        new_space = gym.spaces.Box(
            low=0,
            high=255,
            shape=(self._height, self._width, num_colors),
            dtype=np.uint8,
        )
        if self._key is None:
            original_space = self.observation_space
            self.observation_space = new_space
        else:
            original_space = self.observation_space.spaces[self._key]
            self.observation_space.spaces[self._key] = new_space
        assert original_space.dtype == np.uint8 and len(original_space.shape) == 3

    def observation(self, obs):
        if self._key is None:
            frame = obs
        else:
            frame = obs[self._key]

        if self._grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.resize(
            frame, (self._width, self._height), interpolation=cv2.INTER_AREA
        )
        if self._grayscale:
            frame = np.expand_dims(frame, -1)

        if self._key is None:
            obs = frame
        else:
            obs = obs.copy()
            obs[self._key] = frame
        return obs
class TorchFrame(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        height, width, channels = self.observation_space.shape
        self.observation_space = gym.spaces.Box(
            low=0,
            high=255,
            shape=(channels, height, width),
            dtype=np.uint8,
        )

    def observation(self, obs):
        return torch.as_tensor(obs.transpose([2, 0, 1]))
# %%
env=PongEnv()
env=NoopResetEnv(env,noop_max=30)
env=MaxAndSkipEnv(env)
env=WarpFrame(env)
env= TorchFrame(env)
#%%
obs=env.reset()
frames = []
total_reward = np.zeros(2)
done = False
while not done:
    frames.append(obs[0])
    action = env.action_space.sample()  # 行動空間から一様ランダムに行動をサンプル
    next_obs, reward, done, _ = env.step(action)
    total_reward += reward
    obs = next_obs

print('Reward: ', total_reward)
display_video(frames)
# %%

import gym
import numpy as np
import pygame
from gym import spaces
from track import Track
from vehicule_class import Vehicule

class RacingEnv(gym.Env):
    def __init__(self):
        super(RacingEnv, self).__init__()
        
        self.track = Track()
        self.track_points = self.track.get_track()
        self.position = list(self.track_points[0])
        self.angle = 0

        self.vehicle = Vehicule(10, 1, np.linspace(-np.pi/5, np.pi/5, 20).tolist(), self.position)

        self.action_space = spaces.Discrete(3)  # 0 = avancer, 1 = gauche, 2 = droite
        self.observation_space = spaces.Box(low=-1000, high=1000, shape=(3,), dtype=np.float32)

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Course IA")
        self.clock = pygame.time.Clock()

    def step(self, action):
        if action == 1:  
            self.vehicle.setChamp('left', self.vehicle.getOrientation())
        elif action == 2:  
            self.vehicle.setChamp('right', self.vehicle.getOrientation())

        self.vehicle.setMoveAway()
        self.position = self.vehicle.getPosition()

        reward = -1
        done = False
        if any(np.linalg.norm(np.array(self.position) - p) < 10 for p in self.track_points):
            reward = 1
        else:
            reward = -5  

        if np.linalg.norm(np.array(self.position) - np.array(self.track_points[-1])) < 10:
            reward = 10
            done = True

        return np.array([self.position[0], self.position[1], self.vehicle.getOrientation()]), reward, done, {}

    def reset(self):
        self.position = list(self.track_points[0])
        self.vehicle = Vehicule(10, 1, np.linspace(-np.pi/5, np.pi/5, 20).tolist(), self.position)
        return np.array([self.position[0], self.position[1], self.vehicle.getOrientation()])

    def render(self, mode="human"):
        self.screen.fill((50, 50, 50))
        self.track.draw_track(self.screen)

        pygame.draw.circle(self.screen, (0, 0, 255), (int(self.position[0]), int(self.position[1])), 10)
        pygame.display.flip()
        self.clock.tick(30)

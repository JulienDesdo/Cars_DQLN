from stable_baselines3 import PPO
from racing_env import RacingEnv

env = RacingEnv()

# Entraînement
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

# Sauvegarde
model.save("models/ppo_racing")

# Test
obs = env.reset()
done = False
while not done:
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    env.render()

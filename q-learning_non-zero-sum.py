import itertools
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

S0 = 100   
S_T = 120
K = 105           
sigma = 0.2       
r = 0.05          
T = 1             
dt = 0.01         
num_steps = int(T / dt)  
alpha = 0.1       
gamma = 0.95      

actions = [0, 1, 2]
num_actions = len(actions)

Q_A = np.zeros((num_steps, num_actions))
Q_B = np.zeros((num_steps, num_actions))

def simulate_stock_price(S0, mu, sigma, dt, num_steps):
    S = np.zeros(num_steps)
    S[0] = S0
    for t in range(1, num_steps):
        dW = np.random.normal(0, np.sqrt(dt))
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * dW)
    return S

def payoff(S_T, K, action_A, action_B):
    if action_A == 1 and action_B == 1:  
        return 0.5 * max(S_T - K, 0) 
    elif action_A == 1: 
        return max(S_T - K, 0)
    elif action_B == 1:  
        return max(S_T - K, 0)
    else:  
        return 0

def check_nash_equilibrium(S_T, K):
    actions = [0, 1]  
    nash_equilibria = []

    for action_A, action_B in itertools.product(actions, repeat=2):
        payoff_A = payoff(S_T, K, action_A, action_B)
        payoff_B = payoff(S_T, K, action_A, action_B)
        
        payoff_A_if_A_changes = payoff(S_T, K, 1 - action_A, action_B)
        payoff_B_if_B_changes = payoff(S_T, K, action_A, 1 - action_B)
        
        if payoff_A >= payoff_A_if_A_changes and payoff_B >= payoff_B_if_B_changes:
            nash_equilibria.append((action_A, action_B))
    
    return nash_equilibria


def q_learning(S0, K, sigma, num_steps, alpha, gamma):
    S = simulate_stock_price(S0, r, sigma, dt, num_steps)
    for t in range(num_steps - 1):

        action_A = np.random.choice(actions)
        action_B = np.random.choice(actions)
        
        S_T = S[t+1]
        
        reward_A = payoff(S_T, K, action_A, action_B)
        reward_B = payoff(S_T, K, action_B, action_A)
        
        Q_A[t, action_A] += alpha * (reward_A + gamma * np.max(Q_A[t+1]) - Q_A[t, action_A])
        
        Q_B[t, action_B] += alpha * (reward_B + gamma * np.max(Q_B[t+1]) - Q_B[t, action_B])
        
    return S, Q_A, Q_B

S, Q_A, Q_B = q_learning(S0, K, sigma, num_steps, alpha, gamma)
nash_eq = check_nash_equilibrium(S_T, K)
print(nash_eq)

plt.figure(figsize=(10, 6))
plt.plot(S, label="Stock Price")
plt.title("Simulated Stock Price (Geometric Brownian Motion)")
plt.xlabel("Time Steps")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

print("Q-values for Trader A:")
print(Q_A)

print("Q-values for Trader B:")
print(Q_B)

# Non-Zero-Sum Stochastic Games in Derivative Pricing  

## Abstract  
This project focuses on non-zero-sum stochastic games in financial derivative pricing, where market participants have differing objectives. It explores how strategic interactions affect pricing dynamics and discusses Nash equilibrium and risk-neutral valuation principles in optimizing derivative pricing strategies.

## 1. Introduction  
In real markets, unlike traditional zero-sum models, participants can benefit from cooperation. This project applies stochastic game theory to model market interactions, offering a more realistic understanding of pricing dynamics and participant behavior in derivative markets.

Stochastic games account for the randomness in financial markets and the strategic behavior of agents. The market states evolve over time, influenced by participants' decisions and external factors.

- **State Space & Transition Probabilities**: Market conditions evolve based on player actions and stochastic processes. Transition probabilities capture the likelihood of moving from one state to another.
  
- **Payoff Functions**: Players' rewards depend on both their own actions and others' decisions, unlike in zero-sum games where one player's gain is another’s loss. This framework allows for mutual benefits in derivative pricing.

- **Nash Equilibrium**: In stochastic games, a Nash equilibrium is where no player can improve their payoff by changing their strategy, given others’ strategies.

## 3. Applications in Derivative Pricing  
Stochastic games can model the strategic decisions of market participants, influencing derivative pricing. For instance, in options and futures markets, traders' actions—such as buying or selling derivatives—affect the price, creating more dynamic market behavior than traditional models.

- **Risk-Neutral Valuation**: In stochastic games, the value of a derivative incorporates equilibrium strategies of all players. The formula:
  \[
  V(s) = E_{\sigma^*}[r(s,a_1,\dots,a_n)] - \lambda \cdot C
  \]
  represents the derivative's value, factoring in transaction costs and time value of money.

- **Numerical Methods**: Solving Nash equilibria is computationally complex. Reinforcement learning (RL), particularly Q-learning, provides a scalable method for finding optimal strategies, even in unknown market environments.

## 4. Q-Learning Algorithm  
Q-learning adjusts strategies based on the rewards players receive. The Q-value update rule:
  \[
  Q_i(s,a_i) \leftarrow Q_i(s,a_i) + \alpha \left[ r(s,a_1,...,a_n) + \gamma \max_{a'_i} Q_i(s',a'_i) - Q_i(s,a_i) \right]
  \]
is used to iteratively refine strategies, converging to a Nash equilibrium.

## 5. Results  
The results show that applying stochastic game theory and Q-learning to derivative pricing models significantly enhances the understanding of strategic market interactions. By incorporating the players' differing objectives, the model reveals more dynamic pricing behavior than traditional zero-sum game models. The risk-neutral valuation and Nash equilibrium concepts provide a framework for optimising derivative pricing strategies, while reinforcement learning allows for scalable solution methods even with complex market environments. Although the assumptions of rationality and complete information may not fully capture real-world market complexities, the results demonstrate the potential for these models to improve predictive accuracy and guide strategic decision-making.

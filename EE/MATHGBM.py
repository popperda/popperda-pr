import numpy as np

# Define the initial parameters for the GBM formula
S0 = 15036.85   # initial price of NASDAQ index
mu = 0.1956    # expected rate of return
sigma = 0.2 # volatility
T = 10/365   # time horizon in years

# Define the number of simulations to run
num_simulations = 100
print(((mu - 0.5*sigma**2)*T))
# Define an array to store the simulated prices
simulated_prices = np.zeros(num_simulations)

# Run the simulations
for i in range(num_simulations):
    # Generate a random number from the Wiener process
    W = np.random.normal(0, np.sqrt(T))
    
    # Calculate the simulated price using the GBM formula
    simulated_prices[i] = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*W)

# Print the simulated prices
print("Simulated Prices:")
print(simulated_prices)

# Calculate the average price
avg_price = np.mean(simulated_prices)

# Print the average price
print("Average Price: {:.2f}".format(avg_price))
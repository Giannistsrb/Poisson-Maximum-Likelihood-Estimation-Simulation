import numpy as np 
import math as m 
import matplotlib.pyplot as plt

#CONFIDENCE LEVEL:
CL = 0.68

#Iterations (choose experiments = 1 for Exercise 1 and experiments = 1000 for Exercise 2):
experiments = 1000

#The real value of σ (in the exercise 2, the value is 10): 
σ_real = 10

#Accepted intervals are the intervals which contains the value σ = 10:
accepted = []

#σ values in [0, 20] (or [1, 20] in the first exercise) with step 0.02, for plotting:
σ = np.linspace(0, 20, 1000)

#Low limit x1(σ) from analytical Neyman solution:
def low_limit(sigma):
    return np.sqrt(-2 * np.power(sigma, 2) * m.log( (1+CL) / 2))

#Up limit x2(σ) from analytical Neyman solution:
def up_limit(sigma):
   return np.sqrt(-2 * np.power(sigma, 2) * m.log( (1-CL) / 2))

#Inverse rayleigh distribution for exercise 2 ( from CDF: F(x) = 1 - exp(-x^2/(2σ^2)) with 0<=F<=1 ) 
#to find the x_obs given a random number u in [0,1]: 
def inverse_rayleigh(sigma, F):
    x_obs = np.sqrt(-2 * sigma ** 2 * np.log(1-F))
    return x_obs

for _ in range(experiments):

    #We take a random observation (x_obs) for inverse Rayleigh distribution, with σ = 10:
    x_obs  = inverse_rayleigh(σ_real, np.random.uniform(0, 1))
    
    #The confidence band [σ1, σ2] values given the x_obs values in the experiments:
    σ1 = np.sqrt(- x_obs ** 2 / (2 * np.log((1+CL)/2)))
    σ2 = np.sqrt(- x_obs ** 2 / (2 * np.log((1-CL)/2)))

    if experiments == 1:
        #===================================================================================
        #Exercise 1:
        plt.figure(figsize=(8, 6))

        # Plotting lower and upper limits with labels
        plt.plot(low_limit(σ), σ, 'b-', linewidth=2, label="$x_1$")
        plt.plot(up_limit(σ), σ, 'r-', linewidth=2, label="$x_2$")

        # Filling the area between the curves
        plt.fill_betweenx(σ, low_limit(σ), up_limit(σ), color='lightgray', alpha=0.5, label='Confidence Belt')

        plt.xlabel("x", fontsize=14)
        plt.ylabel("σ", fontsize=14)
        plt.title("Confidence Belt for Rayleigh Distribution", fontsize=16)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.show()

        #===================================================================================
        #Exercise 2:
        #We care for the σ1,σ2 values ranged from 0 to 20:
        if σ1 <= 20 and σ2 <= 20: 
            print("x_obs = ",    x_obs)
            print("σ₁    = ",    σ1)
            print("σ₂    = ",    σ2)
            print("The confidence band for x_obs = ", x_obs, "is:")
            print(f"[σ₁(x_obs), σ₂(x_obs)] = [{σ1}, {σ2}]")

            plt.figure(figsize=(8, 6))
            plt.plot(low_limit(σ), σ, 'b-', linewidth=2, label="$x_1$")
            plt.plot( up_limit(σ), σ, 'r-', linewidth=2, label="$x_2$")
            plt.plot([x_obs, x_obs], [σ1, σ2], marker='o', markersize = 5, label=f"$σ_1$ and $σ_2$ values for x_obs = {x_obs:.3f}", color = 'black')
            plt.text(x_obs, σ1, f'$σ_1$={σ1:.2f}', ha='right', va='bottom', fontsize=10, color='black')
            plt.text(x_obs, σ2, f'$σ_2$={σ2:.2f}', ha='right', va='bottom', fontsize=10, color='black')
            plt.fill_betweenx(σ, low_limit(σ), up_limit(σ), color='lightgray', alpha=0.5, label='Confidence Belt')
            plt.xlabel("x", fontsize=14)
            plt.ylabel("σ", fontsize=14)
            plt.title("Confidence Belt for Rayleigh Distribution", fontsize=16)
            plt.legend(fontsize=12)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(True)
            plt.tight_layout()   
            plt.show()
    
    #Estimate the [σ1,σ2] intervals, which includes the real value σ = 10 (for exercise 2). We should think that σ1<=σ_real=<σ2:
    accept = 1  #Counter for accepted intervals is depicted with value "1"

    if σ2-σ_real <= 0 and σ1-σ_real >= 0: 
        accepted.append(accept)

#Estimation for Exercise 2:
if experiments > 1:
    #For the range of the experimets, we calculate the ratio of the intervals 
    #which don't include the real σ value (σ = 10):
    print(f"The ratio of the non-accepted intervals in {experiments} experiments is: ")
    print("NON_ACCEPTED_INTERVALS_RATIO = ", (1 - len(accepted) / experiments) * 100, " %")



    












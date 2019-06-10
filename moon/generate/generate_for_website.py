from moon.utils.load_data import load_climbset
from moon.models import lstm_gen

def main():
    # Load climbset
    climbset = load_climbset("2016")

    # Train generators
    lstm = lstm_gen.Model()
    lstm.train(climbset)

    # Sample generators
    climbs = lstm.sample()
    print(climbs)
    
    # Save to file

if __name__=="__main__":
    main()

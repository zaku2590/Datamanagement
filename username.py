import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def main():
    user_name = input("Who are you?\n> ")
    print(f"Hello, {user_name}!")
    
    print("Tossing a coin...")
    results = [coin_toss() for _ in range(3)]
    
    for i, result in enumerate(results, start=1):
        print(f"Round {i}: {result}")
    
    heads_count = results.count("Heads")
    tails_count = results.count("Tails")
    
    print(f"Heads: {heads_count}, Tails: {tails_count}")

if __name__ == "__main__":
    main()

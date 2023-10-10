from dataclasses import dataclass
import json
from team_info import process_csv_and_print_team_info

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"Person({self.first_name}, {self.last_name}, {self.age})"

    def __repr__(self) -> str:
        return f"Person({self.first_name}, {self.last_name}, {self.age})"
    
    def print_info(self):
        print(f"Person: {self.first_name} {self.last_name}, {self.age}")
        

    def full_name(self):
        """Return the full name of the person."""
        return f"{self.first_name} {self.last_name}"

    def birthday(self):
        """Increase the age of the person by 1."""
        self.age += 1
        return f"Happy Birthday, {self.first_name}! You are now {self.age} years old."
        
    def introduce(self):
        """Return a string introducing the person."""
        return f"Hello, my name is {self.full_name()} and I am {self.age} years old."

        

# Example usage:
john = Person("John", "Doe", 25)
print(john.introduce())   # "Hello, my name is John Doe and I am 25 years old."
print(john.birthday())    # "Happy Birthday, John! You are now 26 years old."
print(john.introduce())   # "Hello, my name is John Doe and I am 26 years old."



@dataclass
class BankAccount:
    account_number: str
    balance: float = 0.0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        return f"BankAccount({self.account_number}, {self.balance})"

    def __repr__(self) -> str:
        return f"BankAccount({self.account_number}, {self.balance})"
    

bankAccount = BankAccount("1234", 100)
bankAccount.deposit(100)
print(bankAccount.balance)
print(bankAccount.__str__())
print(bankAccount.__repr__())
bankAccount.withdraw(50)
print(bankAccount.balance)
print(bankAccount.withdraw(3000))
    


with open("C:\\Users\\luis.krumbacher\\OneDrive - Qualitest Group\\Documents\\Visual Studio 2022\\Code Snippets\\Python\\Github Copilot\\footballAPI\\config.json", "r") as f:
    config = json.load(f)

rapidapi_key = config["RAPIDAPI_KEY"]



def main():
    headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    file_path = "footballAPI/premier_league_teams.csv"
    
    process_csv_and_print_team_info(file_path, headers, url)


if __name__ == "__main__":
    #main()
    pass
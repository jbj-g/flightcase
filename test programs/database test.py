import json

def reset_data():
    default_data = {
        "calculations": [
            {
                "ProfileType": "7mm",
                "Values": [10, 10, 10, 10]
            }
        ]
    }

    with open('data.json', 'w') as file:
        json.dump(default_data, file)

# Main program loop
while True:
    user_input = input("Enter a command: ")
    
    if user_input == "reset":
        reset_data()
        print("Data reset to default.")
    elif user_input == "exit":
        break
    else:
        print("Invalid command. Type 'reset' to reset the data or 'exit' to quit.")

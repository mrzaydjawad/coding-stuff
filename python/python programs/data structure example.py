# Define a dictionary to store the story and choices
story_data = {
    'start': {
        'text': 'You find yourself in a dark forest. What do you do?',
        'choices': {
            '1': 'Explore deeper into the forest',
            '2': 'Follow a faint path to the right',
            '3': 'Clamber up a tree to get a better view'
        }
    },
    'explore_forest': {
        'text': 'As you explore deeper, you encounter a mysterious creature. What is your next move?',
        'choices': {
            '1': 'Try to communicate with the creature',
            '2': 'Retreat quietly',
            '3': 'Attack the creature'
        }
    },
    'tree_climb': {
        'text': 'From the top of the tree, you spot a distant castle. How do you proceed?',
        'choices': {
            '1': 'Head towards the castle',
            '2': 'Return to the forest floor',
            '3': 'Stay in the tree and observe'
        }
    }
}

# Function to present the story text and choices to the player
def present_story(stage):
    print(story_data[stage]['text'])
    print("Choices:")
    for choice_num, choice_text in story_data[stage]['choices'].items():
        print(f"{choice_num}: {choice_text}")

# Example usage
current_stage = 'start'
while current_stage:
    present_story(current_stage)
    user_choice = input("Enter your choice: ")
    if user_choice in story_data[current_stage]['choices']:
        current_stage = user_choice
    else:
        print("Invalid choice. Please try again.")

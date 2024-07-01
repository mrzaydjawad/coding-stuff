import os
from PIL import Image

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_image(image_path):
    clear_screen()
    image = Image.open(image_path)
    image.show()

def get_choice():
    return input("the story begins\n----------------\n(a)in your hometown\n(b)in a far off place\nYour choice (a/b): ").lower()

def main():
    while True:
        clear_screen()
        choice = get_choice()

        if choice == 'a':
            display_image('E:\\pics\\wallpaper.jpg')  # Replace 'image_a.jpg' with the path to your image for choice A
        elif choice == 'b':
            display_image('E:\\coding\\coding\\python\\python programs\\images\\backrooms   .png')  # Replace 'image_b.jpg' with the path to your image for choice B
        else:
            print("Invalid choice. Please select 'a' or 'b'.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()

from pet import Pet


def main():
    my_pet = Pet("Buddy")
    my_pet.get_status()

    print("\nFeeding Buddy...")
    my_pet.eat()
    my_pet.get_status()

    print("\nPlaying with Buddy...")
    my_pet.play()
    my_pet.get_status()

    print("\nPutting Buddy to sleep...")
    my_pet.sleep()
    my_pet.get_status()

    print("\nTraining Buddy...")
    my_pet.train("Roll Over")
    my_pet.train("Play Dead")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
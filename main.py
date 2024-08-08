
def create_user_profile():
  first_name = input("What is your first name? ")
  last_name = input("What is your last name? ")
  location = input("Where are you in the world? ")
  profile = {
      "First Name": first_name,
      "Last Name": last_name,
      "Location": location
  }
  return profile


def view_all_profiles(profiles):
  # TO DO


def update_profile(profiles, name_to_update, key_to_update, updated_value):
  # TO DO


if __name__ == "__main__":
  user_choice = None
  profiles = []

  while user_choice != "exit":
    user_choice = input(
        "Would you like to\n1. Create a new profile \n2. View all profiles \n3.Edit a profile\n"
    )

    if user_choice == "1":
      profiles.append(create_user_profile())

    if user_choice == "2":
      # TO DO
      print("This should print all the profiles in the list.")

    # TO DO: write a condition for the third option, to edit a profile. 
    # Hint: think about the data you'd need to update the profile, and where
    # you might find it...


# Json allows us to convert the accounts.txt dictionary to a usable one
import json


# extract info
def load_accounts():
    with open('accounts.txt') as f:
        return json.loads(f.read())  # return the dictionary as you read it from accounts.txt


# puts imformation into accounts.txt
def save_accounts(accounts):
    with open('accounts.txt', 'w') as f:
        f.write(json.dumps((accounts)))


def sign_up(accounts):
    username = input("Enter a new username: ")
    while username in accounts:
        username = input("Username already exists, please enter a different one: ")
    password = input("Enter a password: ")
    accounts[username] = {"password": password, "posts": []}
    save_accounts(accounts)
    print("Account sucessfully created!!!")


def login(accounts):
    username = input("Give me your username: ")
    password = input("Enter your password: ")
    if username in accounts and accounts[username]['password'] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid information please try again")
        return None


def post_status(accounts,username):
    posting = True
    while (posting):
        new_post = input("enter your status: (or write homepage to return to homepage): ")
        if (new_post == "homepage"):
            homePage(accounts, username)
        else:
            confirm = input(f"You are about to post: {new_post}. Press c to confirm or x to exit.")
            if (confirm == "c"):
                accounts[username]["posts"].append(new_post)
                save_accounts(accounts)
            else:
                posting = False
                homePage(accounts, username)
def edit_posts(accounts,username):
    posts = accounts[username]["posts"]
    while (True):
        editPost = int(input("What post would you like to edit: ")) - 1
        if (editPost in range(len(posts))):
            newEdit = input("What would you like to edit your post to: ")
            print(f"Editing {posts[editPost]} to {newEdit}")
            posts[editPost] = newEdit
            userChoice = input("Would you like to edit more posts? y/n")
            if (userChoice == "n"):
                break
def delete_posts(accounts, username):
    posts = accounts[username]["posts"]
    choice = input("Would you like to 1. delete a specific post or 2.clear all your posts:   (1/2) ")
    if choice == "2":
        posts.clear()
    elif choice == "1":
        while(True):
            deletePost = int(input("What post would you like to delete: ")) - 1
            if (deletePost in range(len(posts))):
                print(f"Deleting {posts[deletePost]}")
                del posts[deletePost]
                userChoice = input("Whould you like to delete more posts? y/n")
                if(userChoice == "n"):
                    break

    homePage(accounts,username)

def homePage(accounts, username):
    print(f"""
    ------------------------
    Welcome {username}
    ------------------------ 
    """)
    while True:
        print("""
        1. User can Post Status 👍
        2. View a status 😎
        3. Delete a post 🗑️
        4. Delete account
        5. Change Password
        6. Edit post
        7. Logout
        """)
        choice = input("Choice: ")
        match choice:
            case "1":
                post_status(accounts,username)
                break
            case "2":
                view_posts(accounts,username)
                break
            case "3":
                delete_posts(accounts, username)
                break
            case "4":
                delete_account(accounts,username)
                break
            case "5":
                change_password(accounts,username)
                break
            case "6":
                edit_posts(accounts,username)
                break
            case "7":
                main()
        break
def delete_account(accounts,username):
    confirmation = input("Warning: You are about to delete your account. Press C to confirm: ")
    if(confirmation == "c"):
        del accounts[username]
        save_accounts(accounts)
        print("Account deleted!")

def change_password(accounts,username):
    newPassword = input("Enter your new password: ")
    print("Currently saving password")
    accounts[username]["password"] = newPassword
    save_accounts(accounts)
    homePage(accounts, username)


def view_posts(accounts, username):
    posts = accounts[username]["posts"]
    if (len(posts)) == 0:
        print("No posts on this account!")
    else:
        for i in range(len(posts)):
            print(f"{i+1}, {posts[i]}")
    homePage(accounts,username)


def main():
    accounts = load_accounts()
    while True:
        print("WELCOME TO FACELOOK")
        action = input("Choose from the following options 1. signup, 2. login 3. exit: ")
        match action:
            case "1":
                sign_up(accounts)
            case "2":
                user = login(accounts)
                if user is not None:
                    homePage(accounts, user)
                    break
            case "exit":
                break


main()



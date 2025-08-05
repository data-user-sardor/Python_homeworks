# Homework 1. ToDo List Application
# Define Task class
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓ Completed" if self.completed else "✗ Incomplete"
        return f"\nTitle: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"

# Define ToDoList class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"\n✅ Task '{task.title}' added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"\n✅ Task '{title}' marked as complete.")
                return
        print(f"\n❌ Task titled '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks in the list.")
        else:
            print("\n📋 All Tasks:")
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            print("\n🎉 All tasks are complete!")
        else:
            print("\n⏳ Incomplete Tasks:")
            for task in incomplete:
                print(task)

# Main CLI Program
def main():
    todo = ToDoList()
    print("=== ToDo List CLI ===")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (e.g., 2025-07-15): ")
            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == '2':
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)

        elif choice == '3':
            todo.list_all_tasks()

        elif choice == '4':
            todo.list_incomplete_tasks()

        elif choice == '5':
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please choose 1–5.")

# Test the application
if __name__ == "__main__":
    # Automatically test some tasks before CLI starts
    test_todo = ToDoList()
    test_todo.add_task(Task("Buy Groceries", "Milk, Eggs, Bread", "2025-07-12"))
    test_todo.add_task(Task("Workout", "30-minute jog", "2025-07-11"))
    test_todo.add_task(Task("Read Book", "Finish Chapter 5", "2025-07-13"))
    test_todo.complete_task("Workout")

    print("---- Testing Tasks ----")
    print("All Tasks:")
    test_todo.list_all_tasks()
    print("\nIncomplete Tasks:")
    test_todo.list_incomplete_tasks()
    print("-----------------------")

    # Now start the interactive CLI
    main()

# Homework 2. Simple Blog System
# 1. Define Post Class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

# 2. Define Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"\n✅ Post '{post.title}' by {post.author} added.")

    def list_all_posts(self):
        if not self.posts:
            print("\n📭 No posts available.")
        else:
            print("\n📚 All Blog Posts:")
            for post in self.posts:
                print(post)

    def list_posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print(f"\n❌ No posts found by '{author}'.")
        else:
            print(f"\n📝 Posts by {author}:")
            for post in filtered:
                print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"\n🗑️ Post '{title}' deleted.")
                return
        print(f"\n❌ Post titled '{title}' not found.")

    def edit_post(self, title, new_title=None, new_content=None):
        for post in self.posts:
            if post.title.lower() == title.lower():
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print(f"\n✏️ Post '{title}' updated.")
                return
        print(f"\n❌ Post titled '{title}' not found.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("\n📭 No posts available.")
        else:
            print(f"\n🕒 Latest {min(count, len(self.posts))} Posts:")
            for post in self.posts[-count:][::-1]:
                print(post)

# 3. Main Program CLI
def main():
    blog = Blog()
    print("=== 📝 Simple Blog System ===")

    while True:
        print("\nMenu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == '2':
            blog.list_all_posts()

        elif choice == '3':
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)

        elif choice == '4':
            title = input("Enter title of post to delete: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Enter title of post to edit: ")
            new_title = input("Enter new title (or press Enter to skip): ")
            new_content = input("Enter new content (or press Enter to skip): ")
            blog.edit_post(title, new_title if new_title else None, new_content if new_content else None)

        elif choice == '6':
            try:
                count = int(input("How many latest posts to display? "))
            except ValueError:
                count = 3
            blog.display_latest_posts(count)

        elif choice == '7':
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-7.")

# Test the application
if __name__ == "__main__":
    # Create a Blog instance
    blog = Blog()

    # Create some Post instances
    post1 = Post("Welcome", "This is the welcome post.", "Admin")
    post2 = Post("Learning Python", "Python is easy to learn!", "Alice")
    post3 = Post("Daily Update", "Here's what happened today.", "Bob")
    post4 = Post("Advanced Python", "Decorators are powerful!", "Alice")

    # Add posts to the blog
    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)
    blog.add_post(post4)

    # List all posts
    print("\n=== All Posts ===")
    blog.list_all_posts()

    # Display posts by a specific author
    print("\n=== Posts by Alice ===")
    blog.posts_by_author("Alice")

    # Display posts by a non-existent author
    print("\n=== Posts by John ===")
    blog.posts_by_author("John")

# Homework 3. Simple Banking System
# 1. Define Account Class
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"✅ Deposited ${amount:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"❌ Insufficient funds in account {self.account_number}. Available balance: ${self.balance:.2f}")
            return False
        self.balance -= amount
        print(f"✅ Withdrawn ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
        return True

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder Name: {self.holder_name}\nBalance: ${self.balance:.2f}\n"

# 2. Define Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print(f"❌ Account {account.account_number} already exists.")
            return False
        self.accounts[account.account_number] = account
        print(f"✅ Account {account.account_number} added for {account.holder_name}.")
        return True

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"💰 Balance for account {account_number}: ${account.balance:.2f}")
        else:
            print(f"❌ Account {account_number} not found.")

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"❌ Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"❌ Account {account_number} not found.")

    # 4. Enhanced functionalities

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)
        if not from_acc:
            print(f"❌ From-account {from_acc_num} not found.")
            return
        if not to_acc:
            print(f"❌ To-account {to_acc_num} not found.")
            return
        if amount <= 0:
            print("❌ Transfer amount must be positive.")
            return
        if from_acc.balance < amount:
            print(f"❌ Insufficient funds in account {from_acc_num}. Transfer cancelled.")
            return
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"✅ Transferred ${amount:.2f} from account {from_acc_num} to {to_acc_num}.")

    def display_account_details(self, account_number):
        account = self.get_account(account_number)
        if account:
            print("\n📄 Account Details:")
            print(account)
        else:
            print(f"❌ Account {account_number} not found.")

    def handle_overdraft(self, account_number, overdraft_limit):
        """Allow withdrawal even if it causes balance to go below zero, up to overdraft_limit"""
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found.")
            return False

        def withdraw_with_overdraft(amount):
            if amount <= 0:
                print("❌ Withdrawal amount must be positive.")
                return False
            if account.balance - amount < -overdraft_limit:
                print(f"❌ Overdraft limit exceeded. Max allowed overdraft: ${overdraft_limit:.2f}")
                return False
            account.balance -= amount
            print(f"✅ Withdrawn ${amount:.2f} with overdraft. New balance: ${account.balance:.2f}")
            return True

        return withdraw_with_overdraft

# 3. Main Program CLI
def main():
    bank = Bank()
    print("=== 🏦 Simple Banking System ===")

    overdraft_limit = 500  # example overdraft limit

    while True:
        print("\nMenu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Withdraw with Overdraft")
        print("8. Exit")

        choice = input("Choose an option (1–8): ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            holder = input("Enter account holder name: ")
            try:
                balance = float(input("Enter initial balance (default 0): ") or 0)
            except ValueError:
                balance = 0.0
            account = Account(acc_num, holder, balance)
            bank.add_account(account)

        elif choice == '2':
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == '3':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("❌ Invalid amount.")
                continue
            bank.deposit(acc_num, amount)

        elif choice == '4':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("❌ Invalid amount.")
                continue
            bank.withdraw(acc_num, amount)

        elif choice == '5':
            from_acc = input("Enter FROM account number: ")
            to_acc = input("Enter TO account number: ")
            try:
                amount = float(input("Enter transfer amount: "))
            except ValueError:
                print("❌ Invalid amount.")
                continue
            bank.transfer(from_acc, to_acc, amount)

        elif choice == '6':
            acc_num = input("Enter account number: ")
            bank.display_account_details(acc_num)

        elif choice == '7':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("❌ Invalid amount.")
                continue
            withdraw_with_overdraft = bank.handle_overdraft(acc_num, overdraft_limit)
            if withdraw_with_overdraft:
                withdraw_with_overdraft(amount)

        elif choice == '8':
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1–8.")

# Test the application
if __name__ == "__main__":
    main()
def test_banking_system():
    print("=== Running Banking System Tests ===")

    bank = Bank()

    # Create accounts
    acc1 = Account("1001", "Alice", 1000)
    acc2 = Account("1002", "Bob", 500)
    acc3 = Account("1003", "Charlie")

    # Add accounts to bank
    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)

    # Check balances
    bank.check_balance("1001")
    bank.check_balance("1002")
    bank.check_balance("1003")  # Should be zero

    # Deposit money
    bank.deposit("1003", 300)

    # Withdraw money
    bank.withdraw("1001", 200)
    bank.withdraw("1002", 600)  # Should fail (insufficient funds)

    # Transfer money
    bank.transfer("1001", "1003", 400)
    bank.transfer("1002", "1003", 100)  # Bob has 500 initially

    # Display account details
    bank.display_account_details("1001")
    bank.display_account_details("1003")

    # Overdraft withdrawal test
    overdraft_limit = 500
    withdraw_with_overdraft = bank.handle_overdraft("1002", overdraft_limit)
    if withdraw_with_overdraft:
        withdraw_with_overdraft(700)  # Should be allowed up to overdraft limit

    # Final balances
    bank.check_balance("1001")
    bank.check_balance("1002")
    bank.check_balance("1003")

    print("=== Tests Completed ===")

# Run tests if this file is run directly
if __name__ == "__main__":
    test_banking_system()


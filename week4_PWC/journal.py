import random
import datetime

class DiaryEntry:
    def __init__(self, prompt, response):
        self.prompt = prompt
        self.response = response
        self.date = datetime.datetime.now()

class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self):
        prompts = [
           "What was the first thought you had when you woke up this morning?"
           "What was the most important task you completed today?"
           "What did you do to take care of your physical well-being today?"
           "What was the most significant or outstanding moment of your day?"
           "What made you laugh or smile today?"
           "What obstacles or challenges did you face today and how did you overcome them?"
           "What did you learn today that you didn't know before?"
           "What was the act of kindness or help you gave someone today?"
           "What was the most stressful or frustrating moment you experienced today and how did you handle it?"
           "What was the last thing you did before going to sleep and how did it make you feel?"
        ]

        prompt = random.choice(prompts)
        response = input(prompt + ": ")

        entry = DiaryEntry(prompt, response)
        self.entries.append(entry)

    def show_entries(self):
        for entry in self.entries:
            print("Date:", entry.date)
            print("Question:", entry.prompt)
            print("Answer:", entry.response)
            print()

    def save_to_file(self, filename):
        with open(filename+".txt", "w") as file:
            for entry in self.entries:
                file.write(str(entry.date) + "\n")
                file.write(entry.prompt + "\n")
                file.write(entry.response + "\n")
                file.write("\n")

    def load_from_file(self, filename):
        self.entries = []

        with open(filename, "r") as file:
            lines = file.readlines()

            for i in range(0, len(lines), 4):
                date_str = lines[i].strip()
                prompt = lines[i + 1].strip()
                response = lines[i + 2].strip()

                try:
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
                    entry = DiaryEntry(prompt, response)
                    entry.date = date
                    self.entries.append(entry)
                except ValueError:
                    print("Error loading file. wrong date format.")
                    break

def main():
    diary = Diary()

    while True:
        print("MAIN:")
        print("1. WRITE")
        print("2. DISPLAY")
        print("3. LOAD")
        print("4. SAVE")
        print("5. QUIT")

        option = input("What Would do you like to d0?: ")

        if option == "1":
            diary.add_entry()
        elif option == "2":
            diary.show_entries()
        elif option == "3":
            filename = input("Enter the file name: ")
            diary.save_to_file(filename)
        elif option == "4":
            filename = input("Enter the file name: ")
            diary.load_from_file(filename)
        elif option == "5":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
{% include navigation.html %}
<a href="https://github.com/peacekeeper6/Jun-CSP-Project">Link to GitHub Repository for code</a>

<iframe height="800px" width="100%" src="https://replit.com/@TWIYJun/Jun-CSP-Project?lite=true"></iframe>


````
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({ 
               "Book_Title": "Outliers",  
               "Author": "Malcolm Gladwell",
               "Genre": "Nonfiction",
               "Published": "11/18/2008",  
               "Author_Books":["The Bomber Mafia", "What the Dog Saw", "Blink", "David and Goliath", "Talking to Strangers"]  
              })  
InfoDb.append({  
               "Book_Title": "Ready Player One",  
               "Author": "Ernest Cline",
               "Genre": "Science Fiction",
               "Published": "8/16/2011",  
               "Author_Books":["Ready Player Two", "Armada: A Novel", "The Importance of Being Ernest"]   
              })  
InfoDb.append({  
               "Book_Title": "Three Days of Happiness",  
               "Author": "Sugaru Miaki",
               "Genre": "Fiction",
               "Published": "12/25/2013",  
               "Author_Books":["Your Story", "The Place You Called From", "Parasite in Love", "Starting Over", "Pain, Pain, Go Away"]   
              })  
InfoDb.append({  
               "Book_Title": "No Longer Human",  
               "Author": "Osamu Dazai",
               "Genre": "Autobiographical Fiction",
               "Published": "1948 (No specific date)",  
               "Author_Books":["The Setting Sun", "Good Bye", "One Hundred Views of Mount Fuji", "The Late Years"]   
              })  


def print_data(n):
    print(InfoDb[n]["Book_Title"], "by", InfoDb[n]["Author"])  # using comma puts space between values
    print("\t", "Genre: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Genre"]))  # join allows printing a string list with separator
    print("\t", "Another book by the Author: ", end="")
    print(InfoDb[n].get("Author_Books")[0])
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
  
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
  print('*' * 10)
  print("For loop")
  print('*' * 10)
  for_loop()
  print('*' * 10)
  print("While loop")
  print('*' * 10)
  while_loop(0)
  print('*' * 10)
  print("Recursive loop")
  print('*' * 10)
  recursive_loop(0)

if __name__ == "__main__":
  tester()
  
  ````

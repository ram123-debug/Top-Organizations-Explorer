import json
import requests

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Hello, User')

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
n_var = tk.StringVar()
m_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen

def Sort_Tuple(repo_fork):  # sort the list of tuples in descending order
    repo_fork.sort(key=lambda x: x[1], reverse=True)
    return repo_fork
def fetch():
    orgname = orgchoosen
    number_of_repo = n_var.get()
    number_of_committees = m_var.get()
# orgname = input("Organisation:")                                                #Organisation name input
# number_of_repo = int(input("Enter number n:"))                                  #n no of popular repos
# number_of_committees = int(input("Enter number m:"))                             #oldest forkers
    repo_fork = []

    for i in range(1, 20):
        params = {'page': i, 'per_page': 100}
        # Requesting API from GitHub to access organisation name
        r = requests.get('https://api.github.com/orgs/' +
                     orgname+'/repos', params=params)
        todos = json.loads(r.text)  # reading json file for r
        repo_fork.extend([(sub['full_name'], sub['forks_count']) for sub in todos])
        if(len(repo_fork) < i*100):
          break

    Sort_Tuple(repo_fork)
    k = 1

    for i in repo_fork[0:number_of_repo]:
       print(k, i[0], " ", "Fork counts:", i[1])
       k += 1
       l = requests.get('https://api.github.com/repos/' +
                     i[0]+'/contributors')  # accesing repositories
       temp = json.loads(l.text)  # reading json file for l
       # contributors_commits = [(sub['login'],sub['contributions']) for sub in temp]
       individual_commits = [(sub['login'], sub['contributions']) for sub in temp]
       Sort_Tuple(individual_commits)
       m = 1
       for j in individual_commits[0:number_of_committees]:
        data={'Git id:', m, j[0]}
        m += 1
        print(m)
        print(j[0])
        print()
        print()

    # print("N (Top Repos) : " +N)
    # print("M (Oldest Forkers) : " + M)

   


ttk.Label(root, text="Top Organisations Repositories Explorer",
          foreground="blue",
          font=("Times New Roman", 15)).grid(row=0, column=1)


ttk.Label(root, text="Select the Organisation :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)

n = tk.StringVar()
orgchoosen = ttk.Combobox(root, width=27, textvariable=n)

# # Adding combobox drop down list
orgchoosen['values'] = (' Facebook',
                        'Google',
                        'Microsoft')

orgchoosen.grid(column=1, row=5)
orgchoosen.current()
# creating a label for
# name using widget Label
n_label = tk.Label(root, text='N(Top Repos)', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
n_entry = tk.Entry(root, textvariable=n_var, font=('calibre', 10, 'normal'))

# creating a label for m
m_label = tk.Label(root, text='M(Oldest Forkers)',
                   font=('Times New Roman', 10, 'bold'))

# creating a entry for m
m_entry = tk.Entry(root, textvariable=m_var,
                   font=('Times New Roman', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Fetch', command=fetch)

# placing the label and entry in
# the required position using grid
# method
n_label.grid(row=5, column=4)
n_entry.grid(row=5, column=5)
m_label.grid(row=5, column=8)
m_entry.grid(row=5, column=9)
sub_btn.grid(row=9, column=4)

# performing an infinite loop
# for the window to display
root.mainloop()

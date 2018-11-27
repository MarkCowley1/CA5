
# coding: utf-8

# In[7]:


# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:17:14 2018

@author: markc
"""
import pandas as pd

class Commit(object): # As done in class, setting up instance variables.
    def __init__(self, revision, author, date, time, number_of_lines, changed_path=[], comment=[]):
        self.revision = revision
        self.author = author
        self.date = date
        self.time = time
        self.number_of_lines = number_of_lines
        self.changed_path = changed_path
        self.comment = comment
        self.modified = 0
        self.deleted = 0
        self.added = 0

    def __repr__(self):
        return self.revision + ',' + self.author +                 ',' + self.date + ',' + self.time + ',' + str(self.number_of_lines) + 				',' + ' '.join(self.comment) + '\n'
    
    def commit_dict(self): #Adding a dictionary which will be needed for later to get some statistical information
        return {'Revision': self.revision, 
                'Author': self.author,
                'Date': self.date,
                'Number of Lines': self.number_of_lines,
                'Comment': self.comment,
                'Changed Path': self.changed_path,
                'Added': self.added,
                'Modified': self.modified,
                'Deleted': self.deleted}

def get_commits(data):
    sep = 72*'-' #72 dashes between each entry in our log file.
    commits = [] #Empty list where the data we parse will go.
    index = 0
    while index < len(data): #while loop keeps going for length of log file
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = Commit(details[0].strip(), #cleaning up our data below, removing white spaces.
                details[1].strip(),
                details[2].strip().split(' ')[0],
                details[2].strip().split(' ')[1],
                int(details[3].strip().split(' ')[0]))
            change_file_end_index = data.index('', index + 1)
            commit.changed_path = data[index + 3 : change_file_end_index]
            commit.comment = data[change_file_end_index + 1 : 
                    change_file_end_index + 1 + commit.number_of_lines]
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
            
            for path in commit.changed_path: #Here adding information about whether commits were modified, added or deleted.
                path = path.split(' ')
                if path[0] == 'M':
                    commit.modified += 1
                if path[0] == 'A':
                    commit.added += 1
                if path[0] == 'D':
                    commit.deleted += 1
        
        except IndexError:
            index = len(data)
    return commits

def read_file(any_file):
    # use strip to strip out spaces and trim the line.
        data = [line.strip() for line in open(any_file, 'r')]
        return data

def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("revision,author,date,time,number_of_lines,comment\n")
    for commit in commits:
        my_file.write(str(commit))
    my_file.close()

def Mydataframe(commits):
    #change the format of the date so it is compatible in a dataframe
    myDf = pd.DataFrame([i.commit_dict() for i in commits])
    myDf['Date'] = pd.to_datetime(myDf['Date'], format='%Y-%m-%d %H:%M:%S')
    return myDf


if __name__ == '__main__':
    changes_file = "changes_python.log"
    data = read_file(changes_file)
    print(len(data))
    print(len(commits))
    print(commits[0])
    print(commits[0].author)

    commits = get_commits(data)
    df_commits = Mydataframe(commits)
    
    

    
    
    
    
    
    


# In[8]:


df_commits.groupby('Author').nunique() #Here we get a lot of statistical information such as the list of authors and how much adding, deleting and modiying was done by each author.


# importing necessary libraries
from bs4 import BeautifulSoup
import os

# initializing lists
likes = []
comments = []
file_name = ""

# reading the data from list.txt
with open("list.txt","r") as f:
    data = f.read().split(",")

# delete the output.txt file if it exists
if os.path.exists("output.txt"):
    os.remove("output.txt")

# function to write the data in the lists
def data_write(html_content):
    i = 0
    soup = BeautifulSoup(html_content, 'html.parser')

    element = soup.find_all(class_=['_abpm'])

    for value in element:
        value = value.text
        value = value.replace(",","")
        if value[-1] == "K":
            value = float(value[:-1])*1000
        elif value[-1] == "M":
            value = float(value[:-1])*1000000
        else:
            value = float(value)
        if i%2 == 0:
            likes.append(value)
        else:
            comments.append(value)
        i+=1

# function to write the file name in output.txt
def file_writer(likes,comments,file_name):
    for i,j in zip(likes,comments):
        if i > float(data[0]) and j > float(data[1]):
            with open("output.txt","a+") as f:
                f.write(file_name+"\n")
                break

# iterating over the files in files folder
for file in os.listdir("files"):
    with open(f"files/{file}","r") as f:
        html_content = f.read()
        data_write(html_content)
        file_writer(likes,comments,file[:-4])
        likes = []
        comments = []
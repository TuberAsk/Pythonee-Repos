# Recommeneded Librarys!
import discord
import os
# Some Starter Code!
 print("Hello World!")
 # Also some Def Functions!
 # Python3 code to demonstrate
# def keyword

# function for subtraction of 2 numbers
def subNumbers(x, y):
return (x-y)

# main code
a = 90
b = 50

# finding subtraction
result = subNumbers(a, b)

# print statement
print("subtraction of ", a, " and ", b, " is = ", result)

#That code is not mine but it is a example of a def function!
#To start of with a discord bot you will need Visual Studio Code and discord.py 2.2.2 or any other versions!
import discord #Imports the discord module.
from discord.ext import commands #Imports discord extensions.

#The below code verifies the "client".
intents = discord.Intents().all()
client = commands.Bot(command_prefix='?', intents=intents)
client.run("YOUR BOT TOKEN!")

#Just a simple starter script for you bot to make it online!
#Check out Pythoneer on YouTube!

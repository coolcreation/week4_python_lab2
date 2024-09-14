#!/usr/bin/env python3
# Jeff Bohn
# 9/13/2024
# Week 4 Lab 2 - How to Handle Exceptions

########## Exercise 8_2 ##########  


import csv
import sys

FILENAME = "movies.csv"


def yearValidation():
    while True:
        try:
            year = int(input("Enter the year: ")) 
            if year > 0: 
                return year  
            else:
                print('Enter an Integer more that zero')
        except ValueError as e:
            print("That's not an Integer, try again", e) 


def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        # print(f"Could not find {FILENAME} file.")
        # exit_program()
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            #raise BlockingIOError("Blocking IO Error")
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e:
        print("OSError:", e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    name = input("Name: ")
    year = yearValidation()
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

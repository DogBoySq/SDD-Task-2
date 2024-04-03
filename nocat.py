import tkinter as tk
import random 

# Global variable for the array
simarray1 = [12, 19, 23, 32, 42, 54]

# Global variable for bubble_sort_array_label
bubble_sort_array_label = None

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to sort the array
def sort_array():
    bubble_sort(simarray1)
    update_bubble_sort_display()

# Function to shuffle the array
def shuffle_array():
    random.shuffle(simarray1)
    update_bubble_sort_display()

# Function to update the array display in Bubble Sort page
def update_bubble_sort_display():
    global bubble_sort_array_label
    if bubble_sort_array_label:
        bubble_sort_array_label.config(text="Array: " + ", ".join(map(str, simarray1)))

# Function to perform Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to handle binary search button click
def binary_search_handler():
    if simarray1 != sorted(simarray1):
        result_label.config(text="Please sort the array first in Bubble Sort.")
        return
    try:
        target = int(user_input_entry.get())
        index = binary_search(simarray1, target)
        if index != -1:
            result_label.config(text=f"Element {target} found at index {index}.")
        else:
            result_label.config(text=f"Element {target} not found in the array.")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

# Function to show the Binary Search page
def show_binary_search_page():
    main_page_frame.pack_forget()
    bubble_sort_page_frame.pack_forget()
    binary_search_page_frame.pack()
    update_binary_search_display()

# Function to update the array display in Binary Search page
def update_binary_search_display():
    binary_search_array_label.config(text="Array: " + ", ".join(map(str, simarray1)))

# Function to show the Bubble Sort page
def show_bubble_sort_page():
    main_page_frame.pack_forget()
    binary_search_page_frame.pack_forget()
    bubble_sort_page_frame.pack()
    update_bubble_sort_display()

# Function to show the Main page
def show_main_page():
    bubble_sort_page_frame.pack_forget()
    binary_search_page_frame.pack_forget()
    main_page_frame.pack()

# Shuffle the array initially
shuffle_array()

# Main window
root = tk.Tk()
root.title("SDD Task 1")
root.geometry("500x500")
root.configure(bg="white")

# Main page frame
main_page_frame = tk.Frame(root, bg="white")

# Creating a title for Main page
main_title = tk.Label(main_page_frame, text="SDD Task 2", font=("Helvetica", 20), bg="white")
main_title.pack(pady=20)

# Button to go to Bubble Sort page
bubble_sort_button = tk.Button(main_page_frame, text="Bubble Sort", command=show_bubble_sort_page)
bubble_sort_button.pack(pady=10)

# Binary Search page frame
binary_search_page_frame = tk.Frame(root, bg="white")

# Creating a title for Binary Search page
binary_search_title = tk.Label(binary_search_page_frame, text="Binary Search Page", font=("Helvetica", 20), bg="white")
binary_search_title.pack(pady=20)

# Display the array
binary_search_array_label = tk.Label(binary_search_page_frame, text="Array: " + ", ".join(map(str, simarray1)), font=("Arial", 12), bg="white")
binary_search_array_label.pack(pady=5)

# User input box
user_input_label = tk.Label(binary_search_page_frame, text="Enter a number to search:", font=("Arial", 12), bg="white")
user_input_label.pack()
user_input_entry = tk.Entry(binary_search_page_frame, width=20)
user_input_entry.pack(pady=5)

# Search button
search_button = tk.Button(binary_search_page_frame, text="Search", command=binary_search_handler)
search_button.pack(pady=5)

# Result label
result_label = tk.Label(binary_search_page_frame, text="", font=("Arial", 12), bg="white")
result_label.pack(pady=5)

# Button to go to Bubble Sort page from Binary Search
binary_to_bubble_button = tk.Button(binary_search_page_frame, text="Go to Bubble Sort", command=show_bubble_sort_page)
binary_to_bubble_button.pack(pady=10)

# Button to go to Main page from Binary Search
binary_to_main_button = tk.Button(binary_search_page_frame, text="Go to Main Page", command=show_main_page)
binary_to_main_button.pack(pady=10)

# Bubble Sort page frame
bubble_sort_page_frame = tk.Frame(root, bg="white")

# Creating a title for Bubble Sort page
bubble_sort_title = tk.Label(bubble_sort_page_frame, text="Bubble Sort Page", font=("Helvetica", 20), bg="white")
bubble_sort_title.pack(pady=20)

# Display the array
bubble_sort_array_label = tk.Label(bubble_sort_page_frame, text="Array: " + ", ".join(map(str, simarray1)), font=("Arial", 12), bg="white")
bubble_sort_array_label.pack(pady=5)

# Sort button
sort_button = tk.Button(bubble_sort_page_frame, text="Sort", command=sort_array)
sort_button.pack(pady=5)

# Shuffle button
shuffle_button = tk.Button(bubble_sort_page_frame, text="Shuffle", command=shuffle_array)
shuffle_button.pack(pady=5)

# Button to go to Binary Search page from Bubble Sort
bubble_to_binary_button = tk.Button(bubble_sort_page_frame, text="Go to Binary Search", command=show_binary_search_page)
bubble_to_binary_button.pack(pady=10)

# Button to go to Main page from Bubble Sort
bubble_to_main_button = tk.Button(bubble_sort_page_frame, text="Go to Main Page", command=show_main_page)
bubble_to_main_button.pack(pady=10)

# Show Main page initially
show_main_page()

root.mainloop()

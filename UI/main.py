import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Function to simulate file upload
def upload_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    if file_path:
        messagebox.showinfo("File Upload", f"File uploaded successfully: {file_path}")

# Function to simulate file download
def download_template():
    messagebox.showinfo("Download Template", "Data template downloaded successfully.")

# Function to simulate data merge
def merge_data():
    messagebox.showinfo("Merge Data", "Data merged successfully.")

# Function to add metadata to the table
def add_metadata_to_table():
    # Collect data from the metadata fields
    metadata_values = [
        entries['Dataset ID'].get(),
        entries['Experiment Date'].get(),
        entries['Sample Matrix'].get(),
        entries['Fraction'].get(),
        entries['Reliability Evaluation'].get(),
        entries['Reliability Score'].get(),
        entries['Data Source'].get(),
        category_combobox.get(),
        genus_combobox.get(),
        gender_combobox.get(),
        lifestage_combobox.get(),
        species_comment_entry.get()
    ]

    # Insert data into the Treeview table
    tree.insert('', 'end', values=metadata_values)

# Creating the main window
root = tk.Tk()
root.title("Data Entry Interface")
root.geometry("1200x600")

# Header Section
header_frame = tk.Frame(root)
header_frame.pack(fill=tk.X)

btn_main = tk.Button(header_frame, text="Main", width=10)
btn_main.pack(side=tk.LEFT, padx=10, pady=5)

btn_documentation = tk.Button(header_frame, text="Documentation", width=15)
btn_documentation.pack(side=tk.LEFT, padx=10, pady=5)

# Metadata Section
metadata_frame = tk.LabelFrame(root, text="Metadata", padx=10, pady=10)
metadata_frame.pack(fill=tk.X, padx=10, pady=10)

# Left section - Existing Metadata Fields
labels = ['Dataset ID', 'Experiment Date', 'Sample Matrix', 'Fraction', 'Reliability Evaluation', 'Reliability Score', 'Data Source']
entries = {}

for idx, label in enumerate(labels):
    tk.Label(metadata_frame, text=label).grid(row=idx, column=0, sticky=tk.W, padx=5, pady=5)
    entry = tk.Entry(metadata_frame, width=30)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[label] = entry

# Right section - New form fields based on image
right_start_row = 0  # Start at the same row as Dataset ID but in a different column

tk.Label(metadata_frame, text="Choose category").grid(row=right_start_row, column=2, sticky=tk.W, padx=10, pady=5)
category_combobox = ttk.Combobox(metadata_frame, values=["Species", "Assay", "Other"], state="readonly")
category_combobox.grid(row=right_start_row, column=3, padx=5, pady=5)

tk.Label(metadata_frame, text="Genus").grid(row=right_start_row+1, column=2, sticky=tk.W, padx=10, pady=5)
genus_combobox = ttk.Combobox(metadata_frame, values=["Homo", "Pan", "Canis", "Felis"], state="readonly")
genus_combobox.grid(row=right_start_row+1, column=3, padx=5, pady=5)

tk.Label(metadata_frame, text="Species gender").grid(row=right_start_row+2, column=2, sticky=tk.W, padx=10, pady=5)
gender_combobox = ttk.Combobox(metadata_frame, values=["Male", "Female", "Unknown"], state="readonly")
gender_combobox.grid(row=right_start_row+2, column=3, padx=5, pady=5)

tk.Label(metadata_frame, text="Lifestage").grid(row=right_start_row+3, column=2, sticky=tk.W, padx=10, pady=5)
lifestage_combobox = ttk.Combobox(metadata_frame, values=["Juvenile", "Adult", "Old"], state="readonly")
lifestage_combobox.grid(row=right_start_row+3, column=3, padx=5, pady=5)

tk.Label(metadata_frame, text="Species Comment").grid(row=right_start_row+4, column=2, sticky=tk.W, padx=10, pady=5)
species_comment_entry = tk.Entry(metadata_frame, width=30)
species_comment_entry.grid(row=right_start_row+4, column=3, padx=5, pady=5)

# Button for adding metadata to table
add_button = tk.Button(metadata_frame, text="Add Metadata to Table", command=add_metadata_to_table)
add_button.grid(row=right_start_row+5, column=2, columnspan=2, pady=10)

# Download/Upload Data Section
upload_frame = tk.LabelFrame(root, text="Download/Upload Data", padx=10, pady=10)
upload_frame.pack(fill=tk.BOTH, padx=10, pady=10)

btn_download = tk.Button(upload_frame, text="Download Data Template", command=download_template)
btn_download.grid(row=0, column=0, padx=5, pady=5)

btn_upload = tk.Button(upload_frame, text="Upload Data", command=upload_file)
btn_upload.grid(row=0, column=1, padx=5, pady=5)

# Treeview for displaying uploaded and metadata data
columns = ['Dataset ID', 'Experiment Date', 'Sample Matrix', 'Fraction', 'Reliability Eval', 'Reliability Score',
           'Data Source', 'Category', 'Genus', 'Gender', 'Lifestage', 'Species Comment']
tree = ttk.Treeview(upload_frame, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)  # Adjust column width as needed

tree.grid(row=1, column=0, columnspan=2, pady=10)

# Data Merge and Submit Section
submit_frame = tk.LabelFrame(root, text="Data Merge and Submit", padx=10, pady=10)
submit_frame.pack(fill=tk.X, padx=10, pady=10)

btn_merge = tk.Button(submit_frame, text="Merge data and metadata", command=merge_data)
btn_merge.grid(row=0, column=0, padx=5, pady=5)

btn_download_results = tk.Button(submit_frame, text="Download results")
btn_download_results.grid(row=0, column=1, padx=5, pady=5)

btn_expand_table = tk.Button(submit_frame, text="Expand table")
btn_expand_table.grid(row=0, column=2, padx=5, pady=5)

btn_save_work = tk.Button(submit_frame, text="Save your work")
btn_save_work.grid(row=0, column=3, padx=5, pady=5)

tk.Label(submit_frame, text="E-mail address:").grid(row=1, column=0, sticky=tk.W, pady=5)
email_entry = tk.Entry(submit_frame, width=40)
email_entry.grid(row=1, column=1, columnspan=3, pady=5)

# Run the Tkinter loop
root.mainloop()
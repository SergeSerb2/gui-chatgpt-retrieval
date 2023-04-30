import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import time

def set_environment_variables(datastore, env_vars):
    for var_name, var_value in env_vars.items():
        os.environ[var_name] = var_value

def vectorize_and_upload_docs(datastore, docs_path):
    subprocess.Popen(["python", "vectorizeAndUploadDocs.py", datastore, docs_path])

        
def run_plugin_server():
    subprocess.Popen(["poetry", "run", "dev"])


def submit():
    datastore = datastore_var.get()
    if datastore == "Select a datastore":
        messagebox.showerror("Error", "Please select a datastore.")
        return

    env_vars = {
        "DATASTORE": datastore.lower(),
        "BEARER_TOKEN": bearer_token_entry.get().strip(),
        "OPENAI_API_KEY": openai_api_key_entry.get().strip(),
    }

    if "" in env_vars.values():
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    additional_env_vars = {}
    for field, entry in entries.items():
        if field.startswith(datastore.upper()):
            value = entry.get().strip()
            if value == "":
                messagebox.showerror("Error", "Please fill in all required fields.")
                return
            additional_env_vars[field] = value

    env_vars.update(additional_env_vars)
    set_environment_variables(datastore, env_vars)

    docs_path = filedialog.askdirectory(title="Select the folder where your documents are stored")
    if not docs_path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    
    messagebox.showinfo("Warning!", "If index hasn't been created yet, an error is likely to occur. Simply rerun the program once index is created and no issues should persist")

    run_plugin_server()
    vectorize_and_upload_docs(datastore, docs_path)

    messagebox.showinfo("Server Running", "The retrieval plugin server is running at 'localhost:3333'")


def update_fields(*args):
    selected_datastore = datastore_var.get()
    if selected_datastore == "Select a datastore":
        for label in labels.values():
            label.grid_forget()
        for entry in entries.values():
            entry.grid_forget()
    else:
        for field, entry in entries.items():
            if field.startswith(selected_datastore.upper()):
                entry.grid(row=field_positions[field], column=1)
                labels[field].grid(row=field_positions[field], column=0)  # Show the label
            else:
                entry.grid_forget()
                labels[field].grid_forget()  # Hide the label


root = tk.Tk()
root.title("Chat-GPT-Retrieval Plugin Setup")

datastore_options = ["Pinecone", "Weaviate", "Zilliz", "Milvus", "Qdrant", "Redis"]

datastore_var = tk.StringVar(root)
datastore_var.set("Select a datastore")  # Set the initial value to "Select a datastore"
datastore_var.trace("w", update_fields)

bearer_token_label = tk.Label(root, text="OpenAI API Key:")
bearer_token_label.grid(row=0, column=0)
bearer_token_entry = tk.Entry(root)
bearer_token_entry.grid(row=0, column=1)

openai_api_key_label = tk.Label(root, text="Bearer Token:")
openai_api_key_label.grid(row=1, column=0)
openai_api_key_entry = tk.Entry(root)
openai_api_key_entry.grid(row=1, column=1)

datastore_label = tk.Label(root, text="Datastore:")
datastore_label.grid(row=2, column=0)
datastore_optionmenu = tk.OptionMenu(root, datastore_var, "Select a datastore", *datastore_options)
datastore_optionmenu.grid(row=2, column=1)

field_positions = {
    "PINECONE_API_KEY": 3,
    "PINECONE_ENVIRONMENT": 4,
    "PINECONE_INDEX": 5,
    "WEAVIATE_HOST": 3,
    "WEAVIATE_PORT": 4,
    "WEAVIATE_USERNAME": 5,
    "WEAVIATE_PASSWORD": 6,
    "WEAVIATE_CLASS": 7,
        "WEAVIATE_SCOPES": 8,
    "WEAVIATE_BATCH_SIZE": 9,
    "WEAVIATE_BATCH_DYNAMIC": 10,
    "WEAVIATE_BATCH_TIMEOUT_RETRIES": 11,
    "WEAVIATE_BATCH_NUM_WORKERS": 12,
    "ZILLIZ_COLLECTION": 3,
    "ZILLIZ_URI": 4,
    "ZILLIZ_USER": 5,
    "ZILLIZ_PASSWORD": 6,
    "MILVUS_COLLECTION": 3,
    "MILVUS_HOST": 4,
    "MILVUS_PORT": 5,
    "MILVUS_USER": 6,
    "MILVUS_PASSWORD": 7,
    "QDRANT_URL": 3,
    "QDRANT_PORT": 4,
    "QDRANT_GRPC_PORT": 5,
    "QDRANT_API_KEY": 6,
    "QDRANT_COLLECTION": 7,
    "REDIS_HOST": 3,
    "REDIS_PORT": 4,
    "REDIS_PASSWORD": 5,
    "REDIS_INDEX_NAME": 6,
    "REDIS_DOC_PREFIX": 7,
    "REDIS_DISTANCE_METRIC": 8,
    "REDIS_INDEX_TYPE": 9,
}

entries = {}
labels = {}
for field, position in field_positions.items():
    label = tk.Label(root, text=field.replace("_", " ").title() + ":")
    label.grid(row=position, column=0)
    entry = tk.Entry(root)
    entries[field] = entry
    labels[field] = label  # Store the label

update_fields()  # Call the update_fields() function to set the initial state

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=max(field_positions.values()) + 1, column=1)

root.mainloop()

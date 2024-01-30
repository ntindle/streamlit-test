import streamlit as st
import requests

# Base URL for the API
BASE_URL = "https://auto-gpt-xca4qjgx4a-uc.a.run.app"


# Helper function to make API requests
def make_api_request(endpoint, method="get", data=None, params=None):
    url = f"{BASE_URL}{endpoint}"
    if method == "get":
        response = requests.get(url, params=params)
    elif method == "post":
        response = requests.post(url, json=data)
    return response.json()


# GUI Layout
st.title("Agent Protocol Interface")

# Create a new task
st.header("Create a New Task")
task_input = st.text_input("Input prompt for the task")
additional_task_input = st.text_area("Additional Input for the Task (JSON format)")
if st.button("Create Task"):
    task_data = {"input": task_input, "additional_input": additional_task_input}
    response = make_api_request("/ap/v1/agent/tasks", method="post", data=task_data)
    st.write(response)

# List all tasks
st.header("List All Tasks")
current_page_tasks = st.number_input("Current Page (Tasks)", min_value=1, value=1)
page_size_tasks = st.number_input("Page Size (Tasks)", min_value=1, value=10)
if st.button("Get Tasks"):
    params = {"current_page": current_page_tasks, "page_size": page_size_tasks}
    tasks = make_api_request("/ap/v1/agent/tasks", params=params)
    st.write(tasks)

# Get details about a specified task
st.header("Get Task Details")
task_id = st.text_input("Enter Task ID")
if st.button("Get Task Details"):
    task_details = make_api_request(f"/ap/v1/agent/tasks/{task_id}")
    st.write(task_details)

# List all steps for a specified task
st.header("List Steps for a Task")
current_page_steps = st.number_input("Current Page (Steps)", min_value=1, value=1)
page_size_steps = st.number_input("Page Size (Steps)", min_value=1, value=10)
if st.button("Get Task Steps"):
    params = {"current_page": current_page_steps, "page_size": page_size_steps}
    steps = make_api_request(f"/ap/v1/agent/tasks/{task_id}/steps", params=params)
    st.write(steps)

# Execute a step in the specified task
st.header("Execute Task Step")
step_input = st.text_area("Input for the Step (JSON format)")
if st.button("Execute Step"):
    step_data = {"input": step_input}
    response = make_api_request(
        f"/ap/v1/agent/tasks/{task_id}/steps", method="post", data=step_data
    )
    st.write(response)

# List all artifacts for a task
st.header("List Artifacts for a Task")
if st.button("Get Task Artifacts"):
    artifacts = make_api_request(f"/ap/v1/agent/tasks/{task_id}/artifacts")
    st.write(artifacts)

# Upload an artifact for a task
st.header("Upload Artifact for a Task")
uploaded_file = st.file_uploader("Choose a file")
if st.button("Upload Artifact"):
    # Handle file upload
    # Note: Actual file upload implementation will depend on the API requirements
    st.write("Artifact uploaded (mock response)")

# Download a specified artifact
st.header("Download Artifact")
artifact_id = st.text_input("Enter Artifact ID")
if st.button("Download Artifact"):
    # Handle artifact download
    # Note: Actual download implementation will depend on the API requirements
    st.write("Artifact downloaded (mock response)")

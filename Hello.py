import streamlit as st
import requests

# Base URL for the API
BASE_URL = "https://debug-tool-xca4qjgx4a-uc.a.run.app/"

st.title("Debugging Dashboard")

# Security scheme: API Key
api_key = st.sidebar.text_input("Enter your API Key")

headers = {"X-Api-Key": api_key}

# Get Tasks By Discord
discord_id = st.text_input("Enter Discord ID to get tasks")
if discord_id and st.button("Get Tasks by Discord"):
    response = requests.get(
        f"{BASE_URL}/debug/tasksbydiscord/{discord_id}", headers=headers
    )
    if response.status_code == 200:
        tasks = response.json()
        st.json(tasks)
    else:
        st.error("Failed to retrieve tasks for Discord ID")

# Get Tasks By User
user_id = st.text_input("Enter User ID to get tasks")
if user_id and st.button("Get Tasks by User"):
    response = requests.get(f"{BASE_URL}/debug/tasksbyuser/{user_id}", headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        st.json(tasks)
    else:
        st.error("Failed to retrieve tasks for User ID")

# Get Debug Summary, Debug Logs, Debug Steps, Debug Step, Debug Step Llm Calls
task_id = st.text_input("Enter Task ID for Debug Details")
if task_id:
    # Get Debug Summary
    if st.button("Get Debug Summary"):
        response = requests.get(f"{BASE_URL}/debug/task/{task_id}/", headers=headers)
        if response.status_code == 200:
            summary = response.json()
            st.json(summary)
        else:
            st.error("Failed to retrieve debug summary")

    # Get Debug Logs
    if st.button("Get Debug Logs"):
        response = requests.get(
            f"{BASE_URL}/debug/task/{task_id}/logs", headers=headers
        )
        if response.status_code == 200:
            logs = response.json()
            st.json(logs)
        else:
            st.error("Failed to retrieve debug logs")

    # Get Debug Steps
    if st.button("Get Debug Steps"):
        response = requests.get(
            f"{BASE_URL}/debug/task/{task_id}/steps", headers=headers
        )
        if response.status_code == 200:
            steps = response.json()
            st.json(steps)
        else:
            st.error("Failed to retrieve debug steps")

    # Get Debug Step
    step_id = st.text_input("Enter Step ID for Debug Step Details")
    if step_id and st.button("Get Debug Step"):
        response = requests.get(
            f"{BASE_URL}/debug/task/{task_id}/steps/{step_id}", headers=headers
        )
        if response.status_code == 200:
            step_details = response.json()
            st.json(step_details)
        else:
            st.error("Failed to retrieve debug step")

    # Get Debug Step Llm Calls
    if st.button("Get Debug Step Llm Calls"):
        response = requests.get(
            f"{BASE_URL}/debug/task/{task_id}/steps/{step_id}/openai", headers=headers
        )
        if response.status_code == 200:
            llm_calls = response.json()
            st.json(llm_calls)
        else:
            st.error("Failed to retrieve debug step LLM calls")

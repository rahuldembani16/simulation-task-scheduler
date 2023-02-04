# Rahool Dembani - Task Valeo Company - 10 pm to 12 Pakistani time

import random
import time
from threading import Thread

# list of resources
resources = [i for i in range(10)]

# dictionary to keep track of busy resources
busy_resources = {}

# list of projects
projects = ['project1', 'project2', 'project3', 'project4', 'project5']

# list of tasks
tasks = []
for project in projects:
    for i in range(100):
        tasks.append((project, random.randint(1,5)))

# interface to check for new tasks
def check_for_new_task():
    if tasks:
        return tasks.pop()
    return None

# function to run the scheduler
def scheduler():
    while True:
        task = check_for_new_task()
        if task:
            project, priority = task
            assigned = False
            for resource in resources:
                if resource not in busy_resources:
                    busy_resources[resource] = task
                    print(f"Task from project {project} with priority {priority} assigned to resource {resource}")
                    assigned = True
                    break
            if not assigned:
                print(f"No resources available for task from project {project} with priority {priority}")
                tasks.insert(0, task)
        time.sleep(1)

# function to run the resource
def resource(id):
    while True:
        if id in busy_resources:
            task = busy_resources[id]
            project, priority = task
            print(f"Resource {id} working on task from project {project} with priority {priority}")
            time.sleep(2)
            del busy_resources[id]
            time.sleep(1)

#start the scheduler
scheduler_thread = Thread(target=scheduler)
scheduler_thread.start()

#start the resources
resource_threads = [Thread(target=resource, args=(i,)) for i in resources]
for thread in resource_threads:
    thread.start()

#start the outside interface
def outside_interface():
    while True:
        project = input("Enter the project name: ")
        priority = int(input("Enter the priority of the task: "))
        tasks.append((project, priority))
        time.sleep(1)

interface_thread = Thread(target=outside_interface)
interface_thread.start()



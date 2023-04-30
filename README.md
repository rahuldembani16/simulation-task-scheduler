Rahool Dembani - Simulation Task Schedular - Python

This code is a simulation of a simple task scheduler, where multiple resources can be assigned tasks from different projects based on their availability and priority.

The code begins by importing necessary modules such as random, time, and Thread from the threading library. It then creates a list of resources with ids ranging from 0 to 9 and a dictionary busy_resources to keep track of the resources that are currently assigned tasks.

A list of projects and tasks is also created. Each project has 100 tasks assigned to it, with a random priority value between 1 and 5. The check_for_new_task() function is used to check for new tasks in the tasks list.

The main scheduler function scheduler() runs in a continuous loop and continuously checks for new tasks by calling the check_for_new_task() function. If a new task is available, it searches for an available resource to assign the task to based on their availability. If a resource is available, it assigns the task to the resource and marks it as busy in the busy_resources dictionary. If no resource is available, it puts the task at the beginning of the tasks list.

The resource() function simulates the resource behavior. It runs in a continuous loop and checks if it has a task assigned to it. If there is a task, it prints a message saying that it is working on the task and sleeps for 2 seconds. After completing the task, it removes the task from the busy_resources dictionary and sleeps for 1 second.

The scheduler() function and resource() functions are started using Thread and run parallelly. Another interface is created to input new tasks into the tasks list.

Overall, this code simulates a basic scheduling system that assigns tasks to resources based on their availability and priority.

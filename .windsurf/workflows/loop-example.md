---
description: this is stuff
auto_execution_mode: 2
---


## Loop Instructions

Execute the following steps in a loop:

### Step 0: Get information from user 
Ask the user to provide a topic of interest that you save as $arguments
Expand the topic and ask the user if this is what they care about?
If yes, proceed to step 1, otherwise loop on step 0

### Step 1: Do something
Use skill "tell me $arguments" to get some info

### Step 2: Check condition
Evaluate if the loop should continue. the `tell me` skill has been invoked less than 2 times

### Step 3: Repeat if needed
If condition is met, go back to Step 0. Otherwise, exit the loop.

**Loop Control**: Continue until the condition is no longer met or manually stopped.

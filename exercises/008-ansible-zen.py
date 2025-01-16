#!/usr/bin/python3

name = "The Zen of Ansible, by Tim Appnel"

az = '''Ansible is not Python.
YAML sucks for coding.
Playbooks are not for programming.
Ansible users are (most probably) not programmers.
Clear is better than cluttered.
Concise is better than verbose.
Simple is better than complex.
Readability counts.
Helping users get things done matters most.
User experience beats ideological purity.
“Magic” conquers the manual.
When giving users options, always use convention over configuration.
Declarative is always better than imperative - most of the time.
Focus avoids complexity.
Complexity kills productivity.
If the implementation is hard to explain, it's a bad idea.
Every shell command and UI interaction is an opportunity to automate.
Just because something works, doesn't mean it can't be improved.
Friction should be eliminated whenever possible.
Automation is a continuous journey that never ends.
'''
print("")
for i in range(100): 
    if i == 50: print("\n" + name)
    print("*", end='')

print("\n")

lines = az.splitlines()
for line in lines:
    print(line)
    input("")


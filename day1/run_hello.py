print("This is run_hello.py...")
import hello_world
hello_world.foo()
print("In run_hello.py: user =", hello_world.user)
hello_world.user = "Adrian Smith"
hello_world.foo()



import random
from typing import Generator


players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]



def gen_event() -> Generator[tuple, None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)



def consume_event(events_list):
    events = events_list[:]  

    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]

        events = events[:index] + events[index+1:]

        yield event

print("=== Game Data Stream Processor ===")



event_gen = gen_event()


for i in range(1000):
    event = next(event_gen)
    print(f"Event {i}: Player {event[0]} did action {event[1]}")



events_list = []
for _ in range(10):
     events_list = events_list + [next(event_gen)]

print("Built list of 10 events:", events_list)


for event in consume_event(events_list):
    print("Got event from list:", event)
    print("Remains in list:", events_list)
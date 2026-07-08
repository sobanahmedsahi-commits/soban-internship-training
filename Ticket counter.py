from collections import deque

ticket_queue = deque()

def take_ticket(name):
    ticket_queue.append(name)
    print(f"{name} added to queue")

def serve_ticket():
    if ticket_queue:
        served = ticket_queue.popleft()
        print(f"Serving {served}")
    else:
        print("No one in queue")


take_ticket("Ali")
take_ticket("Soban")
take_ticket("Ahmed")

serve_ticket()
serve_ticket()
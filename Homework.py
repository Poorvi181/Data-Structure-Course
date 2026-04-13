def print_simulator(documents):
    print_queue = []

    for doc in documents:
        print_queue.append(doc)

    while len(print_queue) > 0:
        current_doc = print_queue.pop(0)  
        print(f"Printing {current_doc}...")

documents = ["Doc1", "Doc2", "Doc3"]

print_simulator(documents)
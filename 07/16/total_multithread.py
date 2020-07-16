from multiprocessing import Process, Queue 
from time import time

def task_handler(current_list, result_queue):
    total = 0
    for num in current_list:
        total += num
    result_queue.put(total)

def main():
    processes = []
    index = 0
    queue = Queue()
    l = [ x for x in range(1,1000001)]
    start = time()
    for _ in range(8):
        p = Process(target=task_handler, args=(l[index:index+125000], queue))
        index += 1250000
        processes.append(p)
        p.start()
   

    for p in processes:
        p.join()
    
    total = 0
    while not queue.empty():
        total += queue.get()
    
    end = time()
    print('total: %d' % (total))
    print('Used time: %.3f' % (end - start))


if __name__ == "__main__":
    main()

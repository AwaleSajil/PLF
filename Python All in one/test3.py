import multiprocessing

def calc_square(v):
    v.value = 5.67
    print("square")

def calc_cube():
    print("cube")
    

if __name__ == "__main__":
    # result = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(v,))
    p2 = multiprocessing.Process(target=calc_cube, args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(v.value)
    # print(result[:])
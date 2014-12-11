#!/usr/bin/python
import multiprocessing
import pickle

def _pickle_method(method):
    func_name = method.im_func.__name__
    obj = method.im_self
    cls = method.im_class
    return _unpickle_method, (func_name, obj, cls)

def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
    return func.__get__(obj, cls)
class Task(object):
    def __init__(self, 
                 task_list, 
                 log_path,
                 status_queue): 

        self._status_queue = status_queue
def main():
#    pickle(MethodType, _pickle_method, _unpickle_method)
    #Create process pool.
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size)

    #Run.
    #Create Task.
    task_list = []
    inst_list = []
#    task = Task(task_list, server_log_path, msg_queue)

    #Transfer.
    for ip in ['127.0.0.1',]:
        pool.apply_async(task.do, (ip,))

    loghd = multiprocessing.Process(name="log", 
                                    target=status_mplog.write, 
                                    args=(1, "done.")
                                   )
    loghd.start()
    pool.close()
    pool.join()
    loghd.join()

if __name__ == '__main__':
    main()


from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from random import randint
from threading import Thread, Condition
from time import sleep
import numpy as np


FREQ = 5

class RT_Plot(object):

    def __init__(self, update_interval = 200) -> None:
        self.update_interval = update_interval
        self.fig, self.ax = plt.subplots(1,1)
        self.sem = Condition()
        self.sin_delta = 0


    def __init_plot(self):
        '''
            Initialize the plot, good for setting the graph template
        '''
        self.ax.set_title("Senoid animation")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(-2, 2)
        self.ax.set_ylabel("Voltage")
        self.ax.set_xlabel("Time (s)")


    def __plot_update(self, args):
        '''
            Method periodically called to update plot
        '''
        self.sem.acquire()
        self.sem.wait()
        self.ax.cla()
        self.ax.plot(self.x_data, self.y_data)
        self.sem.release()

        self.ax.set_title("Senoid animation")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(-2, 2)
        self.ax.set_ylabel("Voltage")
        self.ax.set_xlabel("Time (s)")


    def data_update(self, data_update_interval = 100):
        '''
            Method to update the data being ploted
        '''
        step = 0
        while True:
            self.value = randint(0,1000)

            self.x_data = np.linspace(0, 1, 10000)
            self.y_data = np.sin(self.x_data * FREQ * 2*np.pi + step)

            step += 1
            if step > FREQ:
                step = 0

            self.sem.acquire()
            self.sem.notify()
            self.sem.release()

            sleep(float(data_update_interval/1000))
            

    def start(self):
        data_thread = Thread(target= self.data_update)
        data_thread.start()

        self.animotion1 = FuncAnimation(self.fig, 
                                       func = self.__plot_update, 
                                       init_func = self.__init_plot,
                                       interval = self.update_interval)
        
        plt.show()



if __name__ == "__main__":
    live_plot = RT_Plot(update_interval=10)
    live_plot.start()
class Berkeley:
    """Berkeley Algorithm for time synchronization

Berkeley algorithm is used for local time synchronization in a distributed system.
A coordinator(Master) node receives the snapshot of timestamps of every node(Slaves) it is connected with.
The Master, then, finds out the average of these timestamps, including the timestamp of itself at the same moment when everyone calculate their timestamps.
In this algorithm, rather than returning the average timestamp value to every node, the Master node sends, to every node, the difference between the average and their respective timestamps.
This is done to reduce the latency as well as the time delay.
Thus, the new local timestamp is set in every node."""
    time_stamp = 0
    count = 0
    initial_time = []
    objects = []

    def __init__(self, time):
        self.time_stamp = time

    def masters(self):
        n = int(input("Enter the number of nodes : "))
        Berkeley.count = n
        master = int(input("Enter the id of master node : "))

        for i in range(n):
            x = int(input("Enter time : "))
            self.objects.append(Berkeley(x))

        for i in range(n):
            self.objects[master].initial_time.append(self.objects[i].time_stamp)

        print("\nEntered timestamps are : ",self.objects[master].initial_time)
        self.objects[master].aver()

        print("This is because the local timestamp of every node is set to the average value. Thus, local timestamps of %d nodes are "  %n )
        for i in self.objects:
            print(i.time_stamp)

    def aver(self):
        sums = 0
        for i in self.initial_time:
            sums += i

        average =  sums/Berkeley.count
        print("Averages is : ",average)

        #x = self.time_stamp - average # USELESS, unless you want to check how subtraction operator works. :P

        self.return_initial_time(average)

    def return_initial_time(self,avg):
        differences = []
        for i in range(self.count):
            differences.append(self.initial_time[i] - avg)

        self.set_new_times(differences)

    def set_new_times(self,differences):

        new_ts = []
        self.objects.clear()
        for i in range(self.count):
            x  = self.initial_time[i] - differences[i]
            new_ts.append(x)
            self.objects.append(Berkeley(x))

        print()
        print("Now, the timestamp list looks like : ", new_ts)



if __name__ == '__main__':
    b = Berkeley(None)
    print(b.__doc__,"\n")
    b.masters()
    print("New Line Added")


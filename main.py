'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01  (B)
Lab Task [30 Nov 2022]
Submitted to Mam Reeda Saeed

Explaination of Task:-
I have made a list of Processes and each process is made up of an individual list that contains the attributes
to specify that spacific list. This was done to simplify the class/functions structure for the FCFS Algorithm.

                       Process = [at,bt,ct,tat,wt]
'''
class FCFS:
    def __init__(self):
        self.process_list = None
        self.AvgTAT = 0
        self.AvgWT = 0
        self.Gantt_Chart = 0

    def findCompletionTime(self):
        for i,p in enumerate(self.process_list):
            self.Gantt_Chart += p[1]
            self.process_list[i].append(self.Gantt_Chart)

    def findTAT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[2]-p[0])

    def findWT(self):
        for i,p in enumerate(self.process_list):
            self.process_list[i].append(p[3]-p[1])

    def findAvgTAT(self):
        for i,p in enumerate(self.process_list):
            self.AvgTAT += p[3]
        self.AvgTAT /= len(self.process_list)

    def findAvgWT(self):
        for i,p in enumerate(self.process_list):
            self.AvgWT += p[4]
        self.AvgWT /= len(self.process_list)

    def showData(self):
        print("____________________________________________________________________________")
        print("Processes Ran from 0 --> {}".format(self.Gantt_Chart))
        print("Average Turn-around Time = ", self.AvgTAT)
        print("Average Wait Time = ", self.AvgWT)

        for i,p in enumerate(self.process_list,1):
            print("\n-----------------------------------------------------------------")
            print("Process #{}:-".format(i))
            print("Arrival Time: ", p[0])
            print("Burst Time: ", p[1])
            print("Completion Time: ", p[2])
            print("Turn-around Time: ", p[3])
            print("Wait Time: ", p[4])

if __name__ == "__main__":
    scheduler = FCFS()

    # Processes |  Arrival Time  |  Burst Time |
    P1          = [     0       ,       5     ]
    P2          = [     5       ,       7     ]
    P3          = [     7       ,       3     ]
    scheduler.process_list = [P1, P2, P3]

    scheduler.findCompletionTime()
    scheduler.findTAT()
    scheduler.findWT()
    scheduler.findAvgTAT()
    scheduler.findAvgWT()
    scheduler.showData()
    


class measured_data_t:
    ID = []
    allID = []
    day = []
    windSpeed = []
    temperature = []
    def __init__(self):
        fileName = "tm_01a.txt"
        file1 = open(fileName,"r")
        data = file1.readlines()
        file1.close()
        k = 1
        tmp = ""
        for i in range(len(data)):
            line = data[i]
            line += " "
            for j in range(len(line)):
                if(line[j] != " "):
                    tmp += line[j]
                elif(tmp != ""):
                    if(k == 1):
                        self.allID.append(int(tmp))
                        k += 1
                    elif(k == 2):
                        self.day.append(int(tmp))
                        k += 1
                    elif(k == 3):
                        self.windSpeed.append(int(tmp))
                        k += 1
                    elif(k == 4):
                        self.temperature.append(int(tmp))
                        k = 1
                    tmp = ""
        for i in range(len(self.allID)):
            if(self.allID[i] in self.ID):
                continue
            else:
                self.ID.append(self.allID[i])
    def exterma(self):
        a = 0
        x = 7
        wind1 = 0
        wind2 = 0
        wind3 = 0
        temp1 = []
        temp2 = []
        temp3 = []
        for i in range(len(self.ID)):
            for j in range(a,x):
                if(j < x-1):
                    tmp = self.temperature[j] - self.temperature[j+1]
                    if(i == 0):
                        wind1 += self.windSpeed[j]
                        temp1.append(tmp)
                    elif(i == 1):
                        wind2 += self.windSpeed[j]
                        temp2.append(tmp)
                    elif(i == 2):
                        wind3 += self.windSpeed[j]
                        temp3.append(tmp)
            a = x
            x += 7
        avgWind1 = wind1 / 7
        avgWind2 = wind2 / 7
        avgWind3 = wind3 / 7
        m1, m2 , m3 = 0, 0, 0
        for i in range(len(self.ID)):
            if(temp1[i] > temp2[i] and temp1[i] > temp3[i]):
                m1 += 1
            if(temp2[i] > temp1[i] and temp2[i] > temp3[i]):
                m2 += 1
            if(temp3[i] > temp1[i] and temp3[i] > temp2[i]):
                m3 += 1
        mcc = m1
        mccID = self.ID[0]
        if(mcc < m2):
            mcc = m2
            mccID = self.ID[1]
        if(mcc < m3):
            mcc = m3
            mccID = self.ID[2]
        print(f"\nMost climate change")
        print(f" ID : {mccID}")
        print(f"\nAverage wind speed")
        print(f" ID {self.ID[0]} : {avgWind1}")
        print(f" ID {self.ID[1]} : {avgWind2}")
        print(f" ID {self.ID[2]} : {avgWind3}")
#  
# 
temperature1 = measured_data_t()
temperature1.exterma()
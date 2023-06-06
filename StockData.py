import xlsxwriter

class StockData:
    def __init__(self):
        self.row=0
        self.col=0
        self.workbook = xlsxwriter.Workbook('ManiaData.xlsx')
        self.worksheet = self.workbook.add_worksheet()
		# Add header self.row
        self.header_row = ["Num ID","Num Date", "Num Heure", "Part Day", "Weather", "Temperature", "Humidity", "Precipitation", "Wind Speed", "Atmospheric Pressure"]
        for i, header in enumerate(self.header_row):
            self.worksheet.write(self.row, i, header)
        self.row += 1

    def start_data(self, d_mania):
        #self.collect the data of the start neuron
        self.worksheet.write(self.row, self.col, d_mania[0])
        self.worksheet.write(self.row, self.col+1, d_mania[1])
        self.worksheet.write(self.row, self.col+2, d_mania[2])
        self.worksheet.write(self.row, self.col+3, str(d_mania[3]))
        self.worksheet.write(self.row, self.col+4, d_mania[4])
        self.worksheet.write(self.row, self.col+5, d_mania[5])
        self.worksheet.write(self.row, self.col+6, d_mania[6])
        self.worksheet.write(self.row, self.col+7, d_mania[7])
        self.worksheet.write(self.row, self.col+8, d_mania[8])
        self.worksheet.write(self.row, self.col+9, d_mania[9])
        self.row+=1

    def stop_data(self):
        self.workbook.close()
		

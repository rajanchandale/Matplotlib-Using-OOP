import matplotlib.pyplot as plt

#classes
class graph_properties:#super class
     def __init__(self,figHeight,figWidth):
          self.figHeight = 0
          self.figWidth = 0

     def survey(self):
          #defining self.figHeight
          self.figHeight = int(input("Enter The Height Of Your Figure In Inches (Max. Height = 18 Inches) \n"))
          #defining self.figWidth
          self.figWidth = int(input("Enter The Width Of Your Figure In Inches (Max. Width = 18 Inches) \n"))
               
class line_graph(graph_properties): #child class
     def __init__(self,line_xValues,line_yValues,line_yValues2,lineColour,lineColour2,line_markerType,line_markerType2,numOf_Lines,line_xLabel,line_yLabel,line_graphTitle,boolFill_Between,boolFill_Between2,fillBetween_Lower,fillBetween_Upper,fillBetween_Lower2,fillBetween_Upper2,lineLegend):
          self.line_xValues = []
          self.line_yValues = []
          self.line_yValues2 = []
          self.lineColour = ""
          self.lineColour2 = ""
          self.line_markerType = ""
          self.line_markerType2 = ""
          self.numOf_Lines = ""
          self.line_xLabel = ""
          self.line_yLabel = ""
          self.line_graphTitle = ""
          self.boolFill_Between = False
          self.boolFill_Between2 = False
          self.fillBetween_Lower = []
          self.fillBetween_Upper = []
          self.fillBetween_Lower2 = []
          self.fillBetween_Upper2= []
          self.lineLegend = []
          

     def lineSurvey(self):
          print("N.B. Each Line Plotted On Your Line Graph Will Require Its Own X and Y Values")
          #defining self.numOf_Lines
          cont = False
          while cont == False:
               num = int(input("Enter The Corresponding Number To The Amount Of Lines Your Line Graph Will Contain: \n 1) One \n 2) Two \n"))
               if num == 1:
                    self.numOf_Lines = 1
                    cont = True
               elif num == 2:
                    self.numOf_Lines = 2
                    cont = True
     
          
          #defining self.line_xValues
          print("Enter X-Values, One Value At A Time (X-Values Must Be Numerical)")
          exitClause = ""
          while exitClause != "x":
               self.line_xValues.append(int(input("Enter An X-Value: \n")))
               cont = False
               while cont == False:
                    exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'x' If This Is The Last X-Value \n").lower()
                    if exitClause == "p" or exitClause == "x":
                         cont = True
                    
          #defining self.line_yValues
          print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
          exitClause = ""
          while exitClause != "y":
               self.line_yValues.append(int(input("Enter A Y-Value: \n")))
               cont = False
               while cont == False:
                    exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                    if exitClause == "p" or exitClause == "y":
                         cont = True
          #defining self.lineColour
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To The Colour Of Your Line: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
               if choice >= 1 and choice <= 6:
                    if choice == 1:
                         self.lineColour = "red"
                         cont = True
                    elif choice == 2:
                         self.lineColour = "green"
                         cont = True
                    elif choice == 3:
                         self.lineColour = "blue"
                         cont = True
                    elif choice == 4:
                         self.lineColour = "orange"
                         cont = True
                    elif choice == 5:
                         self.lineColour = "black"
                         cont = True
                    elif choice == 6:
                         self.lineColour = "GoldenRod"
                         cont = True
          #defining self.line_markerType
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To The Marker Type For Your Line Graph: \n 1) Round \n 2) Square \n 3) Asterisk \n"))
               if choice == 1:
                    self.line_markerType = "o"
                    cont = True
               elif choice == 2:
                    self.line_markerType = "s"
                    cont = True
               elif choice == 3:
                    self.line_markerType = "*"
                    cont = True
          
          #defining self.boolFill_Between
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To Your Decision. \n Would You Like A Fill-Between? \n 1) Yes \n 2) No \n"))
               if choice == 1:
                    self.boolFill_Between = True
                    cont = True 
               elif choice == 2:
                    self.boolFill_Between = False
                    cont = True
          #defining self.fillBetween
          if self.boolFill_Between == True:
               cont = False
               while cont == False:
                    errorType = int(input("Enter The Corresponding Number. \n Is Your Error Interval: \n 1) Numerical \n 2) Percentile\n"))
                    if errorType == 1:
                         error = int(input("Enter The Numerical Error Interval: \n"))
                         self.fillBetween_Lower = [i - error for i in self.line_yValues]
                         self.fillBetween_Upper = [i + error for i in self.line_yValues]
                         cont = True
                    elif errorType == 2:
                         error = float(input("Enter The Percentage Error Interval In Decimal Form: \n"))
                         low = 1 - error
                         high = 1 + error
                         self.fillBetween_Lower = [i * low for i in self.line_yValues]
                         self.fillBetween_Upper = [i * high for i in self.line_yValues]
                         cont = True
          #defining self.lineLegend
          (self.lineLegend).append(input("Enter A Label For This Line: \n"))

               
          if self.numOf_Lines > 1:
               print("Enter Data For The Second Line: ")
               #defining self.line_yValues2
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.line_yValues2.append(int(input("Enter A Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True

               #defining self.lineColour2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Colour Of Your Line: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.lineColour2 = "red"
                              cont = True
                         elif choice == 2:
                              self.lineColour2 = "green"
                              cont = True
                         elif choice == 3:
                              self.lineColour2 = "blue"
                              cont = True
                         elif choice == 4:
                              self.lineColour2 = "orange"
                              cont = True
                         elif choice == 5:
                              self.lineColour2 = "black"
                              cont = True
                         elif choice == 6:
                              self.lineColour2 = "GoldenRod"
                              cont = True
               #defining self.line_markerType2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Marker Type For Your Line Graph: \n 1) Round \n 2) Square \n 3) Asterisk \n"))
                    if choice == 1:
                         self.line_markerType2 = "o"
                         cont = True
                    elif choice == 2:
                         self.line_markerType2 = "s"
                         cont = True
                    elif choice == 3:
                         self.line_markerType2 = "*"
                         cont = True

               #defining self.boolFill_Between2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To Your Decision. \n Would You Like A Fill-Between? \n 1) Yes \n 2) No \n"))
                    if choice == 1:
                         self.boolFill_Between2 = True
                         cont = True 
                    elif choice == 2:
                         self.boolFill_Between2 = False
                         cont = True
               #defining Fill Between
               if self.boolFill_Between == True:
                    cont = False
                    while cont == False:
                         errorType = int(input("Enter The Corresponding Number. \n Is Your Error Interval: \n 1) Numerical \n 2) Percentile\n"))
                         if errorType == 1:
                              error = int(input("Enter The Numerical Error Interval: \n"))
                              self.fillBetween_Lower2 = [i - error for i in self.line_yValues2]
                              self.fillBetween_Upper2 = [i + error for i in self.line_yValues2]
                              cont = True
                         elif errorType == 2:
                              error = float(input("Enter The Percentage Error Interval In Decimal Form: \n"))
                              low = 1 - error
                              high = 1 + error
                              self.fillBetween_Lower2 = [i * low for i in self.line_yValues2]
                              self.fillBetween_Upper2 = [i * high for i in self.line_yValues2]
                              cont = True
               #defining self.lineLegend
               (self.lineLegend).append(input("Enter A Label For This Line: \n"))
               


          #defining self.line_xLabel
          self.line_xLabel = input("Enter The Label For Your X-Axis: \n")
          #defining self.line_yLabel
          self.line_yLabel = input("Enter The Label For Your Y-Axis: \n")
          #defining self.line_graphTitle
          self.line_graphTitle = input("Enter The Title For Your Graph: \n")

          self.plotting_lineGraph()
               
               
               
               
                    
               
          
     def plotting_lineGraph(self):#Gathering data given by user in earlier methods & using this data to plot the desired graph
          plt.figure(figsize = (self.figHeight, self.figWidth))
          plt.plot(self.line_xValues,self.line_yValues,color = self.lineColour,marker = self.line_markerType)
          
          if self.boolFill_Between == True:
               plt.fill_between(self.line_xValues,self.fillBetween_Lower,self.fillBetween_Upper,alpha = 0.2,color = self.lineColour)

          if self.numOf_Lines == 2:
               plt.plot(self.line_xValues,self.line_yValues2,color = self.lineColour2,marker = self.line_markerType2)
               if self.boolFill_Between2 == True:
                    plt.fill_between(self.line_xValues,self.fillBetween_Lower2,self.fillBetween_Upper2,alpha = 0.2,color = self.lineColour2)

          plt.xlabel(self.line_xLabel)
          plt.ylabel(self.line_yLabel)
          plt.title(self.line_graphTitle)

          plt.show()
          
          

class pieCharts(graph_properties):#child class
     def __init__(self,pieProportions,pieLabels):
          self.pieProportions = []
          self.pieLabels = []

     def pieSurvey(self):
          #defining self.pieProportions
          print("Enter The Proportions For Each Sector Of The Pie Chart As Percentages Out Of 100")
          print("The Data Will Finish Collecting Once The Total Of Your Entries Is Equal To 100%")
          total = 0
          while total < 100:
               num = int(input("Enter The Percentage For A Sector(E.G 50% Should Be Entered As 50): \n"))
               total += num
               name = input("Enter The Label For This Sector: \n")
               self.pieProportions.append(num)
               self.pieLabels.append(name)
               print(total)

          user.plotting_pieChart()

     def plotting_pieChart(self):
          plt.figure(figsize = (self.figHeight, self.figWidth))
          plt.pie(self.pieProportions,autopct = "%0.2f%%",labels = self.pieLabels)
          plt.show()

class barGraphs(graph_properties):#child class
     def __init__(self,bar_graphType,bar_xValues,bar_xValues2,bar_yValues,bar_yValues2,bool_yErr,yErr,num_ofBars,bar_xLabel,bar_yLabel,bar_graphTitle,barColour,barColour2,barLegend):
          self.bar_graphType = ""
          self.bar_xValues = []
          self.bar_xValues2 = []
          self.bar_yValues = []
          self.bar_yValues2 = []
          self.bool_yErr = False
          self.yErr = []
          self.num_ofBars = ""
          self.bar_xLabel = ""
          self.bar_yLabel = ""
          self.bar_graphTitle = ""
          self.barColour = ""
          self.barColour2 = ""
          self.barLegend = []

     def barSurvey(self):
          #defining self.bar_graphType
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To The Type Of Graph You Would Like To Plot: \n 1) Bar Graph \n 2) Side-By-Side Bar Graph \n 3) Vertically Stacked Bar Graph \n"))
               if choice == 1:
                    self.bar_graphType = "Normal"
                    cont = True
               elif choice == 2:
                    self.bar_graphType = "Side"
                    cont = True
               elif choice == 3:
                    self.bar_graphType = "Vertical"
                    cont = True
          if self.bar_graphType == "Normal":
               #defining self.bar_xValues
               print("Enter X-Values, One Value At A Time (X-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "x":
                    self.bar_xValues.append(int(input("Enter An X-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'x' If This Is The Last X-Value \n").lower()
                         if exitClause == "p" or exitClause == "x":
                              cont = True

               #defining self.bar_yValues
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.bar_yValues.append(int(input("Enter An Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next Y-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True
               #defining self.bool_yErr
               cont = False
               while cont == False:
                    choice = int(input("Would You Like Your Graph To Contain An Error Bar? (Enter Corresponding Number): \n 1) Yes \n 2) No \n "))
                    if choice == 1:
                         self.bool_yErr = True
                         cont = True
                    elif choice == 2:
                         self.bool_yErr = False
                         cont = True
               #defining self.yErr
               if self.bool_yErr == True:
                    cont = False
                    while cont == False:
                         choice = int(input(("Is The Magnitude Of Your Error Bar Numerical Or Percentile?(Enter Corresponding Number): \n 1) Numerical \n 2) Percentile \n")))
                         if choice == 1:
                              self.yErr = int(input("Enter The Numerical Magnitude Of Your Error Bar: \n"))
                              cont = True
                         if choice == 2:
                              percentileError = float(input("Enter The Percentile Magnitude Of Your Error Bar As A Decimal: \n"))
                              self.yErr = [i * percentileError for i in self.bar_yValues]
                              cont = True
               #defining self.bar_xLabel
               self.bar_xLabel = input("Enter The Label For Your X-Axis: \n")
               #defining self.bar_yLabel
               self.bar_yLabel = input("Enter The Label For Your Y-Axis: \n")
               #defining self.bar_graphTitle
               self.bar_graphTitle = input("Enter The Title For Your Graph: \n")
               #defining self.barColour
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour Of Your Bar Chart: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.barColour = "red"
                              cont = True
                         elif choice == 2:
                              self.barColour = "green"
                              cont = True
                         elif choice == 3:
                              self.barColour = "blue"
                              cont = True
                         elif choice == 4:
                              self.barColour = "orange"
                              cont = True
                         elif choice == 5:
                              self.barColour = "black"
                              cont = True
                         elif choice == 6:
                              self.barColour = "GoldenRod"
                              cont = True
     
          if self.bar_graphType == "Vertical":
               #defining self.bar_xLabel
               self.bar_xLabel = input("Enter The Label For Your X-Axis: \n")
               #defining self.bar_yLabel
               self.bar_yLabel = input("Enter The Label For Your Y-Axis: \n")
               #defining self.bar_graphTitle
               self.bar_graphTitle = input("Enter The Title For Your Graph: \n")
               #defining self.bar_xValues
               print("Enter X-Values, One Value At A Time (X-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "x":
                    self.bar_xValues.append(int(input("Enter An X-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'x' If This Is The Last X-Value \n").lower()
                         if exitClause == "p" or exitClause == "x":
                              cont = True
               print("As You Have Requested To Plot More Than One Bar, Each Bar Will Need To Have Its Data Entered Separately So They Can Be Plotted Individually.")
               #defining self.bar_yValues
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.bar_yValues.append(int(input("Enter A Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True

               #defining self.barColour
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.barColour = "red"
                              cont = True
                         elif choice == 2:
                              self.barColour = "green"
                              cont = True
                         elif choice == 3:
                              self.barColour = "blue"
                              cont = True
                         elif choice == 4:
                              self.barColour = "orange"
                              cont = True
                         elif choice == 5:
                              self.barColour = "black"
                              cont = True
                         elif choice == 6:
                              self.barColour = "GoldenRod"
                              cont = True
               #defining self.barLegend
               (self.barLegend).append(input("Enter A Label For This Group Of Data: \n"))

               #defining self.bar_yValues2
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.bar_yValues2.append(int(input("Enter A Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True

               #defining self.barColour2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.barColour2 = "red"
                              cont = True
                         elif choice == 2:
                              self.barColour2 = "green"
                              cont = True
                         elif choice == 3:
                              self.barColour2 = "blue"
                              cont = True
                         elif choice == 4:
                              self.barColour2 = "orange"
                              cont = True
                         elif choice == 5:
                              self.barColour2 = "black"
                              cont = True
                         elif choice == 6:
                              self.barColour2 = "GoldenRod"
                              cont = True
               #defining self.barLegend
               self.barLegend.append(input("Enter A Label For This Group Of Data: \n"))

          if self.bar_graphType == "Side":
               print("N.B Only The Y-Values Will Need To Be Entered For This Graph. ")
               #defining self.bar_yValues
               print("Enter The Y-Values For The First Set Of Data: ")
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.bar_yValues.append(int(input("Enter A Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True
               #defining self.bar_xValues
               n = 1
               t = 2
               d = (len(self.bar_yValues))
               w = 0.8
               self.bar_xValues =[t*element + w*n for element in range(d)]

               #defining self.barColour
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.barColour = "red"
                              cont = True
                         elif choice == 2:
                              self.barColour = "green"
                              cont = True
                         elif choice == 3:
                              self.barColour = "blue"
                              cont = True
                         elif choice == 4:
                              self.barColour = "orange"
                              cont = True
                         elif choice == 5:
                              self.barColour = "black"
                              cont = True
                         elif choice == 6:
                              self.barColour = "GoldenRod"
                              cont = True

               #defining self.barLegend
               (self.barLegend).append(input("Enter A Label For The First Set Of Data: \n"))

               
               #defining self.bar_yValues2
               print("Enter The Y-Values For The Second Set Of Data: ")
               print("Enter Y-Values, One Value At A Time (Y-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "y":
                    self.bar_yValues2.append(int(input("Enter A Y-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'y' If This Is The Last Y-Value \n").lower()
                         if exitClause == "p" or exitClause == "y":
                              cont = True

               #defining self.bar_xValues2
               n = 2
               t = 2
               d = (len(self.bar_yValues))
               w = 0.8
               self.bar_xValues2 = [t*element + w*n for element in range(d)]

               #defining self.barColour2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.barColour2 = "red"
                              cont = True
                         elif choice == 2:
                              self.barColour2 = "green"
                              cont = True
                         elif choice == 3:
                              self.barColour2 = "blue"
                              cont = True
                         elif choice == 4:
                              self.barColour2 = "orange"
                              cont = True
                         elif choice == 5:
                              self.barColour2 = "black"
                              cont = True
                         elif choice == 6:
                              self.barColour2 = "GoldenRod"
                              cont = True
               #defining self.barLegend
               (self.barLegend).append(input("Enter A Label For The Second Set Of Data: \n"))
               #defining self.bar_xLabel
               self.bar_xLabel = input("Enter The Label For Your X-Axis: \n")
               #defining self.bar_yLabel
               self.bar_yLabel = input("Enter The Label For Your Y-Axis: \n")
               #defining self.bar_graphTitle
               self.bar_graphTitle = input("Enter The Title For Your Graph: \n")              

          self.plotting_barChart()     

     def plotting_barChart(self):
          if self.bar_graphType == "Normal":
               if self.bool_yErr == True:
                    plt.bar(self.bar_xValues,self.bar_yValues,yerr = self.yErr,capsize = 5,color = self.barColour)
                    plt.xlabel(self.bar_xLabel)
                    plt.ylabel(self.bar_yLabel)
                    plt.title(self.bar_graphTitle)
               else:
                    plt.bar(self.bar_xValues,self.bar_yValues,color = self.barColour)
                    plt.xlabel(self.bar_xLabel)
                    plt.ylabel(self.bar_yLabel)
                    plt.title(self.bar_graphTitle)

          if self.bar_graphType == "Vertical":
               plt.bar(self.bar_xValues,self.bar_yValues,color = self.barColour)
               plt.bar(self.bar_xValues,self.bar_yValues2,bottom = self.bar_yValues,color = self.barColour2)
               plt.xlabel(self.bar_xLabel)
               plt.ylabel(self.bar_yLabel)
               plt.title(self.bar_graphTitle)
               plt.legend(self.barLegend)

          if self.bar_graphType == "Side":
               plt.bar(self.bar_xValues,self.bar_yValues,color = self.barColour)
               plt.bar(self.bar_xValues2,self.bar_yValues2,color = self.barColour2)
               plt.xlabel = (self.bar_xLabel)
               plt.ylabel = (self.bar_yLabel)
               plt.title(self.bar_graphTitle)
               plt.legend(self.barLegend)

          plt.show()

class Histograms(graph_properties):#child class
     def __init__(self,num_ofGraphs,hist_xValues,hist_xValues2,histBins,histBins2,hist_Colour,hist_Colour2,hist_Type,hist_Type2,histLegend,hist_xLabel,hist_yLabel,hist_graphTitle):
          self.num_ofGraphs = "" 
          self.hist_xValues = []
          self.hist_xValues2 = []
          self.histBins = ""
          self.histBins2 = "" 
          self.histColour = ""
          self.histColour2 = ""
          self.hist_Type = ""
          self.hist_Type2 = ""
          self.histLegend = []
          self.hist_xLabel = ""
          self.hist_yLabel = ""
          self.hist_graphTitle = ""

     def histSurvey(self):
          print("N.B Only The X-Values Will Need To Be Entered For This Graph. ")
          #defining self.num_ofGraphs
          cont = False
          while cont == False:
               num = int(input("Enter The Number Of Data Sets You Will Be Plotting (Enter The Corresponding Number): \n 1) One \n 2) Two \n"))
               if num == 1:
                    self.num_ofGraphs = 1
                    cont = True
               elif num == 2:
                    self.num_ofGraphs = 2
                    cont = True
          #defining self.hist_xValues
          print("Enter X-Values, One Value At A Time (X-Values Must Be Numerical)")
          exitClause = ""
          while exitClause != "x":
               self.hist_xValues.append(int(input("Enter An X-Value: \n")))
               cont = False
               while cont == False:
                    exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'x' If This Is The Last X-Value \n").lower()
                    if exitClause == "p" or exitClause == "x":
                         cont = True
          #defining self.histColour
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
               if choice >= 1 and choice <= 6:
                    if choice == 1:
                         self.histColour = "red"
                         cont = True
                    elif choice == 2:
                         self.histColour = "green"
                         cont = True
                    elif choice == 3:
                         self.histColour = "blue"
                         cont = True
                    elif choice == 4:
                         self.histColour = "orange"
                         cont = True
                    elif choice == 5:
                         self.histColour = "black"
                         cont = True
                    elif choice == 6:
                         self.histColour = "GoldenRod"
                         cont = True
          #defining self.hist_Type
          cont = False
          while cont == False:
               choice = int(input("Enter The Corresponding Number To The Type Of Histogram You Would Like For The First Set Of Data: \n 1) Solid Fill, Solid Outline \n 2) No Fill, Solid Outline \n"))
               if choice == 1:
                    self.hist_Type = ""
                    cont = True
               elif choice == 2:
                    self.hist_Type = "step"
                    cont = True
          #defining self.histBins
          self.histBins = int(input("Enter The Number Of Bins You Would Like This Data Set To Have: \n"))
          #defining self.histLegend
          (self.histLegend).append(input("Enter A Label For This Set Of Data: \n"))

          if self.num_ofGraphs == 2:
               #defining self.hist_xValues2
               print("Enter X-Values, One Value At A Time (X-Values Must Be Numerical)")
               exitClause = ""
               while exitClause != "x":
                    self.hist_xValues2.append(int(input("Enter An X-Value: \n")))
                    cont = False
                    while cont == False:
                         exitClause = input("Enter 'p' To Enter The Next X-Value OR Enter 'x' If This Is The Last X-Value \n").lower()
                         if exitClause == "p" or exitClause == "x":
                              cont = True
               #defining self.histColour2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Desired Colour For This Group Of Data: \n 1) Red \n 2) Green \n 3) Blue \n 4) Orange \n 5) Black \n 6) Gold \n"))
                    if choice >= 1 and choice <= 6:
                         if choice == 1:
                              self.histColour2 = "red"
                              cont = True
                         elif choice == 2:
                              self.histColour2 = "green"
                              cont = True
                         elif choice == 3:
                              self.histColour2 = "blue"
                              cont = True
                         elif choice == 4:
                              self.histColour2 = "orange"
                              cont = True
                         elif choice == 5:
                              self.histColour2 = "black"
                              cont = True
                         elif choice == 6:
                              self.histColour2 = "GoldenRod"
                              cont = True
               #defining self.hist_Type2
               cont = False
               while cont == False:
                    choice = int(input("Enter The Corresponding Number To The Type Of Histogram You Would Like For The First Set Of Data: \n 1) Solid Fill, Solid Outline \n 2) No Fill, Solid Outline \n"))
                    if choice == 1:
                         self.hist_Type2 = ""
                         cont = True
                    elif choice == 2:
                         self.hist_Type2 = "step"
                         cont = True
               #defining self.histBins2
               self.histBins2 = int(input("Enter The Number Of Bins You Would Like This Data Set To Have: \n"))
               #defining self.histLegend
               (self.histLegend).append(input("Enter A Label For This Set Of Data: \n"))

          #defining self.hist_xLabel
          self.hist_xLabel = input("Enter The Label For Your X-Axis: \n")
          #defining self.hist_yLabel
          self.hist_yLabel = input("Enter The Label For Your Y-Axis: \n")
          #defining self.hist_graphTitle
          self.hist_graphTitle = input("Enter The Title For Your Graph: \n")

          self.plotting_Histogram()

     def plotting_Histogram(self):
          plt.figure(figsize = (self.figHeight, self.figWidth))
          if self.hist_Type == "step":
               plt.hist(self.hist_xValues,bins = self.histBins,alpha = 0.7,color = self.histColour,histtype = self.hist_Type)
          elif self.hist_Type == "":
               plt.hist(self.hist_xValues,bins = self.histBins,alpha = 0.7,color = self.histColour)
          if self.num_ofGraphs == 2:
               if self.hist_Type2 == "step":
                    plt.hist(self.hist_xValues2,bins = self.histBins2,alpha = 0.7,color = self.histColour2,histtype = self.hist_Type)
               elif self.hist_Type2 == "":
                    plt.hist(self.hist_xValues2,bins = self.histBins2,alpha = 0.7,color = self.histColour2)
          plt.legend(self.histLegend)
          plt.xlabel = self.hist_xLabel
          plt.ylabel = self.hist_yLabel
          plt.title = self.hist_graphTitle 

          plt.show()
                                                       
#Main Body
cont = False
while cont == False:
     choice = int(input("Enter The Corresponding Number To The Graph You Wish To Plot: \n 1) Line Graph \n 2) Bar Chart \n 3) Histogram \n 4) Pie Chart \n"))
     if choice == 1:
          graphType = "Line"
          cont = True
     elif choice == 2:
          graphType = "Bar"
          cont = True
     elif choice == 3:
          graphType = "Histogram"
          cont = True
     elif choice == 4:
          graphType = "Pie"
          cont = True

if graphType == "Line":
     user = line_graph("","","","","","","","","","","","","","","","","","")
     user.survey()
     user.lineSurvey()

elif graphType == "Bar":
     user = barGraphs("","","","","","","","","","","","","","")
     user.survey()
     user.barSurvey()

elif graphType == "Histogram":
     user = Histograms("","","","","","","","","","","","","")
     user.survey()
     user.histSurvey()

elif graphType == "Pie":
     user = pieCharts("","")
     user.survey()
     user.pieSurvey()
     

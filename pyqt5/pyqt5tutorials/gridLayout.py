#Grid Layout
    #has buttons in rows and coloumns

#need to include (import) th QGridLayout class from QtWidgets
#create the gridLayout by making a method. ex: def createLayout():
    #add'l method while creatting button
        #gridLayout = QGridLayout("select favorite language")
        #gridLayout.addWidget(button1, 0, 0)    #the parameters are the button, and the row and coloumn
    #after creating the buttons need to do the following
        #self.groupBox.setLayout(gridlayout)
#in the setWindow method call createLayout()
#create vbox object
    #call the addWidget metod using vbox
    #pass self.groupBox as parameter
#need to set layout for window
    #self.setLayout(vbox)
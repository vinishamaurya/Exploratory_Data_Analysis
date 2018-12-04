
# coding: utf-8

# ### Exploratory Data Analysis is a very important step in the field of analytics. So we thought of making a automated process to fetch all required graphs in one go.

# # Graph function version1:

# 
# 
# When we started making a function to automate the process of data visualisation of any given data, we built a function which can call the name of the dataset and return the graphs of all the columns.
# Here we have made our fuction to automatically decide which variables of the dataset are categorical and which are numerical, and accordingly, the function graph_version1 will return the barplot for categorical and histogram and boxplot for numeric data and save it in a folder of provided directory.
# 
# eg. graph_version1('cars')

# In[9]:


def graph_version1(x):                                #defining funtion
    import pandas as pd                               #importing libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns    
    import os
   
    data=pd.read_csv(x+'.csv')                        #reading csv 
    for i, col in enumerate(data.columns):            #loop starts for plots
        b=''                                          #empty string initialised to assign dtype of every column 
        b=data[col].dtype
        if len(data[col].unique())<15 or b==object :   #condition to check categorical data, if no. of unique items in a column <15 or if the type of column is object 
            g = sns.factorplot(col, data=data, aspect=1.5, kind="count", size=4)    #barplot/factorplot from seaborn library for categorical data
            if b==object:                                                           #if dtype is object, then rotate the x-axis to 45 degrees
                g.set_xticklabels(rotation=45)

            plt.title('Barplot of {0}'.format(col),fontsize=10)                     #title of plot
            plt.xlabel('{0}'.format(col))                                           #x-axis label
            plt.ylabel('Count')                                                     #y-axis label
            plt.savefig('C://Users//Vinay//Downloads//new_images//barplot_{0}.png'.format(col))    #saving to default directory
            plt.show()                                                                              #show all plots

        else:                                                 #for numerical data
            plt.hist(data[col])                               #plot histogram using matplotlib
            plt.title('Histogram of {0}'.format(col))         #title of histogram
            plt.xlabel('{0}'.format(col))                     #x-axis label 
            plt.ylabel('Frequecy of {0}'.format(col))         #y-axis label  
            plt.savefig('C://Users//Vinay//Downloads//new_images//histogram_{0}.png'.format(col))  #saving to default directory
            plt.show()                                                                             #show all graphs
            plt.boxplot(data[col])                            #plot boxplot using matplotlib              
            plt.title('Boxplot of {0}'.format(col))           #Title of graphs 
            plt.xlabel('{0}'.format(col))                     #x-axis label
            plt.savefig('C://Users//Vinay//Downloads//new_images//boxplot_{0}.png'.format(col))   #saving graphs to default directory
            plt.show()                                        #show all the graphs


# In[20]:


graph_version1('cars')


# # Graph function version 2:

# Not every user wants to see graphs of all variables. So, we thought of giving the access to the users to get the graphs of variables that they need.
# The function graph_version2 will provide the users to call any dataset and desired column index in a list and get the graphs.
# 
# eg.  graph_version2('cars',[1,3,5])

# In[11]:


def graph_version2(x,number_of_columns):               #defining function to provide dataset and index of column in []
    import pandas as pd                                #importing libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns    
    import os
   
    data=pd.read_csv(x+'.csv')                         #reading csv
    if number_of_columns == None:                      #condition to give all graphs if no columns selected
        for i, col in enumerate(data.columns):         #loop starts for plots
            b=''                                       #empty string initialised to assign dtype of every column  
            b=data[col].dtype
            if len(data[col].unique())<15 or b==object :                            #condition to check categorical data, if no. of unique items in a column <15 or if the type of column is object 
                g = sns.factorplot(col, data=data, aspect=1.5, kind="count", size=4)    #barplot/factorplot from seaborn library for categorical data 
                if b==object:                                                           #if dtype is object, then rotate the x-axis to 45 degrees
                    g.set_xticklabels(rotation=45)

                plt.title('Barplot of {0}'.format(col),fontsize=10)                   #title of plot
                plt.xlabel('{0}'.format(col))                                         #x-axis label  
                plt.ylabel('Count')                                                   #y-axis label
                plt.savefig('C://Users//Vinay//Downloads//new_images//barplot_{0}.png'.format(col))    #saving to default directory
                plt.show()                                                                             #show all graphs

            else:                                                                      #for numerical data 
                plt.hist(data[col])                                                     #plot histogram using matplotlib  
                plt.title('Histogram of {0}'.format(col))                              #title of plot
                plt.xlabel('{0}'.format(col))                                          #x-axis label 
                plt.ylabel('Frequecy of {0}'.format(col))                              #y-axis label
                plt.savefig('C://Users//Vinay//Downloads//new_images//histogram_{0}.png'.format(col))     #saving to default directory
                plt.show()                                                                                #show all graphs 
                plt.boxplot(data[col])                                                 #plot boxplot using matplotlib
                plt.title('Boxplot of {0}'.format(col))                               #title of plot
                plt.xlabel('{0}'.format(col))                                          #x-axis label  
                plt.savefig('C://Users//Vinay//Downloads//new_images//boxplot_{0}.png'.format(col))       #saving to default directory
                plt.show()                                                                                #show all graphs
    else:                                                                    #if user gives a list[] of columns then go to below loop
        all_columns_we_need = data.columns[number_of_columns]                #create a new list of variable with [] provided by user
        needed_dataframe = data[all_columns_we_need]                         #create a new data frame using the needed columns
        
        
        for i, col in enumerate(needed_dataframe.columns):                            #start loop with new data frame  
            b=''                                                                      #empty string initialised to assign dtype of every column                                                                                 
            b=data[col].dtype
            if len(data[col].unique())<15 or b==object :                              #condition to check categorical data, if no. of unique items in a column <15 or if the type of column is object 
                g = sns.factorplot(col, data=data, aspect=1.5, kind="count", size=4)  #barplot/factorplot from seaborn library for categorical data   
                if b==object:                                                         #if dtype is object, then rotate the x-axis to 45 degrees
                    g.set_xticklabels(rotation=45)

                plt.title('Barplot of {0}'.format(col),fontsize=10)
                plt.xlabel('{0}'.format(col))                                            #x-axis label
                plt.ylabel('Count')                                                      #y-axis label 
                plt.savefig('C://Users//Vinay//Downloads//new_images//barplot_{0}.png'.format(col))                #saving to default directory
                plt.show()                                                                                         #show all graphs
            else:                                                                       #for numerical data
                plt.hist(needed_dataframe[col])                                         #plot histogram using matplotlib
                plt.title('Histogram of {0}'.format(col))
                plt.xlabel('{0}'.format(col))                                           #x-axis label       
                plt.ylabel('Frequecy of {0}'.format(col))                               #y-axis label 
                plt.savefig('C://Users//Vinay//Downloads//new_images//histogram_{0}.png'.format(col))             #saving to default directory
                plt.show()                                                                                        #show all graphs 
                plt.boxplot(needed_dataframe[col])                                     #plot boxplot using matplotlib  
                plt.title('Boxplot of {0}'.format(col))                                #title of plot
                plt.xlabel('{0}'.format(col))                                          #x-axis label
                plt.savefig('C://Users//Vinay//Downloads//new_images//boxplot_{0}.png'.format(col))               #saving to default directory
                plt.show()                                                                                        #show all graphs 
            


# In[19]:


graph_version2('cars',[1,3,5])


# # Graph function version 3:

# Till now the graphs were getting saved in the same directory as provided by the function.
# The next step we thought of giving users liberty to select their own dirctory. Now, they can access any dataset, select the desired variables and give the path to save all the graphs.
# 
# eg.  graph_version3( 'cars' , [1,3,5] ,'C://Users//Vinay//Downloads//new_images//graphs1')

# In[21]:


def graph_version3(x,number_of_columns,newpath):                 #defining function to provide dataset, index of column in [] and directory
    import pandas as pd                                          #importing libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns    
    import os
    
   
    data=pd.read_csv(x+'.csv')                              #reading csv
    if not os.path.exists(newpath):                         #condition to check if folder doesn't exist, create a new folder
        os.makedirs(newpath)
    
    if number_of_columns == None:                           #condition to give all graphs if no columns selected
        for i, col in enumerate(data.columns):              #loop starts for plots
            b=''                                            #empty string initialised to assign dtype of every column  
            b=data[col].dtype
            if len(data[col].unique())<15 or b==object :       #condition to check categorical data, if no. of unique items in a column <15 or if the type of column is object 
                g = sns.factorplot(col, data=data, aspect=1.5, kind="count", size=4)    #barplot/factorplot from seaborn library for categorical data 
                if b==object:                                                           #if dtype is object, then rotate the x-axis to 45 degrees
                    g.set_xticklabels(rotation=45)

                plt.title('Barplot of {0}'.format(col),fontsize=10)                      #title of plot 
                plt.xlabel('{0}'.format(col))                                            #x-axis label 
                plt.ylabel('Count')                                              #y-axis label
                plt.savefig(newpath+'//barplot_{0}.png'.format(col))                     #saving to specified direcorty provided by users
                plt.show()                                                               #show all graphs

            else:                                                                        #for numerical data
                plt.hist(data[col])                                                      #plot histogram using matplotlib
                plt.title('Histogram of {0}'.format(col))                                #title of plot
                plt.xlabel('{0}'.format(col))                                            #x-axis label
                plt.ylabel('Frequecy of {0}'.format(col))                                #y-axis label 
                plt.savefig(newpath+'//histogram_{0}.png'.format(col))                   #saving to specified direcorty provided by users      
                plt.show()                                                               #show all graphs 
                plt.boxplot(data[col])                                                   #plot boxplot using matplotlib
                plt.title('Boxplot of {0}'.format(col))                                  #title of plot
                plt.xlabel('{0}'.format(col))                                            #x-axis label
                plt.savefig(newpath+'//boxplot_{0}.png'.format(col))                     #saving to specified direcorty provided by users
                plt.show()                                                               #show all graphs 
    else:
        all_columns_we_need = data.columns[number_of_columns]                            #create a new list of variable with [] provided by user 
        needed_dataframe = data[all_columns_we_need]                                     #create a new data frame using the needed columns
        
        
        for i, col in enumerate(needed_dataframe.columns):                               #start loop with new data frame
            b=''                                                                         #empty string initialised to assign dtype of every column
            b=needed_dataframe[col].dtype
            if len(needed_dataframe[col].unique())<15 or b==object :                      #condition to check categorical data, if no. of unique items in a column <15 or if the type of column is object 
                g = sns.factorplot(col, data=needed_dataframe, aspect=1.5, kind="count", size=4)    #barplot/factorplot from seaborn library for categorical data 
                if b==object:                                                                       #if dtype is object, then rotate the x-axis to 45 degrees
                    g.set_xticklabels(rotation=45)

                plt.title('Barplot of {0}'.format(col),fontsize=10)                        #title of plot
                plt.xlabel('{0}'.format(col))                                              #x-axis label
                plt.ylabel('Count')                                                        #y-axis label
                plt.savefig(newpath+'//barplot_{0}.png'.format(col))                       #saving to specified direcorty provided by users  
                plt.show()                                                                 #show all graphs

            else:                                                                       #for numerical data
                plt.hist(needed_dataframe[col])                                          #plot histogram using matplotlib
                plt.title('Histogram of {0}'.format(col))                                #title of plot
                plt.xlabel('{0}'.format(col))                                            #x-axis label
                plt.ylabel('Frequecy of {0}'.format(col))                                #y-axis label
                plt.savefig(newpath+'//histogram_{0}.png'.format(col))                   #saving to specified direcorty provided by users
                plt.show()                                                               #show all graphs
                plt.boxplot(needed_dataframe[col])                                       #plot boxplot using matplotlib
                plt.title('Boxplot of {0}'.format(col))                                  #title of plot
                plt.xlabel('{0}'.format(col))                                            #x-axis label
                plt.savefig(newpath+'//boxplot_{0}.png'.format(col))                     #saving to specified direcorty provided by users
                plt.show()                                                               #show all graphs 
            


# In[18]:


graph_version3('cars',[1,3,5],'C://Users//Vinay//Downloads//new_images//graphs1')


# In[4]:


import os
os.getcwd()


# In[3]:


os.chdir('C:\\Users\\Vinay\\Downloads')


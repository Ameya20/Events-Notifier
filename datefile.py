def main(s):
    import datefinder
    import pandas as pd
    df=pd.read_csv('projectData.csv')


##    s="""
##       ...: ...
##       ...: entries are due by January 29th, 2020 at 8:00pm
##       ...: """
##    line1=""" 6th September 2016
##    (Name of the guest)
##    (Address of the guest)Dear X,
##    My name is Maria. I am a student at The South Berge University.Today """

    matches = datefinder.find_dates(s)
    for i in matches:
##    print(i.hour)
##        print(i)
##        print(i)
        df.iat[0,0]=1
        df.iat[0,3]=i.day
        df.iat[0,4]=i.month
        df.iat[0,5]=i.year
        df.iat[0,6]=i.hour
        df.iat[0,7]=i.minute
        df.iat[0,8]=i.second
  
        df.to_csv('projectData.csv' , index=False)
        print("DMYT done")

##main()

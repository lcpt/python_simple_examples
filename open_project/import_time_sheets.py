
from __future__ import print_function
import csv
from datetime import timedelta
from datetime import date, datetime

projects_file_name= 'projects.csv'
users_file_name= 'users.csv'
tasks_file_name= 'work_packages.csv'
tasks_journals_file_name= 'work_package_journals.csv'
time_entries_file_name= 'time_entries.csv'

def load_csv_file(fileName):
    retval= dict()
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(fileName, ' column names are {',row,'}')
                line_count += 1
            else:
                recId= int(row[0])
                retval[recId]= row
                line_count += 1
        print('Processed ',line_count,' lines.')
    return retval
    

# Load project records
projectDict= load_csv_file(projects_file_name)
# Load user records
userDict= load_csv_file(users_file_name)
# Tasks records
taskDict= load_csv_file(tasks_file_name)
# Tasks journals
taskJournalsDict= load_csv_file(tasks_journals_file_name)
# Time entries
timeEntries= load_csv_file(time_entries_file_name)

timesheet= dict()
for key in projectDict.keys():
    timesheet[key]= dict()
for key in taskDict.keys():
    task= taskDict[key]
    projectId= int(task[2])
    projectTasks= timesheet[projectId]
    projectTasks[key]= dict()
    projectTask= projectTasks[key]
    projectTask['Luis']= list()
    projectTask['Ana']= list()

for key in timeEntries.keys():
    te= timeEntries[key]
    projectId= int(te[1])
    projectName= projectDict[projectId][1]
    userId= int(te[2])
    userLogin= userDict[userId][1]
    taskId= int(te[3])
    task= taskDict[taskId]
    taskName= task[3]
    start= datetime.strptime(te[11], '%Y-%m-%d %H:%M:%S.%f')
    delta= timedelta(hours= float(te[4]))
    end= start+delta
    dateString= start.strftime("[%Y-%m-%d %a %H:%M]--")
    dateString+= end.strftime("[%Y-%m-%d %a %H:%M]")
    dateString+= ' => '+ str(delta)[:-3]
    projectTask= timesheet[projectId][taskId]
    if(userLogin=='l.pereztato@gmail.com'):
        projectTask['Luis'].append(dateString)
    elif(userLogin=='ana.ortega@xcingenieria.com'):
        projectTask['Ana'].append(dateString)
    #print(projectName, '|', taskName, '|', userLogin, '|', dateString, '|', delta)

for prjKey in timesheet.keys():
    project= timesheet[prjKey]
    projectName= projectDict[prjKey][1]
    print('* '+projectName)
    for taskKey in project.keys():
        task= project[taskKey]
        taskName= taskDict[taskKey][3]
        print('** '+taskName)
        for user in task.keys():
            print('*** '+user)
            print('    :LOGBOOK:')
            timeRecords= task[user]
            for tr in timeRecords:
                print('    CLOCK: '+tr)
            print('    :END:')

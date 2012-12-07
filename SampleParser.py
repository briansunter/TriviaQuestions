import csv
data=csv.reader(open('GeneralKnowledgeQuestions.csv',"rU"),delimiter=',',dialect=csv.excel_tab)
for question  in data:
    print "Question: "+question[0]+" Answer: "+question[1]

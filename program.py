import os
import re
import linecache

def runQuery(query_file_path):
    print "running query..."
    query='$JENA_HOME/bin/sparql --data=/home/nausheenfatma/RDF/data.ttl --query='
    query=query+query_file_path
    os.system(query) #runs linux terminal commands from python


def makeQuery(querynumber,parameters,queryFilePath):
    query_template_file="/home/nausheenfatma/RDF/query_templates.csv"
    line = linecache.getline(query_template_file, querynumber)
    query=line.split("###")[1]
    #print query
    #print parameters[0]
    query=query.replace('"%s"','"'+parameters[0]+'"')
    #print "this"
    print query
    queryFile=open(queryFilePath,"w")
    queryFile.write(
    "PREFIX dc:    <http://purl.org/dc/elements/1.1/> \n" + 
    "PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#> \n" +
    "PREFIX wot:   <http://xmlns.com/wot/0.1/> \n" +
    "PREFIX foaf:  <http://xmlns.com/foaf/0.1/> \n" +
    "PREFIX owl:   <http://www.w3.org/2002/07/owl#> \n" +
    "PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#> \n" +
    "PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n" +  
    "PREFIX vs:    <http://www.w3.org/2003/06/sw-vocab-status/ns#>  \n" + 
    "PREFIX faculty: <http://iiit.ac.in/people/faculty#> \n" + 
    "PREFIX student: <http://students.iiit.ac.in#> \n" + 
    "PREFIX course: <http://courses.iiit.ac.in#> \n")
    queryFile.write(str(query))
    queryFile.close()
    
def findQueryNumber(question):
    #c1=re.compile(r"^[wW]ho(?: teaches| is the teacher of| takes)? [`']{0,2}((?:[A-Z]\.)+|[A-Z]+)[`']{0,2} ?\??")
    c2=re.compile("What are the courses taken by (.*)")
    c1=re.compile("Who teaches (.*)")
    if c2.match(question):
        print "matched"
        return 2,c2.match(question).groups()
        #print len(c2.match(question).groups())
    if c1.match(question):
        print "matched"
        return 1,c1.match(question).groups() 
    return 0,0


#program starts here
query1="Who teaches NLP Applications"
query2="What are the courses taken by NAUSHEEN FATMA"
query3="What are the courses taken by HARISH YENALA"
queryFilePath="/home/nausheenfatma/RDF/query1.rq"
queryNumber,queryParameters=findQueryNumber(query3
)
makeQuery(queryNumber,queryParameters,queryFilePath)
runQuery(queryFilePath)


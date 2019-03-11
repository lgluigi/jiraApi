import re
from jira import JIRA
#----username e password para autenticação http Basic
username =  ''
password = ''
#----nome do projeto que irá fazer query de issue
projeto = ''


# ---Autenticação http basic
jira = JIRA(basic_auth=(username, password), options={'server': ''})

#--- Lista de issues na base do projeto com status diferente de Resolved, Closed, Verification e Rejected
query = 'project ='+projeto+' and status not in (Resolved,Closed,Verification,Rejected) and Referência is null '
pjissues = jira.search_issues(query, maxResults=1)

pjissues_list = []
gcissues_list = []

#-----guarda os objetos issue em uma lista 
for issue in pjissues:
    pjissues_list.append(str(issue))
    
gcquery = 'project = GESTCONFIG and status not in (Resolved,Closed,Verification,Rejected) and Referência is null'
gcissues = jira.search_issues(gcquery)


cont = 0

for issue in pjissues:
    issue = jira.issue(pjissues_list[cont])
    project = issue.fields.project.key
    description = issue.fields.description
    summary = issue.fields.summary  
    print('teste jira :|'+project+' | '+summary+' | '+description)
    new_issue = jira.create_issue(project='', summary=summary,
                              description=description, issuetype={'name': 'Task'})
    issue.update(customfield_10151=str(new_issue.key))
    cont = cont+1


print(pjissues_list)
#-------adiciona issue na base interna pela quantidade de referencias nulls na base externa


#    
  #após criar issue na base interna , editar o issue externo e adicionar o ID da interno como referencia

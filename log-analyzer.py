#!/usr/bin/env python

import psycopg2

def send_query(query):
    '''Makes a query to the database.'''
    db=psycopg2.connect(database="news")
    c=db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

def print_result(query,flag):
    '''reads and prints the result obtained from send_query()
       varies in queries for different requests using flag
       0 for views and 1 for percentage'''
    if flag==0:
          st=' views.'
    elif flag==1:
          st=' %.'
    results=send_query(query)
    for result in results:
        print(str(result[0]) + ' - ' + str(result[1]) + st)
#Find top 3 posts of all time
q1='''select title,count(*) as views from articles inner join 
      log on CONCAT('/article/',articles.slug)=log.path
      where log.status='200 OK'
      group by log.path,articles.title order by views desc limit 3;'''
#Views on posts by different authors
q2='''select authors.name,count(*) as num from articles inner join 
      authors on articles.author = authors.id inner join 
      log on CONCAT('/article/',articles.slug)=log.path where     
      log.status='200 OK' group by authors.name order by num desc;'''
#Find Days having more than 1 percent downtime
q3='''select * from (
      select t1.day, round(cast((100*t2.num) as numeric) / cast(t1.num as numeric), 2) as err from
      (select cast(time as date) as day, count(*) as num from log group by day) as t1
      inner join
      (select cast(time as date) as day, count(*) as num from log where status like '%404%' group by day) as t2
      on t1.day=t2.day)
      as total where err > 1.0;'''

#print the result of queries using the print_result()
print("Top 3 Posts of all time:")
print_result(q1,0)
print("\nAuthor Leaderboard:")
print_result(q2,0)
print("\nDays with more than 1% errors:")
print_result(q3,1)
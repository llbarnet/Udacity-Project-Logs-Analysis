#!/usr/bin/python3

import psycopg2

DBNAME = 'news'

try:
    db = psycopg2.connect(database=DBNAME)
except psycopg2.Error as er:
    print("Not able to connect")
    print(er.pgerror)
    print(er.diag.message_detail)
    sys.exit(1)
else:
    print("Connected...")

crs = db.cursor()


# What are the most popular three articles of all time?
crs.execute("""select articles.title, count(*) as num from articles, log
where articles.slug = substring(log.path, 10)
group by articles.title order by num desc limit 3""")
result = crs.fetchall()

# Who are the most popular article authors of all time?

crs.execute("""select authors.name, count(*) as num from authors, articles, log
where authors.id = articles.author and articles.slug = substring(log.path, 10)
group by authors.name order by num desc""")
result2 = crs.fetchall()

# On which days did more than 1% of requests lead to errors?
# create views
crs.execute("""create view errtotals as select date(time),
count(*) as num from log where status != '200 OK' group by date(time)""")

crs.execute("""create view visittotals as select date(time),
count(*) as num from log group by date(time)""")


# run query
crs.execute("""select errtotals.date, errtotals.num, visittotals.num
from errtotals, visittotals
where errtotals.date = visittotals.date
and errtotals.num > visittotals.num * 0.01""")
result3 = crs.fetchall()


# print results of queries
print('The three most popular articles with total views are:')
for article in result:
    print("{}, {} views").format(article[0], article[1])
print('The most popular authors with total article views of all time are:')
for authors in result2:
    print("{}, {} total views").format(authors[0], authors[1])
print("Days where more than 1% of requests led to errors:")
for i in result3:
    percent = round(i[1] / (i[2]*0.01), 1)
    print("{}, {}%").format(i[0], percent)

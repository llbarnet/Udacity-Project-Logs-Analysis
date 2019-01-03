#NEWS ANALYSIS
  This is a simple python script allowing users to evaluate three questions from the news database. By running this code you can determine the:
  1. three most popular articles of all time
  2. the most popular authors of all time
  3. which days more than 1% of requests lead to errors.

##Installation
  You should have **python** and **postgresql** installed on your machine.
  In order to properly run this code you will need access to the news database.
    - To begin, load the data from the news database into your local database.
    - Open the command line and cd into the appropriate folder with the news database.
    - Use the command:
    **pasql -d news -f newsdata.sql**
    - You should now be able to look through the news database

  Download news_analysis.py and add it to the same folder with the database.
  Once all features are installed, cd into the appropriate folder with the news database and the news_analysis.py files.
    -run **python news_analysis.py** into the command line.
    -You will see "connected..." if the database connects successfully


##Views
  This code runs two views: errtotals and visittotals.
  `Errtotals is a view that sums the total request errors that occurred on an individual day. It has two columns, date (time) and total errors (int).`
  `Visittotals is a view that sums the total visits to the site on an individual day. It has two columns, date (time) and total visits (int).`

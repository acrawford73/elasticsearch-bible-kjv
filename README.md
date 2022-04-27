elasticsearch-bible-kjv
=======================

The Holy Bible (King James Version) for Elasticsearch

This project is 100% free to use.

Have you ever wondered how many times a word occurs in the Bible? One option is picking up a heavy Strong's Concordance reference, but looking it up WILL be very time consuming. Not anymore...

The purpose of this project is to be able to instantly search for any word or text string in the KJV Bible using Elasticsearch engine server with Elasticsearch-Kibana dashboard browser interface.

The dashboard interface has been pre-configured to present search results by:
- Total Hits
- Testament
- Book
- Chapter
- Verse
- Top 50 Near Words (that were also found in verses from your search results)
- Up to 300 verse results can be navigated

To read more about how to customize the search criterias, head on over to this page:
https://lucene.apache.org/core/2_9_4/queryparsersyntax.html

**NOTE:** Knowledge of how to setup and use Elasticsearch and Kibana is recommended. Detailed install instructions can be provided if there is enough community interest. Word 2007 or greater is required if you wish to modify the XLSX files for another translation.

The project comes with the following files:
- Python script (kjv.py)
- Kibana script (kibana-kjv.json)
- CSV files for each book of the Bible (created from XLSX files, exported as "CSV Comma Delimited")
- XLSX files for each book of the Bible

Before running the Python script **kjv.py**, Elasticsearch package for Python must be installed using the following command:

**pip install elasticsearch**

Only Python version 2.7 has been tested.

**NOTE:** An index must be created in the Elasticsearch instance before the import script is run. Create an index called 'bible'. If you wish to use another name for the index go ahead, just make sure you update the Python script where "index_name = bible".

To import the CSV files into your Elasticsearch instance run this command:

**python kjv.py**

After import there should be **31102** verses stored. One Bible verse equals one Elasticsearch document. In the Kibana interface, enter * as the search criteria and hit 'enter'. Total Hits should read **31102**. Remarkably, the entire King James Bible index only consumes ~16MB of drive space.

*** If you are familiar with virtual machines, one of the easiest ways to get this going is to install VirtualBox on your Mac or PC. Create a Redhat/CentOS 64-bit virtual machine with at least 1024MB of memory. Then install Elasticsearch server and if setup correctly you can access it from your browser. I am leaving out many steps here but it can work...

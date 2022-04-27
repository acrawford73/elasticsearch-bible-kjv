elasticsearch-bible-kjv
=======================

The Holy Bible (King James Version) for Elasticsearch

Have you ever wondered how many times a word occurs in the Bible? One option is picking up a heavy Strong's Concordance reference, but looking it up WILL be very time consuming. Not anymore...

The purpose of this project is to be able to instantly search for any word or text string in the KJV Bible using Elasticsearch engine server with Elasticsearch-Kibana dashboard browser interface.

To read more about how to customize the search criterias, head on over to this page:
https://lucene.apache.org/core/2_9_4/queryparsersyntax.html

The project comes with the following files:
- Python script (kjv.py)
- Kibana script (kibana-kjv.json)
- CSV files for each book of the Bible (created from XLSX files, exported as "CSV Comma Delimited")
- XLSX files for each book of the Bible

Before running the Python script **kjv.py**, Elasticsearch package for Python must be installed using the following command:

**pip install elasticsearch**

**NOTE:** An index must be created in the Elasticsearch instance before the import script is run. Create an index called 'bible'. If you wish to use another name for the index go ahead, just make sure you update the Python script where "index_name = bible".

To import the CSV files into your Elasticsearch instance run this command:

**python kjv.py**

After import there should be **31102** verses stored. One Bible verse equals one Elasticsearch document. In the Kibana interface, enter * as the search criteria and hit 'enter'. Total Hits should read **31102**. Remarkably, the entire King James Bible index only consumes ~16MB of drive space.


# Neo4J Tweepy Streamer
Write tweets having to do with a list of terms to a graph database. Uses the Twitter Application API and Neo4J
## Status
At the moment the project is in a state of development and as such is not currently functional in its entirety. Individual parts are implemented, and I have successfully gotten everything working myself but as it is this repository is not in working order.

## How NTS works
NTS uses a Stream from the Tweepy package to receive live Tweets having to do with a specified list of terms from the Twitter Application API. NTS then adds these tweets to a Neo4J graph with related data, using the py2neo package.

Tweets, Users, Tweet Sources, URL's and Hashtags are all made into py2neo nodes (edges) and have relevant relationships (vertices) assigned to them before being committed to the graph. When committed, Neo4J MERGE's are used in order to aggregate all


## Graph Model
The graph schema is closely modeled off of the schema used in the official 'Russian Trolls' Neo4J sandbox, with the addition of the User-RETWEETS->User relationship and removal of the trolls node and associated relationships.

![Graph Schema](https://i.imgur.com/sPb0hsM.png)

## Config
#### There are three methods of configuration:

1. A default config file (empty_config.ini) is provided. Once the required settings are configured the file must be renamed to 'config.ini'.

2. There is a set_settings method (requires a dictionary with keys equivalent to the settings in the ini file) or individual setter methods available by importing the Config class from the confighandler module. If using this alternative method, the settings method/s must be called before initializing other package objects as they rely on these settings.

3. You can supply a dictionary containing the settings with keys equivalent to the settings in the ini file directly to the GraphHandler and TwitterStreamHandler.

#### Twitter
In order to use the Twitter API, the user is required to apply as a Twitter application developer at [dev.twitter.com](https://developer.twitter.com/) (applications are instantly accepted from what I can tell), and then register an app within their developer dashboard. Once the application is created, navigate to it's 'Keys and Tokens' page and generate the required keys/tokens.

#### Neo4J
The user must also have access to a Neo4J server. This can reside on the local machine or a remote one requiring the proper settings have been applied on the remote server to allow inbound remote connections. I have tested against both local and remote server instances, but only using Neo4J's binary protocol 'Bolt'; there is a http, and https protocol available and should work fine, but I have never used it so YMMV. The protocol used is determined via the NEO4J_HOST setting provided by the user. A bolt example is 'bolt://XXX.XXX.XXX.XXX:7687'  

The application also requires a user with access to the server, I suggested that one is made solely for the use of the application and another for the user to use on the web dashboard as I was running into authorization issues when sharing the same account.

##### The required settings are as follows:
```ini
[Twitter API Settings]  
API_KEY = 'Consumer API Key'  
API_SECRET = 'Consumer API Secret Key'  
ACCESS_TOKEN = 'Access Token'  
ACCESS_TOKEN_SECRET = 'Access Token Secret'  


[Neo4J Settings]  
NEO4J_HOST = 'Neo4J Server Access URL (Only Bolt connections have been tested)'  
NEO4J_USER = 'Neo4J Username'  
NEO4J_PASSWORD = 'Neo4J Password'  
```

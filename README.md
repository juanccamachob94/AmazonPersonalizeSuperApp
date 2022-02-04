# RecommenderUsersManagement

In order to recommend content based on the data of the user who requests it, this application is built that collects the categories in which the information to be used in the query of the data to be recommended is classified.

By exploring this requirement, AmazonPersonalize was found to be an ideal tool to meet it. For this reason, the necessary logic is implemented to register, in the related S3 bucket, the data classified in Users, Items and Interactions. The attributes for each of these classifications are listed below.

```
Users: user_id, device_id, timestamp
Items: item_id, site
Interactions: user_id, item_id, event_type, timestamp
```


### How to feed CSV file for Users?
It consists of the simplest data source to fill. This process requires a basic registration in the CSV file, validating the uniqueness of users through the primary key user_id.

### How to feed CSV file for Items?
Items can be registered in a simple way, however it was developed through an implementation similar to the previous point (Users), the ability to register Items as the base data is registered to recommend, which, as will be seen later, correspond to the articles to recommend to users.

In this way, when each article is registered, the category will be registered non-repeatedly in the Items collection.

### How to feed the CSV file for Interactions?
The interactions are updated in a simple way as in the case of users. Before each record, the existence of the item and the user is validated. Additionally, this interaction requires feeding the event to AmazonPersonalize in order to continue with the learning required to refine and update the results over time.


### How to feed the data to recommend?
Articles are currently used as data to recommend. The objective is to receive the id of the user to recommend. Based on this id, AmazonPersonalize returns a list of item recommendations. Subsequently, for the recommended items, the category of the recommended data is obtained to finally consult the articles with that category from an external database to recommend to the user.

At a technical level, these articles are obtained from the XML files published by Brightspot for each site.


## Technical details

### 1. Register of articles
The CentralizedDataGenerator service adds articles to the Dynamo database whose publication date is greater than or equal to a certain number of days and hours, taking into account time periods in months or years also received as a parameter. These articles are obtained from the metadata read from BSP in XML format. For the execution of this service, for each iteration the SitemapContentItemProcessor class is called, which will send the data obtained from the article to Dynamo and in turn will report the new category to the CSV Items file.

### 2. Recommendations.
Each recommendation service must be configured depending on the context of the recommendations. Currently this service located in the ArticlesRecommendationsClient class returns a collection of articles that belong to the preference categories of the user to whom the recommendation will be made. As parameters of this class, the user id and the limit amount of articles that will be recommended to the user are required.

The first task in this class (ArticlesRecommendationsClient) is to get the list of recommendations. Currently you get a list of recommendations of the same size as the number of articles that will be recommended to the user. This strategy is not 100% correct, however it starts from the idea that there will be at least 1 article for each category recommended to the user.

The probability that the number of articles recommended to the user is less than the number of recommendations is considered very low to date; Otherwise, it is proposed to increase the number of recommendations to the number of articles to recommend to the user multiplied by 1.5. Since this recommendation does not have a mathematical foundation, it is expected that a definitive solution will be proposed empirically for this collection of recommendations.

Once the recommendations of the RecommendationsService class have been obtained, for each of them a list of articles is obtained with the same limit expected by the user. An accountant will determine when all expected recommendations have been completed within the cycle that cycles through all recommendations. In this way, when the maximum recommendation quota is met, the system will finish storing the articles and will return a list of these as a result.

The ArticlesByRecommendationService class is responsible for generating the list of articles for each recommendation, currently based on categories.


### 3. Creation of users, interactions and items.
When meeting requirements related to storing information in CSV files, the following diagram is used that explains the distribution of the classes that want to achieve this objective in these three contexts: users, interactions and items.
DAOFactory must be requested to manufacture a DAO model instance for any of these cases, delegating the task to CSVDAOFactory or DynamoDAOFactory as appropriate. Each DAO instance uses a DBManager according to the database engine that is being used. These DBManager classes allow you to manage data in the database in a generic way using a ManagerClient that contains the access credentials, or all the complementary information to manage the entity of the database to be used; in the case of CSV it contains the dynamic and static paths of the file, and for Dynamo the client, the resource and the Dynamo table to use. All this in collaboration with the ManagerFactory.

This manufacturing configuration allows the reuse of clients to different services, avoiding the repeated instance of objects for the same purpose. For this reason, also in many parts of the code, dict variables called instances are located that seek to store a cache of instances in a practical way and especially by minimizing the amount of resources required in the execution of the application.

![image](https://user-images.githubusercontent.com/42450812/144518804-ced9e6ac-8eeb-4841-a51e-15eae56bac62.jpg)


On the other hand, in support of the connection to the database and in general to any Amazon service, the AmazonCredentialsContainer object is created that contains, as its name indicates, the necessary credentials to consume Amazon services. The default child class of this class uses the default keys defined in the environment. As mentioned previously, the factory related to the instance of this default class seeks to maintain the same instance for any service that wants to be consumed.

This architecture is designed to easily integrate credentials to any application resource, adaptable to multiple credentials for multiple purposes to consider in the future.


![image](https://user-images.githubusercontent.com/42450812/144520705-59a2a738-00d6-4d84-93c0-4a205b01b843.jpg)


In a similar way, an architecture is built for the AmazonPersonalizeSolution objects. Its objective is to manage the AmazonPersonalize solutions independently without the need to rebuild all the logic and therefore reuse the existing logic with variables with different values.

Aligned with the previous descriptions, for Python there are Amazon resources and clients that were encapsulated in the following classes in order to centralize the use of the boto library with their respective credentials.


![image](https://user-images.githubusercontent.com/42450812/144518850-99cb9349-4fa7-496b-ad1c-a4c2dc9a1d02.jpg)


### 4. Lambda
The implementation can be executed from lambda easily through a method that receives the event and the context. In this case all the lambda logic was encapsulated in the lambdas module. There are 3 lambdas classes with specific purposes:

#### 4.1 Users Lambda
Its purpose is to register and / or update users in the AmazonPersonalize training CSV file.

#### 4.2 Item Recommender Lambda
Lambda to recommend a certain number of articles to a user

#### 4.3 Interactions Lambda
Lambda for logging interactions in training CSV file and AmazonPersonalize



![image](https://user-images.githubusercontent.com/42450812/144520659-2d240689-91e8-4b20-8956-6e57eeed56b8.jpg)


### 5. Deployment
The project consists of an API to consume the mentioned services. This is consumed by pointing to the lambda methods that resolve the requests and return a result in json format.

Thanks to the API Gateway tool, an api is created from Amazon that connects to the lambda service allowing requests to be received through POST requests with the following formats:

```
Users:
{
  "type": "user",
  "content": {
    "action": "save",
    "user": {
      "user_id": 332,
      "device_id": 2
    }
  }
}

Interactions:
{
  "type": "interaction",
  "content": {
      "interaction": {
          "user_id": 332,
          "item_id": "Deportes|ADN40"
      }
  }
}


Recommendations:
{
  "type": "recommender",
  "content": {
	"user_id": 332,
	"articles_limit": 10,
	"recommendation_source": "algoritia"
  }
}

```


### 6. Considerations
- It is estimated that given the volume of information to receive through requests, it will be required to switch from CSV to Dynamo for all data to be recorded
- Improve the implementation of data consumption from the Dynamo database
- The generation of the data is completely independent. To date, there is only the implementation of articles from the management module





### 7. API documentation
Currently the API has 3 types of services consumed through the following url through the POST method described below.

Current URL: `https://rgfjqp9lh1.execute-api.us-east-1.amazonaws.com/dev/recomendador`

#### Service 1 - User registration
For the consumption of the recommendation service, some user-specific data is required. These data are recorded through this request that requires the user identifier and the identifier of the device being used.

##### Considerations
The user id can be a string or an integer.
The device id has the values 1 for Android, and 2 for iphone.
Sending a user registration request creates or updates the information depending on whether or not the user is located through their unique user_id key


##### Request example
```
{
  "type": "user",
  "content": {
    "action": "save",
    "user": {
      "user_id": 332,
      "device_id": 2
    }
  }
}
```

#### Service 2 - Interaction registration

Each interaction with each user news must be registered to continue training the recommendation algorithm in order to guide the recommendations to the user's preferences. 

##### Considerations
The item id belongs to the identifier of the item to recommend. The following example concatenates the category used in Brightspot for ADN40.

##### Request example
```
{
  "type": "interaction",
  "content": {
      "interaction": {
          "user_id": 332,
          "item_id": "Deportes|ADN40"
      }
  }
}
```
#### Service 3 - Request for recommendations
To obtain the collection of data to recommend based on the items linked to the user through the user registry and their corresponding interactions, the user's id is requested, how much data will be limited in the recommendations and the source of recommendation.

##### Considerations
The recommended amount of data varies between `0` and `n`, where n is the value assigned for the `data_limit` attribute of the request.
Possible values for `recommendation_source` are `algoritia` and `default`.

##### Request example
```
{
  "type": "recommender",
  "content": {
	"user_id": 332,
	"data_limit": 10,
	"recommendation_category": 2
  }
}
```

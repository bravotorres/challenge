# Pixyalbum backend challenge

Goals:

- Create a Dockerized Django project with two services (containers)
	- django-app & mysql-db

- Create an API with django in order to have 3 main functions
	- Create an album
	- Delete an album
	- Add more photos to an existing album

Definition of the models:

Album:
- Title
- Soft cover / Hard cover
- Photos
- Date of creation

Photo:
- URL of the image
- Caption
- Date of creation


Constraints:

- One Album has many photos and the photo only belongs to one album
- We need to use JSON for the API
- We do not need to implement authentication for this challenge


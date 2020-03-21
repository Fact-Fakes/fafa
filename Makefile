TAG = $(shell git describe --tags --always)
PREFIX = fakebuster
REPO_NAME = $(shell git config --get remote.origin.url | tr ':.' '/'  | rev | cut -d '/' -f 2 | rev)

all: images
images: image-backend image-frontend

image-frontend:
	docker build -f dockerfiles/frontend/Dockerfile -t $(PREFIX)/$(REPO_NAME)-frontend . # Build new image and automatically tag it as latest
	docker tag $(PREFIX)/$(REPO_NAME)-frontend $(PREFIX)/$(REPO_NAME)-frontend:$(TAG)  # Add the version tag to the latest image

image-backend:
	docker build -f dockerfiles/backend/Dockerfile -t $(PREFIX)/$(REPO_NAME)-backend . # Build new image and automatically tag it as latest
	docker tag $(PREFIX)/$(REPO_NAME)-backend $(PREFIX)/$(REPO_NAME)-backend:$(TAG)  # Add the version tag to the latest image

push: push-frontend push-backend

push-frontend:
	docker push $(PREFIX)/$(REPO_NAME)-frontend # Push image tagged as latest to repository
	docker push $(PREFIX)/$(REPO_NAME)-frontend:$(TAG) # Push version tagged image to repository (since this image is already pushed it will simply create or update version tag)

push-backend:
	docker push $(PREFIX)/$(REPO_NAME)-backend # Push image tagged as latest to repository
	docker push $(PREFIX)/$(REPO_NAME)-backend:$(TAG) # Push version tagged image to repository (since this image is already pushed it will simply create or update version tag)

clean:

restart-frontend:
	sudo make image-frontend && sudo docker-compose up
IMAGE_NAME := moon-board-climbing/keras

.PHONY: build

build :
	docker build . -t $(IMAGE_NAME)

run :
	docker run --runtime=nvidia -it -v `pwd`:/workdir -w /workdir $(IMAGE_NAME):latest bash

travis : build
	echo $(GIT_TOKEN) | docker login docker.pkg.github.com -u $(GIT_USERNAME) --password-stdin
	docker push docker.pkg.github.com/andrew-houghton/$(IMAGE_NAME)
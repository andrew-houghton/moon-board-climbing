IMAGE_NAME := bielsdown/moon-board-climbing:latest

.PHONY: build

build:
	docker build . -t $(IMAGE_NAME)

bash:
	docker run --runtime=nvidia -it -v `pwd`:/workdir -e PYTHONPATH=/workdir -w /workdir $(IMAGE_NAME) bash

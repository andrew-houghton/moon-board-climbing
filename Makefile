build:
	docker build . -t andrew-houghton/moon

run:
	docker run --runtime=nvidia -it -v `pwd`:/workdir -w /workdir andrew-houghton/moon:latest bash

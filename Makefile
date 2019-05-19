.PHONY: build

build :
	docker build . -t andrew-houghton/moon

run :
	docker run --runtime=nvidia -it -v `pwd`:/workdir -w /workdir andrew-houghton/moon:latest bash

travis : build
	echo $(GIT_TOKEN) | docker login docker.pkg.github.com -u $(GIT_USERNAME) --password-stdin
	docker push andrew-houghton/moon

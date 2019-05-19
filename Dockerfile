ARG image_base=tensorflow/tensorflow
ARG image_version=1.13.1
ARG image_tags=-gpu-py3
FROM ${image_base}:${image_version}${image_tags}

RUN pip install \
	numpy \
	pillow \
	keras \
	tqdm \
	sklearn \
	pygame \
	xgboost

WORKDIR "/src"

build:
	docker build . -t segmentio/papi-python-sdk
.PHONY: build

test:
	docker run -v "$(PWD)/reports:/papi-python-sdk/reports" segmentio/papi-python-sdk tox
.PHONY: test


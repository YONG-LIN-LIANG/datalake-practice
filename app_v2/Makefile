# Makefile

# Image and container names
IMAGE_NAME = ingestion-app-image
CONTAINER_NAME = ingestion-app
NETWORK_NAME = postgres_source_my-network

# 清除映像和容器
.PHONY: clean
clean:
	docker image rm -f $(IMAGE_NAME)
	docker container rm -f $(CONTAINER_NAME)

# 建立映像
.PHONY: build
build:
	docker build -t $(IMAGE_NAME):latest .

# 運行容器
.PHONY: run
run:
	docker run --name $(CONTAINER_NAME) --env-file ./docker.env --network $(NETWORK_NAME) $(IMAGE_NAME):latest

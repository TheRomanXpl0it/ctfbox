FROM --platform=$BUILDPLATFORM docker.io/oven/bun AS frontend 
WORKDIR /app
ADD ./frontend/package.json .
ADD ./frontend/bun.lockb .
RUN bun install
COPY ./frontend/ .
RUN bun run build

FROM public.ecr.aws/docker/library/golang:1.24

WORKDIR /app/

RUN apt-get update && \
	apt-get install -y python3-pip python3-dev python3-capstone python3-venv build-essential \
	iproute2 iputils-ping netcat-openbsd traceroute tcpdump ethtool iptables cmake \
	libcapstone-dev build-essential python3-capstone

COPY ./entry.sh /tmp/
RUN chmod +x /tmp/entry.sh
WORKDIR /app/src/
COPY ./src/go.mod ./src/go.sum /app/src/
RUN go mod download
WORKDIR /app/src/
COPY ./src/ .
WORKDIR /app/src/
RUN go build -o ctfserver .
WORKDIR /app/src/frontend
COPY --from=frontend /app/dist .
WORKDIR /app/src/

ENTRYPOINT [ "/tmp/entry.sh" ]

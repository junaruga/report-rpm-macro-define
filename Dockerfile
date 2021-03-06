ARG BASE_IMAGE=fedora:31
FROM ${BASE_IMAGE}

WORKDIR /work
COPY . .
RUN yum -y install rpmdevtools rpm-build
RUN rpm -q rpm
RUN rpm -q rpm-build

CMD ./test.sh

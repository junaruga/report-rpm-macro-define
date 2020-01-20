ARG BASE_IMAGE=fedora:31
FROM ${BASE_IMAGE}

WORKDIR /work
COPY . .
RUN dnf -y install rpm-build
RUN rpm -q rpm-build

CMD rpmbuild -ba foo.spec

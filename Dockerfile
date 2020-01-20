ARG BASE_IMAGE=fedora:31
FROM ${BASE_IMAGE}

WORKDIR /work
COPY . .

CMD rpmbuild -ba foo.spec

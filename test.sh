#!/bin/bash
set -ex

rpmdev-setuptree
rpmbuild -ba foo.spec
find ~/rpmbuild/ -type f

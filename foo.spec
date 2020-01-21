%global release 2
%if ! 0%{?release_string}
%define release_string %{release}%{?dist}
%endif

%global aaa 2
%{!?bbb:%define bbb %{aaa}}

%global ccc 2
%{!?ddd:%global ddd %{ccc}}

%define eee 2
%{!?fff:%define fff %{eee}}

# If this line is active, the define macro issue happens.
%bcond_without git

Summary: Ruby
Name: foo
Version: 2.7.0
Release: %{release_string}
Group: Development/Languages
License: MIT
URL: http://ruby-lang.org/

%description
Description.


%prep
rpm -q rpm
echo "release_string: %{release_string}"
echo "bbb: %{bbb}"
echo "ddd: %{ddd}"
echo "fff: %{fff}"


%install
rm -rf %{buildroot}

cat <<EOF > foo
#!/bin/bash

echo "foo"
EOF

chmod +x foo
mkdir -p %{buildroot}/%{_bindir}
cp -p foo %{buildroot}/%{_bindir}/foo


%files
%{_bindir}/foo


%changelog
* Thu Jan 16 2020 Jun Aruga <jaruga@redhat.com> 2.7.0-2
- Foo.

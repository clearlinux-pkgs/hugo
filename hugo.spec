Name     : hugo
Version  : 0.55.4
Release  : 11
URL      : https://github.com/gohugoio/hugo
Source0  : https://github.com/gohugoio/hugo/archive/v0.55.4/hugo-0.55.4.tar.gz
Source1  : http://localhost/cgit/projects/hugo-vendor/snapshot/hugo-vendor-0.55.0.tar.gz
Summary  : The world’s fastest framework for building websites
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: Pygments
Requires: docutils
BuildRequires : go

%description
Hugo is one of the most popular open-source static site generators. With its amazing speed and flexibility, Hugo makes building websites fun again.

%prep
%setup -q -n hugo-0.55.4
tar --strip 1 -xf %{SOURCE1}
mv src vendor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
unset GOPATH
go build -mod=vendor -v

%install
rm -rf %{buildroot}

## make_install_append content
install -d -m0755 %{buildroot}/usr/bin
install -m0755 hugo %{buildroot}/usr/bin/hugo
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/bin/hugo

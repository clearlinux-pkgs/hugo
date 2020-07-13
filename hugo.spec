#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hugo
Version  : 0.74.0
Release  : 50
URL      : https://github.com/gohugoio/hugo/archive/v0.74.0/hugo-0.74.0.tar.gz
Source0  : https://github.com/gohugoio/hugo/archive/v0.74.0/hugo-0.74.0.tar.gz
Source1  : http://localhost/cgit/projects/hugo-vendor/snapshot/hugo-vendor-0.74.0.tar.xz
Summary  : The world’s fastest framework for building websites
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT MPL-2.0 Unlicense
Requires: hugo-bin = %{version}-%{release}
Requires: hugo-license = %{version}-%{release}
Requires: Pygments
Requires: docutils
BuildRequires : Pygments
BuildRequires : buildreq-golang
BuildRequires : docutils

%description
Hugo is one of the most popular open-source static site generators. With its
amazing speed and flexibility, Hugo makes building websites fun again.

%package bin
Summary: bin components for the hugo package.
Group: Binaries
Requires: hugo-license = %{version}-%{release}

%description bin
bin components for the hugo package.


%package license
Summary: license components for the hugo package.
Group: Default

%description license
license components for the hugo package.


%prep
%setup -q -n hugo-0.74.0
cd %{_builddir}
tar xf %{_sourcedir}/hugo-vendor-0.74.0.tar.xz
cd %{_builddir}/hugo-0.74.0
mkdir -p ./
cp -r %{_builddir}/hugo-vendor-0.74.0/* %{_builddir}/hugo-0.74.0/./

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594664097
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  -f foo.make || go build -mod=vendor -v


%install
export SOURCE_DATE_EPOCH=1594664097
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hugo
cp %{_builddir}/hugo-0.74.0/LICENSE %{buildroot}/usr/share/package-licenses/hugo/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/hugo-0.74.0/docs/LICENSE.md %{buildroot}/usr/share/package-licenses/hugo/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/hugo-0.74.0/docs/content/en/about/license.md %{buildroot}/usr/share/package-licenses/hugo/0762264440482182008eccd281bcd674a208a2ed
cp %{_builddir}/hugo-vendor-0.74.0/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/Azure/azure-pipeline-go/LICENSE %{buildroot}/usr/share/package-licenses/hugo/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/Azure/azure-storage-blob-go/LICENSE %{buildroot}/usr/share/package-licenses/hugo/eee5b07a657266ef6c5c20acee6685ac6732cd19
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/BurntSushi/locker/UNLICENSE %{buildroot}/usr/share/package-licenses/hugo/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/hugo/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/PuerkitoBio/purell/LICENSE %{buildroot}/usr/share/package-licenses/hugo/33cd8e150548e595fbe201c6ca9df582976e71db
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/PuerkitoBio/urlesc/LICENSE %{buildroot}/usr/share/package-licenses/hugo/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/alecthomas/chroma/COPYING %{buildroot}/usr/share/package-licenses/hugo/820a47085e1f88859859d16b894bc93b47683498
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/armon/go-radix/LICENSE %{buildroot}/usr/share/package-licenses/hugo/96e730c77952892784bebe06fd42b297b67ea06e
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/aws/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/bep/debounce/LICENSE %{buildroot}/usr/share/package-licenses/hugo/82a8c1857c790563bd8e518ed775956006f68485
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/bep/gitmap/LICENSE %{buildroot}/usr/share/package-licenses/hugo/82a8c1857c790563bd8e518ed775956006f68485
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/bep/golibsass/LICENSE %{buildroot}/usr/share/package-licenses/hugo/8199e72e0dd480f4e58942cb7d99e2bbff41cb33
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/bep/tmc/LICENSE %{buildroot}/usr/share/package-licenses/hugo/86deafa660209c3e1ca6978b667af6d5d2e30efe
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/hugo/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/danwakefield/fnmatch/LICENSE %{buildroot}/usr/share/package-licenses/hugo/10a2ce5b9834456e89143edcc2a65b044dbde493
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/disintegration/gift/LICENSE %{buildroot}/usr/share/package-licenses/hugo/02b1b9a6cb5e0ee06071eb0549bb8161c1ab58db
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/dlclark/regexp2/LICENSE %{buildroot}/usr/share/package-licenses/hugo/91cd2d65a9945545fba9e4d03f279aff97470252
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/dustin/go-humanize/LICENSE %{buildroot}/usr/share/package-licenses/hugo/4b5f40487c165cf31691824a93d375fcb65ea30a
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/fortytw2/leaktest/LICENSE %{buildroot}/usr/share/package-licenses/hugo/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/frankban/quicktest/LICENSE %{buildroot}/usr/share/package-licenses/hugo/9abb08f99d05d02f923149766fa509b9a1d82368
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/hugo/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/ghodss/yaml/LICENSE %{buildroot}/usr/share/package-licenses/hugo/271aeaf56ee621c5accfc2a9db0b10717e038eaf
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/gobwas/glob/LICENSE %{buildroot}/usr/share/package-licenses/hugo/1b2d963c77ddfc6454ca369fc4884e87e256a2e1
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/hugo/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/hugo/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/hugo/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/google/wire/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/googleapis/gax-go/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2bda142bd58fd76f408cf18fa997d8fab0278a22
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/googleapis/gax-go/v2/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2bda142bd58fd76f408cf18fa997d8fab0278a22
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/gorilla/websocket/LICENSE %{buildroot}/usr/share/package-licenses/hugo/307711a68aa375a23d90191db6f720426cf88402
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/hugo/ece3df1263c100f93c427face535a292723d38e7
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/hashicorp/hcl/LICENSE %{buildroot}/usr/share/package-licenses/hugo/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/hugo/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/jdkato/prose/LICENSE %{buildroot}/usr/share/package-licenses/hugo/a1605d0f5823bc71559ce2bd0b50515687fbb97b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/jmespath/go-jmespath/LICENSE %{buildroot}/usr/share/package-licenses/hugo/4052101a660a7d8343c13ada130123f75f1dd408
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/kr/pretty/License %{buildroot}/usr/share/package-licenses/hugo/9893c30cda569ecb5d3f8d615986e948947cd56d
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/kr/text/License %{buildroot}/usr/share/package-licenses/hugo/9893c30cda569ecb5d3f8d615986e948947cd56d
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/kyokomi/emoji/LICENSE %{buildroot}/usr/share/package-licenses/hugo/ba44327dd26d6de65733341ace192d85ae2dc46d
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/magefile/mage/LICENSE %{buildroot}/usr/share/package-licenses/hugo/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/magiconair/properties/LICENSE %{buildroot}/usr/share/package-licenses/hugo/20d7220031a3670d7696be5330ebae9f49861d3b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/markbates/inflect/LICENCE %{buildroot}/usr/share/package-licenses/hugo/ed5b15bb1eb9603ac83502b7e06eb548b1f384da
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/hugo/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/hugo/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/miekg/mmark/LICENSE %{buildroot}/usr/share/package-licenses/hugo/75507a0611ff3ee9252bf6c9b1de336eeeb0b497
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/mitchellh/hashstructure/LICENSE %{buildroot}/usr/share/package-licenses/hugo/5e532746c55cbcc078e80cff9c6c532db022f7b2
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/mitchellh/mapstructure/LICENSE %{buildroot}/usr/share/package-licenses/hugo/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/muesli/smartcrop/LICENSE %{buildroot}/usr/share/package-licenses/hugo/60f1a26af79297be45a833fa79ea016fddf27aa0
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/nicksnyder/go-i18n/LICENSE %{buildroot}/usr/share/package-licenses/hugo/62ccfc301241ebb2fde7ead504b27c1fbca93bb6
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/niklasfasching/go-org/LICENSE %{buildroot}/usr/share/package-licenses/hugo/fb99092efe565b9a480ecb7d463bfd7a49dd6c0d
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/olekukonko/tablewriter/LICENSE.md %{buildroot}/usr/share/package-licenses/hugo/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/pelletier/go-toml/LICENSE %{buildroot}/usr/share/package-licenses/hugo/cba29923f92249281f98723c1294f9b2546c50b0
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/hugo/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/rogpeppe/go-internal/LICENSE %{buildroot}/usr/share/package-licenses/hugo/74850a25a5319bdddc0d998eb8926c18bada282b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/hugo/c4eaa8f9b736e2aced4747c352c05c16fbbb33ea
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/rwcarlsen/goexif/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2c7b0a6b6d9e0c4c7dbc9d2eac1faaa2067eaa2a
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/sanity-io/litter/LICENSE %{buildroot}/usr/share/package-licenses/hugo/3ce8448ef24e766a9de8a7e356a17334012d2a6b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/afero/LICENSE.txt %{buildroot}/usr/share/package-licenses/hugo/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/cast/LICENSE %{buildroot}/usr/share/package-licenses/hugo/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/hugo/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/fsync/LICENSE %{buildroot}/usr/share/package-licenses/hugo/1db22bdccf1a633c185b7445bb54e47892924b5b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/jwalterweatherman/LICENSE %{buildroot}/usr/share/package-licenses/hugo/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/hugo/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/spf13/viper/LICENSE %{buildroot}/usr/share/package-licenses/hugo/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/subosito/gotenv/LICENSE %{buildroot}/usr/share/package-licenses/hugo/e149fd13c863538e9c1c2e373c502be37ff20ebe
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/tdewolff/minify/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/hugo/d51d5c00974845892268cf9de5929e466563d7a6
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/tdewolff/parse/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/hugo/d51d5c00974845892268cf9de5929e466563d7a6
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/yuin/goldmark-highlighting/LICENSE %{buildroot}/usr/share/package-licenses/hugo/efbb6e2284183e25da23cf92f883857f5c239128
cp %{_builddir}/hugo-vendor-0.74.0/vendor/github.com/yuin/goldmark/LICENSE %{buildroot}/usr/share/package-licenses/hugo/efbb6e2284183e25da23cf92f883857f5c239128
cp %{_builddir}/hugo-vendor-0.74.0/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/hugo/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/hugo-vendor-0.74.0/vendor/gocloud.dev/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/image/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/hugo-vendor-0.74.0/vendor/golang.org/x/xerrors/LICENSE %{buildroot}/usr/share/package-licenses/hugo/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
cp %{_builddir}/hugo-vendor-0.74.0/vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/hugo/ab32a5c14ccc0a6d38e173568a5577493e3f6870
cp %{_builddir}/hugo-vendor-0.74.0/vendor/google.golang.org/api/googleapi/internal/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/hugo/e99e0980a6d8f06248a213a988ba1bb3c8d4a76b
cp %{_builddir}/hugo-vendor-0.74.0/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/hugo-vendor-0.74.0/vendor/gopkg.in/ini.v1/LICENSE %{buildroot}/usr/share/package-licenses/hugo/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
cp %{_builddir}/hugo-vendor-0.74.0/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/hugo/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/hugo-vendor-0.74.0/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/hugo/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/hugo-vendor-0.74.0/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/hugo/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
true # nothing to do... skip this step
## install_append content
install -d -m0755 %{buildroot}/usr/bin
install -m0755 hugo %{buildroot}/usr/bin/hugo
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hugo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hugo/02b1b9a6cb5e0ee06071eb0549bb8161c1ab58db
/usr/share/package-licenses/hugo/0762264440482182008eccd281bcd674a208a2ed
/usr/share/package-licenses/hugo/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/hugo/10a2ce5b9834456e89143edcc2a65b044dbde493
/usr/share/package-licenses/hugo/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/hugo/1b2d963c77ddfc6454ca369fc4884e87e256a2e1
/usr/share/package-licenses/hugo/1db22bdccf1a633c185b7445bb54e47892924b5b
/usr/share/package-licenses/hugo/20d7220031a3670d7696be5330ebae9f49861d3b
/usr/share/package-licenses/hugo/271aeaf56ee621c5accfc2a9db0b10717e038eaf
/usr/share/package-licenses/hugo/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/hugo/2bda142bd58fd76f408cf18fa997d8fab0278a22
/usr/share/package-licenses/hugo/2c7b0a6b6d9e0c4c7dbc9d2eac1faaa2067eaa2a
/usr/share/package-licenses/hugo/307711a68aa375a23d90191db6f720426cf88402
/usr/share/package-licenses/hugo/33cd8e150548e595fbe201c6ca9df582976e71db
/usr/share/package-licenses/hugo/3ce8448ef24e766a9de8a7e356a17334012d2a6b
/usr/share/package-licenses/hugo/4052101a660a7d8343c13ada130123f75f1dd408
/usr/share/package-licenses/hugo/4a606a34022a7ef2eab88e43148dd48547d3c017
/usr/share/package-licenses/hugo/4b5f40487c165cf31691824a93d375fcb65ea30a
/usr/share/package-licenses/hugo/523489384296f403da31edf8edf6f9023d328517
/usr/share/package-licenses/hugo/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/hugo/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/hugo/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/hugo/5e532746c55cbcc078e80cff9c6c532db022f7b2
/usr/share/package-licenses/hugo/60f1a26af79297be45a833fa79ea016fddf27aa0
/usr/share/package-licenses/hugo/62ccfc301241ebb2fde7ead504b27c1fbca93bb6
/usr/share/package-licenses/hugo/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/hugo/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/hugo/75507a0611ff3ee9252bf6c9b1de336eeeb0b497
/usr/share/package-licenses/hugo/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
/usr/share/package-licenses/hugo/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
/usr/share/package-licenses/hugo/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/hugo/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/hugo/8199e72e0dd480f4e58942cb7d99e2bbff41cb33
/usr/share/package-licenses/hugo/820a47085e1f88859859d16b894bc93b47683498
/usr/share/package-licenses/hugo/82a8c1857c790563bd8e518ed775956006f68485
/usr/share/package-licenses/hugo/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
/usr/share/package-licenses/hugo/86deafa660209c3e1ca6978b667af6d5d2e30efe
/usr/share/package-licenses/hugo/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/hugo/91cd2d65a9945545fba9e4d03f279aff97470252
/usr/share/package-licenses/hugo/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/hugo/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/hugo/96e730c77952892784bebe06fd42b297b67ea06e
/usr/share/package-licenses/hugo/9893c30cda569ecb5d3f8d615986e948947cd56d
/usr/share/package-licenses/hugo/9abb08f99d05d02f923149766fa509b9a1d82368
/usr/share/package-licenses/hugo/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/hugo/a1605d0f5823bc71559ce2bd0b50515687fbb97b
/usr/share/package-licenses/hugo/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/hugo/ab32a5c14ccc0a6d38e173568a5577493e3f6870
/usr/share/package-licenses/hugo/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/hugo/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/hugo/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/hugo/ba44327dd26d6de65733341ace192d85ae2dc46d
/usr/share/package-licenses/hugo/c4eaa8f9b736e2aced4747c352c05c16fbbb33ea
/usr/share/package-licenses/hugo/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/hugo/cba29923f92249281f98723c1294f9b2546c50b0
/usr/share/package-licenses/hugo/d51d5c00974845892268cf9de5929e466563d7a6
/usr/share/package-licenses/hugo/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/hugo/e149fd13c863538e9c1c2e373c502be37ff20ebe
/usr/share/package-licenses/hugo/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
/usr/share/package-licenses/hugo/e99e0980a6d8f06248a213a988ba1bb3c8d4a76b
/usr/share/package-licenses/hugo/ece3df1263c100f93c427face535a292723d38e7
/usr/share/package-licenses/hugo/ed5b15bb1eb9603ac83502b7e06eb548b1f384da
/usr/share/package-licenses/hugo/eee5b07a657266ef6c5c20acee6685ac6732cd19
/usr/share/package-licenses/hugo/efbb6e2284183e25da23cf92f883857f5c239128
/usr/share/package-licenses/hugo/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
/usr/share/package-licenses/hugo/fb99092efe565b9a480ecb7d463bfd7a49dd6c0d
/usr/share/package-licenses/hugo/feb9285b75d0c82a47d32e7d4dc84eb02db9ee34
/usr/share/package-licenses/hugo/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

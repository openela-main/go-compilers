Name:           go-compilers
Version:        1
Release:        20%{?dist}
Summary:        Go language compilers for various architectures
Group:          Development/Tools
License:        GPLv3+
Source0:        macros.golang-compiler

# FIXME: This is defined in go-srpm-macros why do we need it here?
%global go_arches   x86_64 aarch64 ppc64le s390x %{ix86}
ExclusiveArch:  %{go_arches}

# for install, cut and rm commands
BuildRequires:  coreutils
# for go specific macros
BuildRequires:  go-srpm-macros

%description
The package provides correct golang language compiler
base on an architectures.

%ifarch %{golang_arches}
%package golang-compiler
Summary:       compiler for golang

Requires:      golang

Provides:      compiler(go-compiler) = 2
Provides:      compiler(golang)

%description golang-compiler
Compiler for golang.
%endif

%prep
# nothing to prep, just for hooks

%build
# nothing to build, just for hooks

%install
%ifarch %{golang_arches}
install -m 644 -D %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.golang-compiler
%endif

%ifarch %{golang_arches}
%files golang-compiler
%{_rpmconfigdir}/macros.d/macros.golang-compiler
%endif

%changelog
* Fri Dec 21 2018 Tom Stellard <tstellar@redhat.com> - 1-20
- Add -compressdwarf=false to ldflags

* Mon Nov 19 2018 Derek Parker <deparker@redhat.com> - 1-19
- Update to remove SCL
- Resolves: rhbz#1642080

* Mon Aug 6 2018 Derek Parker <deparker@redhat.com> - 1-18
- Update to use new golang SCL package

* Wed Jun 20 2018 Derek Parker <deparker@redhat.com> - 1-17
- Fix gobuild macro more, seperate for greedy arguments

* Fri Jun 15 2018 Troy Dawson <tdawson@redhat.com> - 1-16
- Fix gobuild macro

* Fri Apr 13 2018 Tom Stellard <tstellar@redhat.com> - 1-15
- Use go-toolset-7 instead of golang
- Drop gcc-go

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Jakub Čajka <jcajka@redhat.com> - 1-12
- rebuild for ppc64 drop

* Wed Feb 15 2017 Jakub Čajka <jcajka@redhat.com> - 1-11
- pie is not supported on ppc64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jakub Čajka <jcajka@redhat.com> - 1-9
- Add crash traceback level to golang as default
- Switch to PIE and push distribution ld flags
- Resolves BZ#1413529
- Related BZ#1411242

* Wed Jul 20 2016 Jakub Čajka <jcajka@redhat.com> - 1-8
- Build for s390x switch to golang
- Related: bz1357394

* Wed Apr 13 2016 Dan Horák <dan[at]danny.cz> - 1-7
- fix bug in gcc-go version of gotest macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Jakub Čajka <jcajka@redhat.com> - 1-5
- Build for {power64} switch to golang

* Fri Jan 22 2016 Jakub Čajka <jcajka@redhat.com> - 1-4
- version provides to make seamless transition between compilers possible
- Resolves: bz#1300717

* Thu Nov 12 2015 Jakub Čajka <jcajka@redhat.com> - 1-3
- remove version requirement from gcc-go subpackage to avoid cyclic
  dependency due to macro declaration in subpackage

* Thu Sep 10 2015 jchaloup <jchaloup@redhat.com> - 1-2
- go_compiler macro must be in go-srpm-macros package as it is used
  to pick compiler(go-compiler) which would provide go_compiler

* Tue Jul 07 2015 Jan Chaloupka <jchaloup@redhat.com> - 1-1
- Initial commit
  resolves: #1258182

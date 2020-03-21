#
# Conditional build:
%bcond_with	tests		# unit tests [not present when repackaging .gem file]
# test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	pkgname	rspec-expectations
Summary:	Rspec-2 expectations (should and matchers)
Summary(pl.UTF-8):	Oczekiwania Rspec-2 (should oraz matchers)
Name:		ruby-%{pkgname}
Version:	3.7.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	23a198e5227cb308417efef6d136c41e
URL:		http://github.com/rspec/rspec-expectations
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby >= 1:1.8.7
%if %{with tests}
BuildRequires:	ruby-minitest >= 5.2
BuildRequires:	ruby-rspec
BuildRequires:	ruby-rspec-support >= 3.7.0
%endif
# .gemspec contains: s.add_dependency(%q<diff-lcs>.freeze, ["< 2.0", ">= 1.2.0"])
# but only "rubygems(diff-lcs) < 2.0" is detected, "rubygems(diff-lcs) >= 1.2.0" not...
Requires:	ruby-diff-lcs >= 1.2.0
Requires:	ruby-diff-lcs < 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rspec-expectations adds `should` and `should_not` to every object and
includes RSpec::Matchers, a library of standard matchers.

%description -l pl.UTF-8
rspec-expectations dodaje `should` oraz `should_not` do każdego
obiektu oraz zawiera RSpec::Matchers - bibliotekę standardowych
funkcji dopasowujących.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
ruby -rubygems -Ilib/ -S rspec spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md LICENSE.md
%{ruby_vendorlibdir}/rspec/expectations.rb
%{ruby_vendorlibdir}/rspec/expectations
%{ruby_vendorlibdir}/rspec/matchers.rb
%{ruby_vendorlibdir}/rspec/matchers
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

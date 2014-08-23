#
# Conditional build:
%bcond_without	tests		# build without tests
# test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	gem_name	rspec-expectations
Summary:	Rspec-2 expectations (should and matchers)
Summary(pl.UTF-8):	Oczekiwania Rspec-2 (should oraz matchers)
Name:		ruby-%{gem_name}
Version:	2.13.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	2873d31ef1f8f65d3a04ac40e27825a1
URL:		http://github.com/rspec/rspec-expectations
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-diff-lcs
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
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
ruby -rubygems -Ilib/ -S rspec spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

# cleanups
rm -f $RPM_BUILD_ROOT%{gem_instdir}/{.document,.gitignore,.travis.yml,.yardopts}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md License.txt
%{ruby_vendorlibdir}/rspec-expectations.rb
%{ruby_vendorlibdir}/rspec/matchers.rb
%{ruby_vendorlibdir}/rspec/matchers
%{ruby_vendorlibdir}/rspec/expectations.rb
%{ruby_vendorlibdir}/rspec/expectations

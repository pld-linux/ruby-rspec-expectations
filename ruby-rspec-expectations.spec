#
# Conditional build:
%bcond_with	bootstrap		# build with boostrap
%bcond_without	tests		# build without tests

%if %{with boostrap}
%undefine	with_tests
%endif

# bootstrap: test needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core

%define	gem_name	rspec-expectations
Summary:	Rspec-2 expectations (should and matchers)
Name:		ruby-%{gem_name}
Version:	2.13.0
Release:	0.1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	2873d31ef1f8f65d3a04ac40e27825a1
URL:		http://github.com/rspec/rspec-expectations
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{without bootstrap}
BuildRequires:	ruby-minitest
BuildRequires:	ruby-rspec
%endif
Requires:	ruby-diff-lcs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rspec-expectations adds `should` and `should_not` to every object and
includes RSpec::Matchers, a library of standard matchers.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


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

%if 0
%files	doc
%defattr(644,root,root,755)
%endif

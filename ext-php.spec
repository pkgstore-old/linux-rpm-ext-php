%global app                     php
%global d_conf                  %{_sysconfdir}/%{app}.d
%global release_prefix          100

Name:                           ext-php
Version:                        1.0.2
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure PHP
License:                        MIT
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source10:                       %{app}.custom.ini

Requires:                       php
Requires:                       php-gd
Requires:                       php-gmp
Requires:                       php-imap
Requires:                       php-intl
Requires:                       php-mbstring
Requires:                       php-mysqlnd
Requires:                       php-odbc
Requires:                       php-opcache
Requires:                       php-pdo
Requires:                       php-pecl-geoip
Requires:                       php-pecl-imagick
Requires:                       php-pecl-memcached
Requires:                       php-pecl-redis4
Requires:                       php-pecl-zip
Requires:                       php-pecl-uploadprogress
Requires:                       php-xml

%description
META-package for install and configure PHP.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_conf}/99-%{app}.custom.ini


%files
%config(noreplace) %{d_conf}/99-%{app}.custom.ini


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-103
- Update SPEC-file.

* Tue Apr 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-102
- UPD: Add "php-pecl-zip".

* Wed Apr 24 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-101
- UPD: Add "php-gmp".

* Fri Feb 15 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- NEW: 1.0.1-100.

* Thu Jan 03 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- UPD: Remove "remi-release-29" requires.

* Wed Jan 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.

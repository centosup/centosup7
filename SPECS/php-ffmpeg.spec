%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")

Name:           php-ffmpeg
Version:        0.6.0
Release:        1%{?dist}
Summary:        Extension to manipulate movie in PHP

Group:          Development/Languages
License:        GPLv2
URL:            http://ffmpeg-php.sourceforge.net/
Source0:        http://centosup.ispsystem.info/7/SOURCES/ffmpeg-php-0.6.0~git-tony2001-pached.tgz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ffmpeg-devel >= 0.5, php-devel, php-gd
Requires:       php-gd

%description
ffmpeg-php is an extension for PHP that adds an easy to use, object-oriented
API for accessing and retrieving information from video and audio files. 
It has methods for returning frames from movie files as images that can be 
manipulated using PHP's image functions. This works well for automatically 
creating thumbnail images from movies. ffmpeg-php is also useful for reporting
the duration and bitrate of audio files (mp3, wma...). ffmpeg-php can access
many of the video formats supported by ffmpeg (mov, avi, mpg, wmv...).

%prep
%setup -q -n ffmpeg-php-%{version}

%build
phpize
./configure
make


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

# install config file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/%{name}.ini << 'EOF'
; --- Enable %{name} extension module
extension=ffmpeg.so

; --- options for %{name} 
;ffmpeg.allow_persistent = 0
;ffmpeg.show_warnings = 0
EOF

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog CREDITS EXPERIMENTAL INSTALL LICENSE TODO test_ffmpeg.php
%config(noreplace) %{_sysconfdir}/php.d/%{name}.ini
%{php_extdir}/ffmpeg.so




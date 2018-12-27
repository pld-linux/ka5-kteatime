%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kteatime
Summary:	kteatime
Summary(pl.UTF-8):	kteatime
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e6ecd3159ec17e49df663f99da98fb4f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.46.0
BuildRequires:	kf5-kconfig-devel >= 5.46.0
BuildRequires:	kf5-kcrash-devel >= 5.46.0
BuildRequires:	kf5-kdoctools-devel >= 5.46.0
BuildRequires:	kf5-ki18n-devel >= 5.46.0
BuildRequires:	kf5-kiconthemes-devel >= 5.46.0
BuildRequires:	kf5-knotifications-devel >= 5.46.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.46.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.46.0
BuildRequires:	kf5-kxmlgui-devel >= 5.46.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTeaTime is a handy timer for steeping tea. No longer will you have to
guess at how long it takes for your tea to be ready. Simply select the
type of tea you have, and it will alert you when the tea is ready to
drink.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_desktopdir}/org.kde.kteatime.desktop
%{_iconsdir}/hicolor/16x16/apps/kteatime.png
%{_iconsdir}/hicolor/22x22/apps/kteatime.png
%{_iconsdir}/hicolor/32x32/apps/kteatime.png
%{_iconsdir}/hicolor/48x48/apps/kteatime.png
%{_iconsdir}/hicolor/64x64/apps/kteatime.png
%{_iconsdir}/hicolor/scalable/apps/kteatime.svgz
%{_datadir}/knotifications5/kteatime.notifyrc
%{_datadir}/metainfo/org.kde.kteatime.appdata.xml

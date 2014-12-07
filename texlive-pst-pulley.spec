# revision 25142
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-pulley
# catalog-date 2012-01-18 12:22:27 +0100
# catalog-license lppl1.3
# catalog-version 0.01
Name:		texlive-pst-pulley
Version:	0.01
Release:	8
Summary:	Plot pulleys, using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-pulley
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pulley.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pulley.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-pulley.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to draw pulley systems with up to
6 pulleys. The pulley diagrams are labelled with the physical
properties of the system. The package uses pstricks, and
requires a several pstricks-related packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-pulley/pst-pulley.tex
%{_texmfdistdir}/tex/latex/pst-pulley/pst-pulley.sty
%doc %{_texmfdistdir}/doc/generic/pst-pulley/Changes
%doc %{_texmfdistdir}/doc/generic/pst-pulley/README
%doc %{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-pulley/pst-pulley-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-pulley/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01-1
+ Revision: 762705
- texlive-pst-pulley
- texlive-pst-pulley


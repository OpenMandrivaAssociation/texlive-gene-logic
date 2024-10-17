Name:		texlive-gene-logic
Version:	15878
Release:	2
Summary:	Typeset logic formulae, etc
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/logic
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a facility to typeset certain logic
formulae. It provides an environment like eqnarray, an extended
newtheorem environment, and several macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gene-logic/gn-logic14.sty
%doc %{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.pdf
%doc %{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
